# coding=utf-8

import logging
from Word2Vec import load_model

logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)


def analyse(model_name):
    model = load_model(model_name)
    result = model.similarity(u'高兴', u'开心')
    return result
