from tkinter import *


root = Tk()
root.title("Geeky Asif Tutorials")
root.geometry("400x400")
# Frame :- Frame is like div in frame we add our widgets

f1 = Frame(root,bg="white", borderwidth=5, relief=SUNKEN)
l1 = Label(f1,text="Project Tkinter",font=30)
l1.pack()
f1.pack()




root.mainloop()