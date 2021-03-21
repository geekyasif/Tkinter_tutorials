from tkinter import *

root = Tk()
root.title("Radio buttons")
root.geometry("400x400")
def ans():
    print(var.get())
Label(root, text="What is python ?").pack()
var = StringVar()
radio = Radiobutton(root, text="Programming langauege", variable=var, value="PRogramming language").pack()
radio = Radiobutton(root, text="Scripting language", variable=var, value="sc").pack()
radio = Radiobutton(root, text="Both", variable=var, value="both").pack()


btn = Button(root, text="Submit answer", command=ans)
btn.pack()
root.mainloop()