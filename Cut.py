# coding=utf-8

import jieba
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def cut(input_file_name, output_file_name):
    input_file = open(input_file_name, 'r')
    output_file = open(output_file_name, 'w')

    lines = input_file.readlines()

    for line in lines:
        seg_list = jieba.cut(line, cut_all=False)
        output_file.write(" ".join(seg_list))

    input_file.close()
    output_file.close()
