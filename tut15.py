from tkinter import *

# menu and sub menu in tkinter

root = Tk()
root.title('menu and sub menu in tkinter')
root.geometry("400x400")

def myfunc():
    pass

# it is use to create non dropdown-menu section add on the top of the window
# myMenu = Menu(root)
# myMenu.add_command(label="File",command=myfunc)
# myMenu.add_command(label="Exit", command=quit)
# root.config(menu=myMenu)


# it is use to create a dropwdown-menu
submenu = Menu(root, tearoff=False)

# creating the sub menu
file = Menu(submenu,tearoff=0)
file.add_command(label="New", command=myfunc)
file.add_command(label="New Window", command=myfunc)
file.add_command(label="Open..", command=myfunc)
file.add_command(label="Save", command=myfunc)
file.add_command(label="Save as..", command=myfunc)
file.add_separator()
file.add_command(label="Add Setup..", command=myfunc)
file.add_command(label="Print..", command=myfunc)
file.add_separator()
file.add_command(label="Exit", command=quit)



root.config(menu=submenu)
submenu.add_cascade(label="File", menu= file)

edit = Menu(submenu,tearoff=0)
edit.add_command(label="Undo", command=myfunc)
edit.add_separator()
edit.add_command(label="Copy", command=myfunc)
edit.add_command(label="Cut", command=myfunc)
edit.add_command(label="Paste", command=myfunc)
edit.add_command(label="Delete", command=myfunc)
edit.add_separator()
edit.add_command(label="Find", command=myfunc)
edit.add_command(label="Find Next", command=myfunc)
edit.add_separator()
edit.add_command(label="Select All", command=quit)

root.config(menu=submenu)
submenu.add_cascade(label="Edit", menu= edit)



root.mainloop()