# coding=utf-8
from gensim.models import word2vec
import logging

# 主程序
logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)
sentences = word2vec.LineSentence("d:\\data\\operated2.txt")  # 加载语料
model = word2vec.Word2Vec(sentences, size=400, window=5, min_count=5, workers=4)  #训练skip-gram模型，默认window=5

model.save("word2vec_model")
