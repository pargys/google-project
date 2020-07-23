from collections import defaultdict
from auxiliary_functions import *

sentences_list = []
data_dict = defaultdict(set)
sources_dict = {0: "file1.txt", 1: "file2.txt"}
offset_dict = {}
data_sources_dict = {}


def read_from_files():
    global sources_dict
    global offset_dict
    global data_sources_dict

    for key, value in sources_dict.items():
        with open(value) as the_file:
            temp_sentences_list = the_file.read().split("\n")
        for i, str in enumerate(temp_sentences_list):
            data_sources_dict[len(sentences_list)] = key
            offset_dict[len(sentences_list)] = i
            sentences_list.append(str)


def init():
    read_from_files()

    for i in range(len(sentences_list)):
        for j in range(len(sentences_list[i])):
            for k in range(j+1, len(sentences_list[i])+1):
                data_dict[ignore_delimiters(sentences_list[i][k:j])].add(i)
                data_dict[ignore_delimiters(sentences_list[i][j:k])].add(i)

    data_dict.pop("")

    for prefix in data_dict.keys():
        if len(data_dict[prefix]) > 5:
            sentences = [sentences_list[index] for index in data_dict[prefix]]
            sentences.sort()
            data_dict[prefix] = set([sentences_list.index(sentence) for sentence in sentences][:5])


def get_sentences_list():
    return sentences_list


def get_offset(index):
    return offset_dict[index]


def get_source(index):
    return sources_dict[data_sources_dict[index]]