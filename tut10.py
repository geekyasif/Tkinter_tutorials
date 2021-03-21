from tkinter import *

root = Tk()
root.title("Checkbox In Tkinter")
root.geometry("600x300")

def getvals():
    list = [nameVal.get(),phoneVal.get(),genderVal.get(),paymentModeVal.get(),mealVal.get()]
    print(list)
    with open("details.txt",'a') as f:
        f.write(f"{list}\n")


    # nameVal.set("")
    # phoneVal.set("")
    # genderVal.set("")
    # paymentModeVal.set("")
    # mealVal.set("")




heading = Label(root, text="Welcome to Asif Travels",font="comicsansms 20 bold")
heading.grid(row=0,column=1,padx=20,pady=20)

Name = Label(root, text="Name")
Name.grid(row=1,column=0, padx=20,pady=5)

Phone = Label(root, text="Phone")
Phone.grid(row=2,column=0, padx=20,pady=5)

Gender = Label(root, text="Gender")
Gender.grid(row=3,column=0, padx=20,pady=5)

PaymentMode = Label(root, text="PaymentMode")
PaymentMode.grid(row=4,column=0, padx=20,pady=5)

nameVal = StringVar()
phoneVal = StringVar()
genderVal = StringVar()
paymentModeVal = StringVar()
mealVal = IntVar()

nameEntry = Entry(root,textvariable=nameVal)
nameEntry.grid(row=1,column=1, padx=10,pady=5)

phoneVal = Entry(root,textvariable=phoneVal)
phoneVal.grid(row=2,column=1, padx=10,pady=5)

genderVal = Entry(root,textvariable=genderVal)
genderVal.grid(row=3,column=1, padx=10,pady=5)

paymentModeVal = Entry(root,textvariable=paymentModeVal)
paymentModeVal.grid(row=4,column=1, padx=10,pady=5)

mealservice = Checkbutton(text="Want meal with your journey ?", variable=mealVal)
mealservice.grid(row=5,column=1, padx=10,pady=5)

Button(text="Sumbit to Geeky Travels", command=getvals, fg="white", background="green").grid(row=7,column=1,pady=10)




root.mainloop()