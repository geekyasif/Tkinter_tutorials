from tkinter import *

root = Tk()

root.title("Canvas in Tkinter")

canvas_width = 500
canvas_height = 500
root.geometry(f"{canvas_width}x{canvas_height}")

canvas_widget = Canvas(root, width=canvas_width, height=canvas_height)
canvas_widget.pack()

# the line goes from x1,y1, to x2,y2
canvas_widget.create_line(0,110,110,0)  

# creating a rectangle and specify the parameters in this order - coors of the top left
# coor of bottom right
# canvas_widget.create_rectangle(3,5,400,200, fill="red")

# canvas_widget.create_text(300,400, text="Python")

# creating a oval shape with canvas widget
# canvas_widget.create_oval(10,10,300,400)

canvas_widget.create_polygon(10,100,10,200)

canvas_widget.create_arc(1,2,2,3)
root.mainloop()