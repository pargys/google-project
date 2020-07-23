from autocomplete import *
from data import init

init()


def start_app():
    while True:
        print('please start search:')
        input_ = input()
        if input_ != "":
            while input_[-1] != '#':
                best_completion = get_best_k_completions(input_)
                if best_completion:
                    for sentence in best_completion:
                        print(f"{sentence.get_completed_sentence()}:\n"
                              f"source: {sentence.get_source_text()}, offset: {sentence.get_offset()}, score: {sentence.get_score()}\n")
                    print(input_, end="")

                else:
                    print('no results found!')
                    break

                input_ = input_ + input()


start_app()
