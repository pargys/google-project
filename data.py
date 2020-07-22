from collections import defaultdict
from auxiliary_functions import *

data_dict = defaultdict(set)
sources_dict = {}

with open("file.txt") as file:
    sentences_list = file.read().split("\n")


def init():

    for i in range(len(sentences_list)):
        for j in range(len(sentences_list[i])):
            for k in range(j+1, len(sentences_list[i])+1):
                data_dict[ignore_delimiters(sentences_list[i][k:j])].add(i)
                data_dict[ignore_delimiters(sentences_list[i][j:k])].add(i)

    data_dict.pop("")

    for i in range(len(sentences_list)):
        sources_dict[i] = "file.txt"

    for prefix in data_dict.keys():
        if len(data_dict[prefix]) > 5:
            sentences = [sentences_list[index] for index in data_dict[prefix]]
            sentences.sort()
            data_dict[prefix] = set([sentences_list.index(sentence) for sentence in sentences][:5])


def get_offset(str, substr):
    return str.find(substr)

def get_source(index):
    return sources_dict[index]