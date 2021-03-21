from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("GeekyNews - Daily News Paper")
root.geometry('1000x1000')
title = Label(text="GeekyNews - Today,s Top HeadLines ",fg="blue",font=30,background="Lightgray",padx=20, pady=20)
title.pack(fill=X)

texts = []
with open('1.txt','r') as f:
    text1 = f.read()
    texts.append(text1)

#opeing the image from the file
image = Image.open("logo.png")

#resziing the image
imag = image.resize((250,250))

#making the image callabe and storing into an variabel
img = ImageTk.PhotoImage(imag)


# creating a div (called Frame ) and adding text and img into label and setting all the decoration
article_1 = Frame(root, width=600, height=600,background="white",padx=20,pady=20)

# label for text
Label(article_1, text=texts[0],background="white",padx=10).pack(side="left")

# label for image
Label(article_1, image=img).pack(side="right")

#closing or packing the div(Frame)
article_1.pack(anchor="w",pady=10,padx=10)


# creating a div (called Frame ) and adding text and img into label and setting all the decoration
article_2 = Frame(root, width=600, height=600)

# label for text
Label(article_2, text=texts[0]).pack(side="right")

# label for image
Label(article_2, image=img).pack(side="left")

#closing or packing the div(Frame)
article_2.pack(anchor="w",pady=10,padx=10)


# creating a div (called Frame ) and adding text and img into label and setting all the decoration
article_3 = Frame(root, width=600, height=600,background="white")

# label for text
Label(article_3, text=texts[0],background="white").pack(side="left")

# label for image
Label(article_3, image=img).pack(side="right")

#closing or packing the div(Frame)
article_3.pack(anchor="w",pady=10,padx=10)


# for i in range(0,2):
#     with open(f"{i+1}.txt") as f:
#         text = f.read()
#         texts = [x for x in text]
#
#     image = Image.open(f"{i+1}.png")
    # resizing the images
    # TODO: rezing the image
    # photos = [x for x in image]

root.mainloop()