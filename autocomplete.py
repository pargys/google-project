from data import data_dict
from autocomplete_data import AutoCompleteData
from auxiliary_functions import *


def replace_character(prefix, best_completion):
    equal = -1
    results_indexes = []
    for i in range(len(prefix)-1, -1, -1):
        if(-1 == equal):
            for letter in range(ord('a'), ord('z')):
                corrected_prefix = prefix[:i]+letter+prefix[i+1:]
                indexes = data_dict.get(corrected_prefix)
                if indexes:
                    equal=i
                    results_indexes = [index for index in indexes]
                    break
    corrected_prefix = prefix[:i] + letter + prefix[i + 1:]
    if equal > 0:
        completed_sentences = [data_dict[index] for index in results_indexes]
        completed_sentences.sort()

    score = 5 - equal if equal < 5 else 1
    on_top = 5 - len(best_completion)
    num_of_elements = on_top if len(results_indexes) > on_top else len(results_indexes)
    for i in range(num_of_elements):
        best_completion.append(AutoCompleteData(data_dict[results_indexes[i]], "", get_offset((results_indexes[i], corrected_prefix)), len(prefix) * 2 - score))


def get_best_k_completions(prefix):
    count_characters = len(prefix)
    prefix = ignore_delimiters(prefix)
    results_indexes = [index for index in data_dict[prefix]]
    completed_sentences = [data_dict[index] for index in results_indexes]

    if len(results_indexes) > 5:
        completed_sentences.sort()

    results_len = 5 if len(results_indexes) > 5 else len(results_indexes)
    best_completion = []

    # -----I did not finish
    for i in range(results_len):
        best_completion.append(AutoCompleteData(data_dict[completed_sentences[i]], get_offset(completed_sentences[i], prefix), count_characters*2))

    if len(results_indexes) < 5:
        results_indexes.append(replace_character(prefix, best_completion))

    if len(results_indexes) < 5:
        # מחיקה של תוים
        pass

