# Contains the classes and functions to draw the SCOS Userland Toolbar

from tkinter import *
from elements.actionMenu import actionMenu

class toolbarElements:
    isActionMenuDrawn = 0
    def createToolbar(uiWindow): # Called by the userland-ui file. uiWindow is the TKinter window object in userland-ui.
        def actionButtonCallback():
            actionMenu.drawMenu(uiWindow)

        Canvas(uiWindow, width=uiWindow.winfo_screenwidth(), height=int(uiWindow.winfo_screenheight()) - uiWindow.winfo_screenheight()/1.04).place(anchor="nw") # Make and load a white rectangle at the top of the window for the toolbar.
        #TODO: Add the ability to enable Dark Theme, which makes the bar black when active. This could be a simple setting once the Settings app is made.
        
        actionButton = Button(uiWindow, text="Action Button", command=actionButtonCallback) # Make the Action Button
        timeClockLabel = Label(uiWindow, text="Cl:oc:k.") # Make the clock label. 

        timeClockLabel.place(relx=1, rely=0.01, anchor="ne") # Load the clock label
        actionButton.grid(row=0, column=0) # Load the Action Button