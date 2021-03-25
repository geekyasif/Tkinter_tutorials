from tkinter import *

root = Tk()

#widget and attributes
#label, Geometry, Maxsize and Minsize


# geomatery is a function Here we set (width x height) for window
root.geometry("400x400")

# setting max or min size it takes(width, height)

root.minsize(300,200) #setting minimum size
root.maxsize(800,700) #setting max size

#label is a widget that user can not interact
name = Label(text="Hello Mohammad Asif")
name.pack()



root.mainloop() #eventLoop