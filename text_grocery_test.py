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
import random

from tgrocery import Grocery

grocery = Grocery('sample')


# 准备数据
def prepare_train_data(text_path, proportion):
    train_data = []
    test_data = []
    text_abs_path = os.path.abspath(text_path)
    for subdir in os.listdir(text_path):
        label = subdir
        sub_abs_text_path = text_abs_path + '/' + subdir
        for text_filename in os.listdir(sub_abs_text_path):
            text_fp = open(sub_abs_text_path + '/' + text_filename)
            text = text_fp.read()
            if random.random() <= proportion:
                train_data.append((label, text))
            else:
                test_data.append((label, text))

    return train_data, test_data


if __name__ == '__main__':
    train_data, test_data = prepare_train_data('ocr_result', 0.8)
    train_data_size = len(train_data)
    test_data_size = len(test_data)

    grocery.train(train_data)
    grocery.save()
    new_grocery = Grocery('sample')
    new_grocery.load()
    true_num = 0
    print 'actual\t|\tpredict\t|\ttrue?'
    print '----------------------------'
    for (actual, text) in test_data:
        predict = new_grocery.predict(text)
        is_true = 'true' if actual == predict.predicted_y else 'false'
        if is_true == 'true':
            true_num += 1
        print '{actual}\t|\t{predict}\t|\t{is_true}'.format(actual=actual, predict=predict, is_true=is_true)

    print '----------------------------'
    print '训练数据集大小: {size}'.format(size=train_data_size)
    print '测试数据集大小: {size}'.format(size=test_data_size)
    print '正确数: {true_num}    错误数: {false_num}'.format(true_num=true_num, false_num=test_data_size-true_num)
    print '准确率: {accuracy}%'.format(accuracy=float(100.0 * true_num / test_data_size))
