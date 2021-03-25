from tkinter import *

root = Tk()
root.title("Buttons in Tkinter")
root.geometry("300x300")


def hello():
    greet = "Hello World"
    print(greet)



f =Frame(root, bg="white")

# command is use to do work on click on the button
btn = Button(f, fg="red", text="Submit Now",command=hello)
btn.pack()

f.pack()


root.mainloop()