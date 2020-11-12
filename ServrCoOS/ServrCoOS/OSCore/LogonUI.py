import hashlib
from tkinter import *
from OSCore import variables
from OSCore import DataHandler
from time import sleep
from OSCore import TempVariables

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

LogonScreen1 = Canvas(LogonUI, width=screen_width - 1, height=screen_height - 95)
PasswordBoxLabel = Label(LogonUI, text="Yes, this is where you enter your password. You can TOTALLY trust this box!")
EnterPassword = Entry(LogonUI, show="*", width=25)
PressEnterLabel = Label(LogonUI, text="Key in your password and press enter!")

DataHandler.open_log()
DataHandler.log("Password Box Element Loading...")
DataHandler.close_log()

LogonScreen1.pack()
PasswordBoxLabel.pack()
EnterPassword.pack()
PressEnterLabel.pack()

LogonScreen1.configure(background="green")

DataHandler.open_log()
DataHandler.log("Password Box Element Loaded")
DataHandler.close_log()

def RetreivePassword(event):
    TempVariables.ReportedPassword = EnterPassword.get()

    DataHandler.open_log()
    DataHandler.log("Attempting to retreive password.")
    DataHandler.log(TempVariables.ReportedPassword)
    DataHandler.close_log()

    print('i got that password for ya.')
    print('now i will check it for you.')
    hashed = hashlib.sha512(TempVariables.ReportedPassword.encode())
    print(hashed.hexdigest())
    if hashed.hexdigest() == variables.PasswordHash:
        print('passwords match!')
        TempVariables.ReportedPassword = ""
        
        sleep(1)
        LogonUI.quit()

def KillSwitch(event):
    LogonUI.quit()
    print("Kill Switch Activated")

LogonUI.bind('<Return>', RetreivePassword)
LogonUI.bind('<F2>', KillSwitch)


DataHandler.open_log()
DataHandler.log("We are now successfully at the end of the LogonUI Code.")
DataHandler.close_log()

LogonUI.mainloop()