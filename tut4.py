from tkinter import *
from PIL import Image, ImageTk
import os

root = Tk()


# root.geometry("400x400")

#dispalying image in this tutorial
# image is a label

#setting image by default only png image can be set in tkinter not jpg for jpg use pillow library
# pic = PhotoImage(file="img.png")
# image=image.resize(width, height )

# creating a label for image
# pic_label = Label(image=pic.resize(""))

#packing the image label
# pic_label.pack()
os.chdir("D:\DCIM\CAMERA")
i = 0
j= 0
for pc_pics in os.listdir():
    print(pc_pics)
    ext = os.path.splitext(pc_pics)
    if ext[1] == ".jpg":
        img = Image.open(pc_pics)
        # img.load()
        # img = img.resize((100,100))
        pic_jpg = ImageTk.PhotoImage(img)
        pc_pics_label = Label(image=pic_jpg)
        pc_pics_label.pack()

# for taking jpg image we have to import pillow library
# example :-
# img = Image.open()
# pic = ImageTk.PhotoImage(img)
# pic_label = Label(image=pic)
# pic.label()



root.mainloop()



