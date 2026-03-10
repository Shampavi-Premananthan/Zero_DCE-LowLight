import torch
import torch.nn as nn
import torchvision
import torch.backends.cudnn as cudnn
import torch.optim
import os
import sys
import argparse
import time
import dataloader
import model
import Myloss
import numpy as np
from torchvision import transforms


def weights_init(m):
    classname = m.__class__.__name__
    if classname.find('Conv') != -1:
        m.weight.data.normal_(0.0, 0.02)
    elif classname.find('BatchNorm') != -1:
        m.weight.data.normal_(1.0, 0.02)
        m.bias.data.fill_(0)


def set_seed(seed):
	if seed is None:
		return
	import random
	random.seed(seed)
	np.random.seed(seed)
	torch.manual_seed(seed)
	if torch.cuda.is_available():
		torch.cuda.manual_seed_all(seed)





def train(config):
	# Select device: allow override via --device
	if config.device == 'cuda' and not torch.cuda.is_available():
		print("CUDA not available; falling back to CPU.")
		device = torch.device('cpu')
	else:
		device = torch.device(config.device)
	if device.type == 'cuda':
		cudnn.benchmark = True
	print(f"Using device: {device}")

	set_seed(config.seed)

	DCE_net = model.enhance_net_nopool().to(device)

	DCE_net.apply(weights_init)
	print("Training Zero-DCE from scratch (no pre-trained weights).")
	train_dataset = dataloader.lowlight_loader(config.lowlight_images_path)

	train_loader = torch.utils.data.DataLoader(
		train_dataset,
		batch_size=config.train_batch_size,
		shuffle=True,
		num_workers=config.num_workers,
		pin_memory=torch.cuda.is_available()
	)



	L_color = Myloss.L_color()
	L_spa = Myloss.L_spa()

	L_exp = Myloss.L_exp(16,0.6)
	L_TV = Myloss.L_TV()


	optimizer = torch.optim.Adam(DCE_net.parameters(), lr=config.lr, weight_decay=config.weight_decay)
	scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=config.lr_step, gamma=config.lr_gamma)
	use_amp = config.use_amp and device.type == 'cuda'
	scaler = torch.cuda.amp.GradScaler(enabled=use_amp)
	
	DCE_net.train()

	best_loss = float('inf')
	for epoch in range(config.num_epochs):
		for iteration, img_lowlight in enumerate(train_loader):

			img_lowlight = img_lowlight.to(device)

			optimizer.zero_grad()
			with torch.cuda.amp.autocast(enabled=use_amp):
				enhanced_image_1, enhanced_image, A = DCE_net(img_lowlight)

				Loss_TV = 200 * L_TV(A)
				loss_spa = torch.mean(L_spa(enhanced_image, img_lowlight))
				loss_col = 5 * torch.mean(L_color(enhanced_image))
				loss_exp = 10 * torch.mean(L_exp(enhanced_image))

				loss = Loss_TV + loss_spa + loss_col + loss_exp

			scaler.scale(loss).backward()
			scaler.unscale_(optimizer)
			torch.nn.utils.clip_grad_norm_(DCE_net.parameters(), config.grad_clip_norm)
			scaler.step(optimizer)
			scaler.update()

			if ((iteration + 1) % config.display_iter) == 0:
				print(
					"Loss at iteration",
					iteration + 1,
					":",
					loss.item(),
					"| tv:",
					Loss_TV.item(),
					" spa:",
					loss_spa.item(),
					" col:",
					loss_col.item(),
					" exp:",
					loss_exp.item(),
				)
			if ((iteration + 1) % config.snapshot_iter) == 0:
				snapshot_path = os.path.join(
					config.snapshots_folder,
					f"Epoch{epoch}_Iter{iteration + 1}.pth",
				)
				torch.save(DCE_net.state_dict(), snapshot_path)

			if config.save_best and loss.item() < best_loss:
				best_loss = loss.item()
				best_path = os.path.join(config.snapshots_folder, "best.pth")
				torch.save(DCE_net.state_dict(), best_path)

		scheduler.step()




if __name__ == "__main__":

	parser = argparse.ArgumentParser()

	# Input Parameters
	parser.add_argument('--lowlight_images_path', type=str, default="data/train_data/")
	parser.add_argument('--lr', type=float, default=0.0001)
	parser.add_argument('--weight_decay', type=float, default=0.0001)
	parser.add_argument('--grad_clip_norm', type=float, default=0.1)
	parser.add_argument('--num_epochs', type=int, default=200)
	parser.add_argument('--train_batch_size', type=int, default=8)
	parser.add_argument('--val_batch_size', type=int, default=4)
	parser.add_argument('--num_workers', type=int, default=4)
	parser.add_argument('--display_iter', type=int, default=10)
	parser.add_argument('--snapshot_iter', type=int, default=10)
	parser.add_argument('--snapshots_folder', type=str, default="snapshots/")
	parser.add_argument('--seed', type=int, default=42)
	parser.add_argument('--device', type=str, default='cuda', choices=['cuda', 'cpu'])
	parser.add_argument('--use_amp', action='store_true')
	parser.add_argument('--lr_step', type=int, default=50)
	parser.add_argument('--lr_gamma', type=float, default=0.5)
	parser.add_argument('--save_best', action='store_true')

	config = parser.parse_args()

	os.makedirs(config.snapshots_folder, exist_ok=True)


	train(config)








	
