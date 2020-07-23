from data import *
from autocomplete_data import AutoCompleteData
from auxiliary_functions import *


def replace_character(prefix, on_top, results_indexes):
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
                    if j not in results_indexes:
                        results.append({"sentence": j, "source": get_source(j), "offset": get_offset(j), "score": len(prefix)*2 - score})
                        results_indexes.append(j)
                break
    return results[:on_top]


def delete_char(prefix, on_top, results_indexes):
    results = []
    for i in range(len(prefix)-1, -1, -1):
        if len(results) != 0:
            break
        for letter in range(ord('a'), ord('z')+1):
            corrected_prefix = prefix[:i] + chr(letter) + prefix[i:]
            indexes = data_dict.get(corrected_prefix)
            if indexes:
                score = 10 - 2*i if i < 4 else 2
                for j in indexes:
                    if j not in results_indexes:
                        results.append({"sentence": j, "source": get_source(j), "offset": get_offset(j), "score": len(prefix)*2 - score})
                        results_indexes.append(j)
                break
    return results[:on_top]


def add_char(prefix, on_top, results_indexes):
    results = []
    for i in range(len(prefix)-1, -1, -1):
        corrected_prefix = prefix[:i] + prefix[i+1:]
        indexes = data_dict.get(corrected_prefix)
        if indexes:
            score = 10 - 2*i if i < 4 else 2
            for j in indexes:
                if j not in results_indexes:
                    results.append({"sentence": j, "source": get_source(j), "offset": get_offset(j), "score": len(prefix)*2 - score})
                    results_indexes.append(j)
            break
    return results[:on_top]


def fix_word(prefix, on_top, results_indexes):
    temp_results_indexes = [index for index in results_indexes]
    change_list = replace_character(prefix, on_top, temp_results_indexes)
    insert_list = add_char(prefix, on_top, temp_results_indexes)
    delete_list = delete_char(prefix, on_top, temp_results_indexes)
    correction_list = sorted(change_list + insert_list + delete_list, key=lambda k: k["score"], reverse=True)
    correction_list = correction_list[:on_top]
    return correction_list


def get_best_k_completions(prefix):
    count_characters = len(prefix)
    prefix = ignore_delimiters(prefix)
    results_indexes = list(data_dict[prefix])
    completed_sentences = [get_sentences_list()[index] for index in results_indexes]

    best_completion = []

    for i in range(len(results_indexes)):
        best_completion.append(AutoCompleteData(completed_sentences[i], get_source(get_sentences_list().index(completed_sentences[i])), get_offset(results_indexes[i]), count_characters*2))

    results_dict = fix_word(prefix, 5 - len(results_indexes), results_indexes)
    for result in results_dict:
        best_completion.append(AutoCompleteData(get_sentences_list()[result["sentence"]], result["source"], result["offset"], result["score"]))

    return best_completion

