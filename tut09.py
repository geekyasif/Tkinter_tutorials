from tkinter import *

root = Tk()
root.title("Grid in Tkinter")
root.geometry("400x400")
# Label(root, text="Grid in Tkinter", font=20).pack()

def login():
    print(userValue.get())
    print(passwordValue.get())
    userValue.set("")
    passwordValue.set("")


user = Label(root, text="Username")
password = Label(root, text="Password")
user.grid(row=0,column=0)
password.grid(row=1,column=0)

#entry widget
#classes in tkinter
# boolean - BooleanVar
#double var - DoubleVar
#InterVar - IntVar
#StringVar - StringVar

#creating a variabel
userValue = StringVar()
passwordValue = StringVar()

# creating a Entry for input and seting the variabel
userEntry = Entry(root, textvariable = userValue)
passEntry = Entry(root, textvariable = passwordValue)

#packing the Entry with grid
userEntry.grid(row=0,column=1)
passEntry.grid(row=1,column=1)

# creating a buttton for submit and calling a function that print the value
Button(text="Submit",command=login).grid()


root.mainloop()