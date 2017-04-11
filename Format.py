# coding=utf-8

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def format(input_file_name, output_file_name):

    input_file = open(input_file_name, 'r')
    output_file = open(output_file_name, 'w')

    lines = input_file.readlines()

    for line in lines:
        line.replace('<content>', '').replace('</content>', '').replace('\t', '').replace('\n', '').replace(' ', '')
        if line.strip() == "":
            continue
        output_file.write(line)

    input_file.close()
    output_file.close()