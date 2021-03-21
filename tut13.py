from tkinter import *

root = Tk()
root.title("Even Listener in Python")
root.geometry("400x400")

# we pass event in function without its produce and error
def asif(event):

    # we can caputre events with x and y axis
    print(f"Hello geeks at {event.x} {event.y}")


# creating a button
btn_widget = Button(root, text="Click here")
btn_widget.pack()

# Binding event with buttons and <Button-1 is an event it show that one click on button triggered>
btn_widget.bind('<Button-1>', asif)




root.mainloop()