from autocomplete import get_best_k_completions
from data import init
from tkinter import Tk, Menu, END, Entry, Button, Listbox

init()
root = Tk() 
root.title('Auto Complete') 

def search():
    input = entry.get()
    list.delete(0, END)
    if input != "":
        if input[-1] == '#':
            entry.delete(0, END)

        else:
            best_completion = get_best_k_completions(input)
            i = 1
            if best_completion:
                for sentence in best_completion:
                    list.insert(END, f'{i}. {sentence.get_completed_sentence()}')

                    list.insert(END, f'source: {sentence.get_source_text()}  , offset: {sentence.get_offset()}  , score: {sentence.get_score()}\n')
                    list.insert(END, '\n\n')
                    i += 1
            else:
                list.insert(END, 'no results!')


entry = Entry(width=70)
entry.grid(row=0, column=0)

button_search = Button(root, text='Search', width=5, command=search)
button_search.grid(row=0, column=1)

list = Listbox(root, width=70)
list.grid(row=1, column=0)

root.mainloop()
