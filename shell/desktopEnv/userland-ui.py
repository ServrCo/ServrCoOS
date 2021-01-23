# This is the main Python file for the SCOS-Userland section of the OS.

from tkinter import *
from extras import failsafe
from elements import toolbar
from elements import background
from help import startHelp
from icon import icon
import sys
#from icon import icon

uiWindow = Tk()
uiWindow.title("Servr Co OS Userland")

class callbacks: # This is a class for event and button callbacks.
    def failsafeCallback(event):
        failsafe.failsafe(uiWindow)
    def helpCallback(event):
        startHelp.launchHelp()

# Load in elements from external modules

background.backgroundElements.drawBackground(uiWindow)
toolbar.toolbarElements.createToolbar(uiWindow)
#testIcon = iconInstance(uiWindow, "test text")

# Initalize and load everything
uiWindow.bind_all("<F1>", callbacks.failsafeCallback)
uiWindow.bind_all("<F2>", callbacks.helpCallback)
uiWindow.attributes("-fullscreen", True)
uiWindow.attributes("-zoomed", True)

icon.drawNewIcon(uiWindow, "hi")

if "dbg" in sys.argv: # Adds a watermark to the screen if the shell is launched in debug mode.
    Label(uiWindow, text="Servr Co OS Debug version.\nBe careful.").place(relx=0.85, rely=0.04)

uiWindow.mainloop()
