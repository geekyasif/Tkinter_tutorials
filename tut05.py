from tkinter import *
import os

#attributes of label and pack

root = Tk()
path = os.getcwd()
# print(path)
root.title("tut5" + " " + path)
root.geometry("400x223")

# important label options
# text - add the text
# bd - background
# fg - foreground
# font - sets the font
# 1 font=("comicsansms",19, "bold")
# 2 font=("comicsansms 19 bold")
# padx = padding in x
# pady = padding in y
# relief - border styling - SUNKEN - RAISED, GROOVE, RIDGE

# title_label = Label(text = '''
# Python tutorial provides basic and advanced concepts of Python. Our Python tutorial is designed for beginners and professionals.
# Python is a simple, general purpose, high level, and object-oriented programming language.
# Python is an interpreted scripting language also. Guido Van Rossum is known as the founder of Python programming.
# ''', bg="lightgray", fg="blue", padx=23, pady=29, font="comicsansms 9 bold", borderwidth=3, relief=GROOVE)


title_label = Label(text="Ready",background="Lightgray", fg="red")
# important pack option
# anchor = north-west (nw)
# side - TOP, BOTTOM, RIGHT, LEFT
# fill = X, Y
# padx
# pady
title_label.pack(side=BOTTOM, fill=X)



root.mainloop()
