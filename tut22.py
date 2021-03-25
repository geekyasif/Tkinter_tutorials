from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("Tkinter using Classes and objects")

    def click(self):
        self.stringVar.set("Loading...")
        self.label.update()
        import time
        time.sleep(2)
        self.stringVar.set("Ready")

    def btn(self):
        Button(text="Click here", command=self.click).pack()


    def statusBar(self):
        self.stringVar= StringVar()
        self.stringVar.set("Ready")
        self.label = Label(textvariable=self.stringVar, relief=SUNKEN,anchor="w")
        self.label.pack(side=BOTTOM, fill=X)


if __name__ == '__main__':
    win = GUI()
    win.btn()
    win.statusBar()
    win.mainloop()
