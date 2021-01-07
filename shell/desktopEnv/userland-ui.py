# This is the main Python file for the SCOS-Userland section of the OS.
# The code imports each module seperately, but due to Object Oriented Programming weirdness, I can't do a Wildcard import.

from tkinter import *
from extras import failsafe
from elements import toolbar
from elements import background
from help import startHelp
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
uiWindow.mainloop()