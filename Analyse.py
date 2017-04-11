# coding=utf-8
import gensim
import logging

logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)
model = gensim.models.Word2Vec.load("word2vec_model")

result = model.similarity(u'高兴', u'开心')
print result
