# from tkinter import *
# from tkinter.filedialog import askopenfilename
#
# root = Tk()
# root.title("Notepad Basic")
#
# def open_folder():
#     filepath = askopenfilename()
#     # txt_edit.delete("1.0", END)
#     with open(filepath, "r") as input_file:
#         text = input_file.read()
#         # txt_edit.insert(END, text)
#     root.title(f"Simple Text Editor - {filepath}")
#
# frame1 = Frame(master=root, width=80, bg="lightgray")
# frame1.pack(fill=Y, side= LEFT)
#
# open_btn = Button(frame1,command=open_folder,width=10,text="Open")
# open_btn.pack()
#
# save_btn = Button(frame1,width=10,text="Save")
# save_btn.pack()
#
# save_as_btn = Button(frame1,width=10,text="Save as")
# save_as_btn.pack()
#
# text_box = Text()
# text_box.pack()
#
#
# root.mainloop()
class Circle:

    def __init__(self,radius):
        self.radius = radius

    def print_area(self):
        area =  3.14*self.radius*self.radius
        print(area)
obj1 = Circle(3)
obj1.print_area()