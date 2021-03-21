from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()

root.title("Alert and message box")
root.geometry("400x400")

def rate_us():
    value = tmsg.askquestion("Rate Us","Go to play store and rate us or app")
    if value == "yes":
        msg = "great"
    else:
        msg = "we are soory"

    tmsg.showinfo("Experience", msg)


def help():
    # print("help")
    tmsg.showinfo("Help","Check our website for more info !")


submenu = Menu(root)
helpmenu  = Menu(submenu, tearoff=0)
helpmenu.add_command(label="Help", command=help)
helpmenu.add_command(label="Rate us", command=rate_us)
root.config(menu=submenu)
submenu.add_cascade(label="Help", menu=helpmenu)

root.mainloop()