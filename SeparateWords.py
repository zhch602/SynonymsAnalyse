# coding=utf-8
import jieba
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

inputFileName = "d:\\data\\corpus.txt"  # source file
outputFileName = "d:\\data\\operated.txt"  # source file

f1 = open(inputFileName)
f2 = open(outputFileName, 'a')
lines = f1.readlines()
for line in lines:
    seg_list = jieba.cut(line, cut_all=False)
    f2.write(" ".join(seg_list))
f1.close()
f2.close()
