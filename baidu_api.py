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
    encoded_string.replace('\/', '%')
    data = 'image=' + encoded_string

    response = requests.post(url=url, headers=headers, params=payload, data=data)
    words_result = json.loads(response.text)['words_result']
    for words_item in words_result:
        print words_item['words']

    print response.text


if __name__ == '__main__':
    filename = 'config.json'
    config = json.load(open(filename))
    # access_token = get_access_token(config=config)

    ocr(config['access_token'], 'images/01.jpg')
