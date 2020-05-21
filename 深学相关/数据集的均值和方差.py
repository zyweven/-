# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 18:18:50 2019

@author: 张译文
"""

import numpy as np
import cv2
import random
import os
# calculate means and std
from tqdm import tqdm
import numpy as np
 
train_txt_path = './image_sets/training.txt'  # 数据集images name索引txt
image_prefix = './images'  # 图片
 
CNum = 659  # select images 取前10000张图片作为计算样本
 
img_h, img_w = 32, 32
imgs = np.zeros([img_w, img_h, 3, 1])
means, stdevs = [], []
 
with open(train_txt_path, 'r') as f:
    lines = f.readlines() # 读取全部image name
    random.shuffle(lines)  # shuffle images
 
    for i in tqdm(range(CNum)):
        file_name = lines[i].strip()
        img_path = os.path.join(image_prefix, file_name)
 
        img = cv2.imread(img_path)
        img = cv2.resize(img, (img_h, img_w)) # 将图片进行裁剪[32,32]
        img = img[:, :, :, np.newaxis]
        imgs = np.concatenate((imgs, img), axis=3)
#         print(i)
 
imgs = imgs.astype(np.float32) / 255.
 
for i in tqdm(range(3)):
    pixels = imgs[:, :, i, :].ravel()  # flatten
    means.append(np.mean(pixels))
    stdevs.append(np.std(pixels))
 
# cv2 : BGR
means.reverse()  # BGR --> RGB
stdevs.reverse()
 
print("normMean = {}".format(means))
print("normStd = {}".format(stdevs))
print('transforms.Normalize(normMean = {}, normStd = {})'.format(means, stdevs))
