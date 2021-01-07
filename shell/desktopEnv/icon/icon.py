from tkinter import *

class iconInstance(object):
    def __init__(self, windowObject, iconLabel):
        self.windowObject = windowObject
        self.iconLabel = iconLabel
    "base class for an icon. iconImage must be a PNG."
    iconLabelElement = Label(windowObject, text=iconLabel)
    iconLabelElement.place(relx=0.5, rely=0.5)
    iconLabelElement.bind("<B1-Motion>", lambda event: iconLabelElement.place(x=event.x, y= event.y))

    