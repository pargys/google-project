from autocomplete import *
from data import sentences_list, init
from autocomplete_data import AutoCompleteData

print(sentences_list)
input_ = input()

def start_app():

    while True:
        print('please start search:')

        while input_[len(input_)-1] != '#':
            print("Here are the results:")
            best_completion = get_best_k_completions(input_)
            for sentence in best_completion:
                print(sentence.get_completed_sentence())
            print(input_, end="")
            input_ = input_ + input()

start_app()
