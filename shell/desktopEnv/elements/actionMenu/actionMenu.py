from tkinter import *
from extras import failsafe
import requests
import sys
from elements.actionMenu import appCalls

def drawMenu(uiWindow):
    def endSessionCallback():
        failsafe.failsafe(uiWindow)

    def aboutAppCallback(uiWindow):
        appCalls.aboutAppLaunch()
        uiWindow.attributes("-fullscreen", True)
        uiWindow.attributes("-zoomed", True)
    
    menuBackground = Canvas(uiWindow, width=uiWindow.winfo_screenwidth()/3, height=uiWindow.winfo_screenheight()/2)
    menuBackground.place(rely=0.04)
    if "apitest" in sys.argv:
        apiTest = requests.get("http://localhost:5000/")
        apiStatLabel = Label(uiWindow, text="System API Status: " + apiTest.text)
        apiStatLabel.place(relx=0.20, rely=0.5)

    endSessionButton = Button(uiWindow, text="End Session", command=endSessionCallback)
    endSessionButton.place(relx=0.1,rely=0.5)

    aboutButton = Button(uiWindow, text="About Servr Co OS", bg="#ffffff", width=20, command=appCalls.aboutAppLaunch)
    aboutButton.place(rely=0.1)

    def destroyMenu():
        if "apitest" in str(sys.argv):
            apiStatLabel.destroy()
        menuBackground.destroy()
        endSessionButton.destroy()
        aboutButton.destroy()
        destroyExitButton()

    exitMenuButton = Button(uiWindow, text="Exit Menu", command=destroyMenu)
    exitMenuButton.place(rely=0.5)

    def destroyExitButton():
        exitMenuButton.destroy()
