# The Servr Co OS crash screen
# Basically a Windows BSOD, but less sad. :(

import os, sys
from tkinter import *
from time import sleep
totalClicks = 0

try:
    errCode = sys.argv[1]
    print(errCode)
except:
    errCode = "SCOS.ERR_UNDEFINED"
    print("Err code undefined.")

crashScreen = Tk()
crashScreen.title("SCOS Crash Screen")

w, h = crashScreen.winfo_screenwidth(), crashScreen.winfo_screenheight()

# Let's set this to full screen, as we well should.
crashScreen.attributes("-fullscreen", True)
crashScreen.attributes("-zoomed", True)

def killWindow(event):
    crashScreen.quit()

def activateEgg(event):
    global totalClicks
    if totalClicks < 5:
        totalClicks += 1
    else:
        eggLabel = Label(crashScreen, text="Spam clicking won't help you.")
        eggLabel.place(relx=0.5, rely=0.9, anchor="c")

crashScreen.bind_all("<F2>", func=killWindow) # Provides a kill switch in case you get stuck. Press F2 to escape!
crashScreen.bind_all("<Button-1>", func=activateEgg) # Triggers a fun easter egg.

bgColor = Canvas(crashScreen, bg="#00C000", width=w, height=h)
bgColor.place(relx=0.5, rely=0.5, anchor="c")

asciiSadFace = Label(crashScreen, text=".   .\n |\n/---\\", bg="#00C000", fg="#ffffff", font=("Arial", 40))
asciiSadFace.place(relx=0.25, rely=0.3, anchor="c")

noticeText = Label(crashScreen, text="Well, you broke it. Great job. We will fix it for you.\nJust be patient.", bg="#00C000", fg="#ffffff", font=("Arial", 40))
noticeText.place(relx=0.5, rely=0.5, anchor="c")

errorCause = Label(crashScreen, text="crashScreen.updateErrorCause()", bg="#00C000", fg="#ffffff", font=("Arial", 20)) # TODO: Make this error code change to be accurate.
errorCause.place(relx=0.5, rely=0.8, anchor="c")

def updateNoticeText(noticeMode): # We have 2 different messages for the crash screen, depending on your build type.
    if noticeMode == "release":
        noticeText.config(text="Servr Co OS has crashed. We're fixing it, then we'll get you back\nto your system.")
    else:
        noticeText.config(text="Well, you broke it. Great job. We will fix it for you.\nJust be patient.")

def updateErrorCause(cause):
    errorCause.config(text=cause)

# Now we populate the labels with info.

updateErrorCause(errCode)

# Okay, we're done initalizing everything. Now we wait for OSStartup to kill our process :--(.

try:
    updateNoticeText(sys.argv[2])
except:
    updateNoticeText("release")
crashScreen.mainloop()
