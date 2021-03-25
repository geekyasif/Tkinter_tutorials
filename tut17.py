from tkinter import *

root = Tk()
root.title("Radio buttons")
root.geometry("400x400")
def ans():
    print(var.get())

Label(root, text="What is python ?").pack()

var = StringVar()
radio1 = Radiobutton(root, text="Programming langauege", variable=var, value="Programming language").pack()
radio2 = Radiobutton(root, text="Scripting language", variable=var, value="sc").pack()
radio3 = Radiobutton(root, text="Both", variable=var, value="both").pack()


btn = Button(root, text="Submit answer", command=ans)
btn.pack()
root.mainloop()