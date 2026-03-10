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
import numpy as np
from torchvision import transforms
from PIL import Image
import glob
import time


 
def lowlight(image_path, device, ckpt_path, enhancement_strengths=[1.0, 1.7]):
	data_lowlight = Image.open(image_path)

 

	data_lowlight = (np.asarray(data_lowlight)/255.0)


	data_lowlight = torch.from_numpy(data_lowlight).float()
	data_lowlight = data_lowlight.permute(2,0,1)
	data_lowlight = data_lowlight.to(device).unsqueeze(0)

	DCE_net = model.enhance_net_nopool().to(device)
	# Allow loading older checkpoints without attention weights; missing keys fall back to default init
	state_dict = torch.load(ckpt_path, map_location=device)
	load_info = DCE_net.load_state_dict(state_dict, strict=False)
	if load_info.missing_keys:
		print(f"Warning: missing keys in checkpoint (using defaults): {load_info.missing_keys}")
	if load_info.unexpected_keys:
		print(f"Warning: unexpected keys in checkpoint (ignored): {load_info.unexpected_keys}")
	start = time.time()
	_,enhanced_image,A = DCE_net(data_lowlight)

	end_time = (time.time() - start)
	print(f"Inference time: {end_time:.4f}s")
	
	# Generate multiple outputs with different enhancement strengths
	result_path = image_path.replace('test_data','result')
	result_dir = os.path.dirname(result_path)
	if not os.path.exists(result_dir):
		os.makedirs(result_dir)
	
	base_path, ext = os.path.splitext(result_path)
	
	for idx, strength in enumerate(enhancement_strengths, 1):
		if strength == 1.0:
			# Standard output
			output_path = result_path
			torchvision.utils.save_image(enhanced_image, output_path)
			print(f"  Saved: {output_path}")
		else:
			# Adjust enhancement by interpolating between original and enhanced image
			# strength=1.0 -> original, strength=2.0 -> 2x enhancement, etc.
			adjusted_enhanced = data_lowlight + (strength - 1.0) * (enhanced_image - data_lowlight)
			adjusted_enhanced = torch.clamp(adjusted_enhanced, 0, 1)
			
			output_path = f"{base_path}_v{idx}{ext}"
			torchvision.utils.save_image(adjusted_enhanced, output_path)
			print(f"  Saved (strength={strength}): {output_path}")

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--device', type=str, default='cuda', choices=['cuda', 'cpu'])
	parser.add_argument('--checkpoint', type=str, default='snapshots/Epoch99.pth')
	parser.add_argument('--test_dir', type=str, default='data/test_data/')
	parser.add_argument('--strength1', type=float, default=1.0)
	parser.add_argument('--strength2', type=float, default=1.7)
	
	args = parser.parse_args()
	
	if args.device == 'cuda' and not torch.cuda.is_available():
		print("CUDA not available; using CPU.")
		device = torch.device('cpu')
	else:
		device = torch.device(args.device)
	
	print(f"Using device: {device}")
	print(f"Checkpoint: {args.checkpoint}")
	print(f"Enhancement strengths: {args.strength1}, {args.strength2}\n")
	
	if not os.path.exists(args.checkpoint):
		print(f"Error: Checkpoint not found at {args.checkpoint}")
		sys.exit(1)

# test_images
	with torch.no_grad():
		filePath = args.test_dir
		file_list = os.listdir(filePath)

		for file_name in file_list:
			test_list = glob.glob(filePath+file_name+"/*") 
			for image in test_list:
				print(f"\nProcessing: {image}")
				lowlight(image, device, args.checkpoint, [args.strength1, args.strength2])

		

