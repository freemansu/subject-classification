# coding=utf-8
import codecs

import baidu_api
import os
import json


# Convert all images to text
def to_text(image_path, text_path, access_token):
    image_abspath = os.path.abspath(image_path)
    text_abspath = os.path.abspath(text_path)

    for subdir in os.listdir(image_abspath):
        sub_image_path = image_abspath + '/' + subdir
        sub_text_path = text_abspath + '/' + subdir
        os.mkdir(sub_text_path)
        for image_filename in os.listdir(sub_image_path):
            if image_filename.endswith('.jpg'):
                text = baidu_api.ocr(access_token, sub_image_path + '/' + image_filename)
                text_fp = codecs.open(sub_text_path + '/' + image_filename[0:-4] + '.txt', 'w', 'utf-8')
                text_fp.write(text)


if __name__ == '__main__':
    filename = 'config.json'
    config = json.load(open(filename))
    to_text('images', 'ocr_result', config['access_token'])
