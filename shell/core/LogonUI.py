import hashlib
from tkinter import *
from core import variables
from time import sleep
from core import TempVariables
import os
import sys

if "dbg" in str(sys.argv): # This code prevents unneeded console logs unless we want them.
    print("Opening LogonUI")

LogonUI = Tk()
LogonUI.title("Logon UI")

w, h = LogonUI.winfo_screenwidth(), LogonUI.winfo_screenheight()

LogonUI.geometry("%dx%d+0+0" % (w, h)) # This block of code sets LogonUI to fullscreen and as top priority.
LogonUI.attributes('-topmost', 1)
LogonUI.attributes('-type', 'splash')
LogonUI.focus_force()

PasswordBoxLabel = Label(LogonUI, text="Yes, this is where you enter your password. You can TOTALLY trust this box!")
EnterPassword = Entry(LogonUI, show="*", width=25)
PressEnterLabel = Label(LogonUI, text="Key in your password and press enter!")

PasswordBoxLabel.place(relx=0.5, rely=0.46, anchor="c")
EnterPassword.place(relx=0.5, rely=0.5, anchor="c")
PressEnterLabel.place(relx=0.5, rely=0.54, anchor="c")

def RetreivePassword(event):
    TempVariables.ReportedPassword = EnterPassword.get()

    if "dbg" in str(sys.argv):
        print('Password Checking has been called.')

    hashed = hashlib.sha512(TempVariables.ReportedPassword.encode())
    
    if hashed.hexdigest() == variables.PasswordHash:
        if "dbg" in str(sys.argv):
            print('Password is correct!')

        TempVariables.ReportedPassword = ""
        # sleep(1)
        LogonUI.destroy()
        if "dbg" in str(sys.argv):
            print("Launching SCOS Desktop Environment.")
            os.system("cd desktopEnv ; python3 userland-ui.py dbg") # Launch userland-ui with dbg flag if this script was launched with it
        else:
            os.system("cd desktopEnv ; python3 userland-ui.py") # Launch userland-ui like a normal person.
    else:
        incorrectLabel = Label(LogonUI, text="Incorrect.") # Make fun of the user for entering a wrong password.
        incorrectLabel.place(relx=0.5, rely=0.1, anchor="c")
        if "dbg" in str(sys.argv):
            print("incorrect password")
        
def KillSwitch(event): # TODO: Make this only accessible in debug builds.
    sys.exit(1)
    print("Kill Switch Activated")

LogonUI.bind('<Return>', RetreivePassword)
LogonUI.bind('<F1>', KillSwitch)

LogonUI.mainloop()