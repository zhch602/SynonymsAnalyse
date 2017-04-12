# coding=utf-8

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def get_max_similarity_word(words, model):
    length = len(words)
    sum_list = []
    
    for i in range(length):
        word_sum = 0
        for j in range(length):
            if i != j:
                if words[i] in words[j]:
                    pass
                elif words[j] in words[i]:
                    word_sum += 1
                elif words[i] == words[j]:
                    word_sum += 1
                else:
                    word_sum += model.similarity(unicode(words[i], "utf-8"), unicode(words[j], "utf-8"))
        sum_list.append((words[i], word_sum))

    sum_list.sort(key=lambda a: a[1], reverse=True)

    return sum_list[0][0]
