from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()

root.title("scrollbar in tkinter")
root.geometry("500x500")

# for connecting scrollbar to a widget
# 1. widget(yscrollcommand = scrollbar.set)
# 2. scrollbar.config(command=widget.yview)

def add():
    if str_val.get() != "":
        lbox.insert(ACTIVE, str_val.get())
        str_val.set("")
    else:
        tmsg.showinfo("Warning", "Value not be empty")

# creating scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)


# creating list box
lbox = Listbox(root, yscrollcommand= scrollbar.set)
lbox.pack()

#connecting the listbox with scrollbar
scrollbar.config(command=lbox.yview)



str_val = StringVar()
input = Entry(root, textvariable=str_val).pack()
btn = Button(root, text="Add", command=add).pack()


root.mainloop()