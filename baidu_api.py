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

import json

import requests

import base64


def get_access_token(config):
    url = 'https://aip.baidubce.com/oauth/2.0/token'
    payload = {
        'grant_type': 'client_credentials',
        'client_id': config['api_key'],
        'client_secret': config['api_secret']
    }

    response = requests.post(url, params=payload)
    return json.loads(response.text)['access_token']


def ocr(access_token, image_path):
    with open(image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read())

    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    payload = {
        'access_token': access_token
    }

    data = {
        'image': encoded_string
        # 'detect_direction': 'true'
    }

    response = requests.post(url=url, headers=headers, params=payload, data=data)
    words = ''
    if response.status_code == 200:
        print response.text
        words_result = json.loads(response.text)['words_result']
        for words_item in words_result:
            words += words_item['words']

    return words


if __name__ == '__main__':
    filename = 'config.json'
    config = json.load(open(filename))
    access_token = get_access_token(config=config)
    print access_token
    print ocr(config['access_token'], 'images/01.jpg')
