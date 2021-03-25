from tkinter import *

root = Tk()
root.title("Status bar in tkinter")
root.geometry("400x400")

def upload():
    statusVar.set("busy....")
    statusLabel.update()
    import time
    time.sleep(2)
    statusVar.set("Ready..")


statusVar = StringVar()
statusVar.set("Ready")
statusLabel = Label(root, textvariable=statusVar, relief=SUNKEN,anchor='w')
statusLabel.pack(side=BOTTOM, fill=X)

btn = Button(root, text="Upload",command=upload)
btn.pack()
root.mainloop()
