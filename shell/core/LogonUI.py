import hashlib
from tkinter import *
from core import variables
from time import sleep
from core import TempVariables
import os
import sys

print("Opening LogonUI")
LogonUI = Tk()
LogonUI.title("Logon UI: Development")

w, h = LogonUI.winfo_screenwidth(), LogonUI.winfo_screenheight()

LogonUI.geometry("%dx%d+0+0" % (w, h))
LogonUI.attributes('-topmost', 1)
LogonUI.attributes('-type', 'splash')
LogonUI.focus_force()

screen_width = LogonUI.winfo_screenwidth()
screen_height = LogonUI.winfo_screenheight()

PasswordBoxLabel = Label(LogonUI, text="Yes, this is where you enter your password. You can TOTALLY trust this box!")
EnterPassword = Entry(LogonUI, show="*", width=25)
PressEnterLabel = Label(LogonUI, text="Key in your password and press enter!")

#LogonScreen1.pack()
PasswordBoxLabel.place(relx=0.5, rely=0.46, anchor="c")
EnterPassword.place(relx=0.5, rely=0.5, anchor="c")
PressEnterLabel.place(relx=0.5, rely=0.54, anchor="c")

def RetreivePassword(event):
    TempVariables.ReportedPassword = EnterPassword.get()

    print('Password Checking has been called.')

    hashed = hashlib.sha512(TempVariables.ReportedPassword.encode())
    print("Password Hash: "+hashed.hexdigest())
    if hashed.hexdigest() == variables.PasswordHash:
        print('Passwords match!')
        TempVariables.ReportedPassword = ""
        sleep(1)
        LogonUI.quit()
        print("Launching SCOS Desktop Environment.")
        os.system("cd desktopEnv ; sh launch.sh")
    else:
        incorrectLabel = Label(LogonUI, text="Incorrect.")
        incorrectLabel.place(relx=0.5, rely=0.1, anchor="c")
        print("incorrect password")
        
def KillSwitch(event):
    sys.exit(1)
    print("Kill Switch Activated")

LogonUI.bind('<Return>', RetreivePassword)
LogonUI.bind('<F1>', KillSwitch)

LogonUI.mainloop()