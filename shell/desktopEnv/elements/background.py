from tkinter import *
from PIL import ImageTk, Image
import sys

class backgroundElements:
    def drawBackground(uiWindow):
        if "dbg" in str(sys.argv):
            print("Loading Desktop Background")
        background_image = PhotoImage(file="./rsrc/img/bgs/default.png")
        background_image_container = Label(uiWindow, image=background_image)
        background_image_container.place(x=0, y=0, relwidth=1, relheight=1)
        background_image_container.image = background_image