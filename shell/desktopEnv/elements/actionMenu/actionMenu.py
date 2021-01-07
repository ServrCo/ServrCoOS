from tkinter import *
from extras import failsafe
import requests

apiTest = requests.get("http://localhost:5000/")

def drawMenu(uiWindow):
    def endSessionCallback():
        failsafe.failsafe(uiWindow)
    
    menuBackground = Canvas(uiWindow, width=uiWindow.winfo_screenwidth()/3, height=uiWindow.winfo_screenheight()/2)
    menuBackground.place(rely=0.04)

    apiStatLabel = Label(uiWindow, text="System API Status: " + apiTest.text)
    apiStatLabel.place(relx=0.20, rely=0.5)

    endSessionButton = Button(uiWindow, text="End Session", command=endSessionCallback)
    endSessionButton.place(relx=0.1,rely=0.5)

    def destroyMenu():
        menuBackground.destroy()
        endSessionButton.destroy()
        apiStatLabel.destroy()
        destroyExitButton()

    exitMenuButton = Button(uiWindow, text="Exit Menu", command=destroyMenu)
    exitMenuButton.place(rely=0.5)

    def destroyExitButton():
        exitMenuButton.destroy()
