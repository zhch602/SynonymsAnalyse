# coding=utf-8

from Analyse import get_max_similarity_word
from Word2Vec import load_model

if __name__ == "__main__":

    words = ['狗', '犬', '金毛狗', '金毛犬']

    model = load_model('word2vec_model')

    print get_max_similarity_word(words, model)
