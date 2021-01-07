from tkinter import *
import os
win = Tk()
win.title("Crash")

win.attributes("-fullscreen", True)
win.attributes("-zoomed", True)

def relaunch():
    win.destroy()
    print("Now relaunching.")
    os.system("cd ../.. ; ./OSStartup")

def exit():
    win.destroy()

Label(win, text="Shell has crashed. Press a button to continue.").place(relx=0.5, rely=0.45, anchor="c")
Button(win, text="relaunch", command=relaunch).place(relx=0.45, rely=0.51, anchor="c")
Button(win, text="exit", command=exit).place(relx=0.55, rely=0.51, anchor="c")

def KillSwitch(event):
    win.destroy()

win.bind_all("<F1>", KillSwitch)

win.mainloop()