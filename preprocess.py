from PIL import Image
import os
import pathlib
import csv
import numpy as np
from shutil import copyfile
from collections import Counter

IMG_DIR = "CelebAMask-HQ/CelebA-HQ-img/"
MASK_DIR = "CelebAMask-HQ/CelebAMask-HQ-mask-anno/"

NEW_FOLDER = "CelebAMask"

NEW_MASK_DIR_TRAIN = "CelebAMask/train_mask/"
NEW_MASK_DIR_TEST = "CelebAMask/test_mask/"

NEW_IMG_DIR_TRAIN = "CelebAMask/train_img/"
NEW_IMG_DIR_TEST = "CelebAMask/test_img/"


data_dir = pathlib.Path(NEW_FOLDER)
if not data_dir.exists():
	os.mkdir(NEW_FOLDER)
	
data_dir = pathlib.Path(NEW_IMG_DIR_TRAIN)
if not data_dir.exists():
	os.mkdir(NEW_IMG_DIR_TRAIN)
data_dir = pathlib.Path(NEW_IMG_DIR_TEST)
if not data_dir.exists():
	os.mkdir(NEW_IMG_DIR_TEST)


data_dir = pathlib.Path(NEW_MASK_DIR_TRAIN)
if not data_dir.exists():
	os.mkdir(NEW_MASK_DIR_TRAIN)
data_dir = pathlib.Path(NEW_MASK_DIR_TEST)
if not data_dir.exists():
	os.mkdir(NEW_MASK_DIR_TEST)


train = []
test = []

with open('train_test_split-10e5aa2b-26ae-4110-b7a6-2beed2c7da6a.csv', newline='') as csvfile:
	imgs = csv.reader(csvfile, delimiter=',')
	for i in imgs:
		if i[1] == 'True':
			train.append(i[0])
		if i[1] == 'False':
			test.append(i[0])


for i in range(len(train)):
	image = Image.open(IMG_DIR + train[i])
	new_image = image.resize((128, 128))
	new_image.save(NEW_IMG_DIR_TRAIN + train[i])


for i in range(len(test)):
	image = Image.open(IMG_DIR + test[i])
	new_image = image.resize((128, 128))
	new_image.save(NEW_IMG_DIR_TEST + test[i])


for subdir, dirs, files in os.walk(MASK_DIR):
    for file in files:
    	if file == ".DS_Store":
    		continue
    	name = str(int(file.split('_')[0])) + '.jpg'
    	if name in train:
			image = Image.open(os.path.join(subdir, file))
			new_image = image.resize((128, 128))
			new_image.save(NEW_MASK_DIR_TRAIN + file)
    	if name in test:
			image = Image.open(os.path.join(subdir, file))
			new_image = image.resize((128, 128))
			new_image.save(NEW_MASK_DIR_TEST + file)
