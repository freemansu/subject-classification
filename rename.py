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

import os

images_dir = 'images'
for subdir in os.listdir(images_dir):
    i = 1
    for filename in os.listdir(images_dir + '/' + subdir):
        if filename.endswith('.jpg'):
            path = './' + images_dir + '/' + subdir + '/'
            os.rename(path + filename, path + subdir + str(i).zfill(3) + '.jpg')
            i += 1
