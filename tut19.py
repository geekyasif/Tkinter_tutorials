from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("500x500")
root.title("List Box in tkinter")

# creating a function to add the value to the list box
def add():
    if str_val.get() != "":
        lbox.insert(ACTIVE, str_val.get())
        str_val.set("")
    else:
        tmsg.showinfo("Warning", "Value not be empty")

# creating a listbox
lbox = Listbox(root)
lbox.pack()

# adding direct value to the list box ( END :-  add the value to the last whereas ACTIVE add the item to the first)
lbox.insert(END, "First1 item of our listbox")
lbox.insert(END, "First item of our listbox")
lbox.insert(END, "First item of our listbox")


# creating a strig variable
str_val = StringVar()

# creating a input box for taking input from the user
input = Entry(root, textvariable=str_val).pack()

# creating a button
btn = Button(root, text="Add", command=add).pack()


root.mainloop()