# coding=utf-8
"""
Copyright @2017 [Su Yu, yusu.work@gmail.com]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import codecs

import requests
import os


def word_segmentation(text):
    url = 'http://api.pullword.com/get.php'
    params = {
        'source': text,
        'param1': 0.7,
        'param2': 1
    }

    response = requests.post(url=url, params=params)
    if response.status_code == 200:
        return response.text


def to_word(text_path, word_path):
    text_abspath = os.path.abspath(text_path)
    word_abspath = os.path.abspath(word_path)

    for subdir in os.listdir(text_abspath):
        sub_text_path = text_abspath + '/' + subdir
        sub_word_path = word_abspath + '/' + subdir
        if not os.path.isdir(sub_word_path):
            os.mkdir(sub_word_path)
        for text_filename in os.listdir(sub_text_path):
            if text_filename.endswith('.txt'):
                word_filename = sub_word_path + '/' + text_filename[0:-4] + '.txt'
                if not os.path.isfile(word_filename) or \
                        (os.path.isfile(word_filename) and os.path.getsize(word_filename) == 0):
                    text_fp = open(sub_text_path + '/' + text_filename)
                    words = word_segmentation(text_fp.read())
                    word_fp = codecs.open(word_filename[0:-4] + '_words.txt', 'w', 'utf-8')
                    word_fp.write(words)


if __name__ == '__main__':
    to_word('ocr_result', 'word_segmentation_result')
