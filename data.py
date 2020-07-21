from collections import defaultdict

with open("file.txt") as file:
    sentences_list = file.read().split("\n")

data_dict = defaultdict(set)

for i in range(len(sentences_list)):
    for j in range(len(sentences_list[i])):
        for k in range(j+1, len(sentences_list[i])+1):
            data_dict[sentences_list[i][k:j]].add(i)
            data_dict[sentences_list[i][j:k]].add(i)

data_dict.pop(" ")
