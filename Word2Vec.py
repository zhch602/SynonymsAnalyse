# coding=utf-8

from gensim.models import word2vec
from gensim.models import Word2Vec
import logging

logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)


def build_model(input_file_name):
    sentences = word2vec.LineSentence(input_file_name)
    model = word2vec.Word2Vec(sentences, size=400, window=5, min_count=5, workers=4)
    return model


def save_model(model, model_name):
    model.save(model_name)


def load_model(model_name):
    model = Word2Vec.load(model_name)
    return model
