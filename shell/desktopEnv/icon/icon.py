from tkinter import *
from PIL import ImageTk, Image

def make_draggable(widget):
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)

def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

def on_drag_motion(event):
    widget = event.widget
    # x = widget.winfo_x() - widget._drag_start_x + event.x
    # y = widget.winfo_y() - widget._drag_start_y + event.y
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)

def drawNewIcon(window, label):
    iconLabelElement = Label(window, text=label)
    iconLabelElement.place(x=640, y=360, anchor="c")
    #iconLabelElement.bind("<B1-Motion>", lambda event: iconLabelElement.place(x=event.x, y= event.y, anchor="c"))
    make_draggable(iconLabelElement)
