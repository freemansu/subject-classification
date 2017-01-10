# coding=utf-8

import os

images_dir = 'images'
for subdir in os.listdir(images_dir):
    i = 1
    for filename in os.listdir(images_dir + '/' + subdir):
        if filename.endswith('.jpg'):
            path = './' + images_dir + '/' + subdir + '/'
            os.rename(path + filename, path + subdir + str(i).zfill(3) + '.jpg')
            i += 1
