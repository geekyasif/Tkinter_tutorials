from tkinter import *

root = Tk()

def get_vals():
    width = widthVar.get()
    height = heightVar.get()
    print(width,height)
    root.geometry(f"{width}x{height}")
    widthVar.set(" ")
    heightVar.set(" ")



widthlabel = Label(root, text="Enter window width ")
widthlabel.grid(row=0,column=0)

hiegthlabel = Label(root, text="Enter window height ")
hiegthlabel.grid(row=1,column=0)

widthVar = IntVar()
heightVar = IntVar()

widthEntry = Entry(root, textvariable=widthVar)
widthEntry.grid(row=0,column=1)

heightEntry = Entry(root, textvariable=heightVar)
heightEntry.grid(row=1,column=1)

btn = Button(root, text="Submit", command=get_vals)
btn.grid(row=2,column=1)




root.mainloop()