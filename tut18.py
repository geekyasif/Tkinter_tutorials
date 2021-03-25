from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title("Slider in TKinter")
root.geometry("400x400")

# creating a function to show message box
def get_doller():
    tmsg.showinfo("Amount Credited", f"We have credited {slider.get()} dollers in your account.")

# creating a lebel
Label(root, text="How many doller you want ? ").pack()

# creating slider
slider = Scale(root, from_=0, to=100, orient=HORIZONTAL)
slider.pack()

# creating button
btn = Button(root, text="Get Dollers", command=get_doller)
btn.pack()


root.mainloop()