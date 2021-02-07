# The Servr Co OS New LogonUI
# Rewritten because Andrew was unhappy with how the original turned out.
# Run this script with the dbg flag to get extra debug features, including a kill switch in case you happen to get stuck!

from tkinter import *
import sys, os, hashlib

isDbgMode = "dbg" in sys.argv

root = Tk()
root.title("root")

w, h = root.winfo_screenwidth(), root.winfo_screenheight() # Gets screen height and width.

root.geometry("%dx%d+0+0" % (w, h)) # This block of code sets root to fullscreen and as top priority.
root.attributes('-topmost', 1)
root.attributes('-type', 'splash')
root.focus_force()

# This is where the callbacks live. Put them all here so they're accessible by all the code below!
def logonUIKillCallback(event):
    root.destroy()

def checkPwd():
    if isDbgMode:
        print(passwdEntry.get())
    
    try:
        pwdFile = open("pwdFile")
        pwd512Hash = pwdFile.readlines()[0].lower()
    except OSError:
        pwd512Hash = "10983B6BBC12BA90992C5672838ADCAC253E821EE4D8E1B622E02B151E04C3F7520A26B60E456E2AFEEBC500817195C37E1776DAD827FD6C2078B85611A66257".lower() # Set the password to ServrCoOS if all else fails.

    hashed = hashlib.sha512(passwdEntry.get().encode())

    if hashed.hexdigest() == pwd512Hash:
        if isDbgMode:
            print("Correct!")
        logonUIKillCallback([])
    else:
        incorrectLabel = Label(root, text="Incorrect.") # Make fun of the user for entering a wrong password.
        incorrectLabel.place(relx=0.5, rely=0.7, anchor="c")
        if isDbgMode:
            print(hashed.hexdigest(), "Correct hash:" + pwd512Hash)
    
def enterKeyCheckPwd(event):
    checkPwd()

if isDbgMode:
    root.bind_all("<F2>", func=logonUIKillCallback) # This is a kill switch. Press F2 if you get stuck on this window and need to exit.

root.bind_all("<Return>", func=enterKeyCheckPwd)

# NOW we can start placing stuff in the window.

bgColor = Canvas(root, width=w, height=h, bg="#4287f5") # Place a nice blue background behind all other elements.
bgColor.place(anchor="c", relx=0.5, rely=0.5)

SCOSText = Label(root, text="Servr Co OS", bg="#4287f5", fg="#ffffff", font=("Arial", 40)) # Place the text "Servr Co OS" at the top of the window.
SCOSText.place(anchor="n", relx=0.5)

welcomeText = Label(root, text="Welcome to Servr Co OS! Please enter your password below!", bg="#4287f5", fg="#ffffff", font=("Ubuntu", 20))
welcomeText.place(anchor="c", relx=0.5, rely=0.45)

passwdEntry = Entry(root, show="*", width=35)
passwdEntry.place(anchor="c", relx=0.44, rely=0.5)

submitBtn = Button(root, text="Submit", command=checkPwd)
submitBtn.place(anchor="c", relx=0.56, rely=0.5)

root.mainloop()
