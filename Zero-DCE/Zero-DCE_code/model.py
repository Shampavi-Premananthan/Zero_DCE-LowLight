import torch
import torch.nn as nn
import torch.nn.functional as F
import math
#import pytorch_colors as colors
import numpy as np


class ChannelAttention(nn.Module):
	"""Channel Attention Module"""
	def __init__(self, in_channels, reduction=8):
		super(ChannelAttention, self).__init__()
		self.avg_pool = nn.AdaptiveAvgPool2d(1)
		self.max_pool = nn.AdaptiveMaxPool2d(1)
		
		self.fc = nn.Sequential(
			nn.Conv2d(in_channels, in_channels // reduction, 1, bias=False),
			nn.ReLU(inplace=True),
			nn.Conv2d(in_channels // reduction, in_channels, 1, bias=False)
		)
		self.sigmoid = nn.Sigmoid()
	
	def forward(self, x):
		avg_out = self.fc(self.avg_pool(x))
		max_out = self.fc(self.max_pool(x))
		out = avg_out + max_out
		return self.sigmoid(out)


class SpatialAttention(nn.Module):
	"""Spatial Attention Module"""
	def __init__(self, kernel_size=7):
		super(SpatialAttention, self).__init__()
		padding = (kernel_size - 1) // 2
		self.conv = nn.Conv2d(2, 1, kernel_size, padding=padding, bias=False)
		self.sigmoid = nn.Sigmoid()
	
	def forward(self, x):
		avg_out = torch.mean(x, dim=1, keepdim=True)
		max_out, _ = torch.max(x, dim=1, keepdim=True)
		out = torch.cat([avg_out, max_out], dim=1)
		out = self.conv(out)
		return self.sigmoid(out)


class CBAM(nn.Module):
	"""Convolutional Block Attention Module"""
	def __init__(self, in_channels, reduction=8, kernel_size=7):
		super(CBAM, self).__init__()
		self.channel_attention = ChannelAttention(in_channels, reduction)
		self.spatial_attention = SpatialAttention(kernel_size)
	
	def forward(self, x):
		x = x * self.channel_attention(x)
		x = x * self.spatial_attention(x)
		return x


class enhance_net_nopool(nn.Module):

	def __init__(self):
		super(enhance_net_nopool, self).__init__()

		self.relu = nn.ReLU(inplace=True)

		number_f = 32
		self.e_conv1 = nn.Conv2d(3,number_f,3,1,1,bias=True) 
		self.e_conv2 = nn.Conv2d(number_f,number_f,3,1,1,bias=True) 
		self.e_conv3 = nn.Conv2d(number_f,number_f,3,1,1,bias=True) 
		self.e_conv4 = nn.Conv2d(number_f,number_f,3,1,1,bias=True) 
		self.e_conv5 = nn.Conv2d(number_f*2,number_f,3,1,1,bias=True) 
		self.e_conv6 = nn.Conv2d(number_f*2,number_f,3,1,1,bias=True) 
		self.e_conv7 = nn.Conv2d(number_f*2,24,3,1,1,bias=True) 

		# Attention modules
		self.attn1 = CBAM(number_f)
		self.attn2 = CBAM(number_f)
		self.attn3 = CBAM(number_f)
		self.attn4 = CBAM(number_f)

		self.maxpool = nn.MaxPool2d(2, stride=2, return_indices=False, ceil_mode=False)
		self.upsample = nn.UpsamplingBilinear2d(scale_factor=2)


		
	def forward(self, x):

		x1 = self.relu(self.e_conv1(x))
		# x1 = self.attn1(x1)  # Disabled for speed
		# p1 = self.maxpool(x1)
		x2 = self.relu(self.e_conv2(x1))
		# x2 = self.attn2(x2)  # Disabled for speed
		# p2 = self.maxpool(x2)
		x3 = self.relu(self.e_conv3(x2))
		# x3 = self.attn3(x3)  # Disabled for speed
		# p3 = self.maxpool(x3)
		x4 = self.relu(self.e_conv4(x3))
		# x4 = self.attn4(x4)  # Disabled for speed

		x5 = self.relu(self.e_conv5(torch.cat([x3,x4],1)))
		# x5 = self.upsample(x5)
		x6 = self.relu(self.e_conv6(torch.cat([x2,x5],1)))

		x_r = F.tanh(self.e_conv7(torch.cat([x1,x6],1)))
		r1,r2,r3,r4,r5,r6,r7,r8 = torch.split(x_r, 3, dim=1)


		x = x + r1*(torch.pow(x,2)-x)
		x = x + r2*(torch.pow(x,2)-x)
		x = x + r3*(torch.pow(x,2)-x)
		enhance_image_1 = x + r4*(torch.pow(x,2)-x)		
		x = enhance_image_1 + r5*(torch.pow(enhance_image_1,2)-enhance_image_1)		
		x = x + r6*(torch.pow(x,2)-x)	
		x = x + r7*(torch.pow(x,2)-x)
		enhance_image = x + r8*(torch.pow(x,2)-x)
		r = torch.cat([r1,r2,r3,r4,r5,r6,r7,r8],1)
		return enhance_image_1,enhance_image,r



