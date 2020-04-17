import os
from imutils import paths
import cv2
import imutils


BASE_IMG = os.path.join(os.getcwd(), 'image-dataset')

dir_paths = [os.path.join('image-dataset', dir) for dir in os.listdir(BASE_IMG)]
for dir_path in dir_paths:
    os.rename(dir_path, dir_path.replace(' ', '_'))

for dir_path in dir_paths:
    i = 0
    imgs = paths.list_images(dir_path)
    for img in imgs:
        print(img)

        a = imutils.resize(cv2.imread(img), height=300)
        cv2.imwrite(img, a)

        fname = img.split('\\')
        os.rename(img, os.path.join(fname[0], fname[1], f'{i:04d}.jpg'))
        i += 1