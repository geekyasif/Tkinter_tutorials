from tkinter import *

# creating a object of Tk it created a window root for basic funcationality
root = Tk()  #staring point

# setting the title of the gui
root.title("Starting Tkinter Tutorials")

# setting window size
root.geometry("400x400")

# setting icon with .ico file
# root.wm_iconbitmap("1.ico")

# setting background image
root.configure(background="red")

# creating button to close the gui
Button(text="Click here to close the app", command=root.destroy).pack()


# gui logic here
# all the logic are write here


root.mainloop() #ending point
