from data import *
from autocomplete_data import AutoCompleteData
from auxiliary_functions import *


def replace_character(prefix, on_top):
    results = []
    for i in range(len(prefix)-1, -1, -1):
        if len(results) != 0:
            break
        for letter in range(ord('a'), ord('z')+1):
            corrected_prefix = prefix[:i] + chr(letter) + prefix[i+1:]
            indexes = data_dict.get(corrected_prefix)
            if indexes:
                score = 5 - i if i < 5 else 1
                for j in indexes:
                    results.append({"sentence": j, "source": get_source(j), "offset": get_offset(sentences_list[j], corrected_prefix), "score": len(prefix)*2 - score})
                break
    return results[:on_top]


def fix_word(prefix, on_top):
    change_list = replace_character(prefix, on_top)
    # insert_list = insert_char()
    # delete_list = delete_char()
    return change_list


def get_best_k_completions(prefix):
    count_characters = len(prefix)
    prefix = ignore_delimiters(prefix)
    results_indexes = [index for index in data_dict[prefix]]
    completed_sentences = [sentences_list[index] for index in results_indexes]

    best_completion = []

    for i in range(len(results_indexes)):
        best_completion.append(AutoCompleteData(completed_sentences[i], get_source(sentences_list.index(completed_sentences[i])), get_offset(completed_sentences[i],prefix), count_characters*2))

    results_dict = fix_word(prefix, 5 - len(results_indexes))
    print(len(results_dict))
    for result in results_dict:
        best_completion.append(AutoCompleteData(sentences_list[result["sentence"]], result["source"], result["offset"], result["score"]))

    return best_completion

