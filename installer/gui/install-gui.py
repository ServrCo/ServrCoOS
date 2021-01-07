from tkinter import *
import os
win = object()
installButton = object()

def startInstall():
    print("Installing")
    installButton.destroy()
    os.system("")
    

def main(): # This dialog box was created early on a Thursday morning. Please, someone who makes better user interfaces, fix it.
    global win
    global installButton
    win = Tk()
    win.title("Servr Co OS Installer")
    win.geometry("400x500")
    installButton = Button(win, text="Install", command=startInstall)
    installButton.place(relx=0.5, rely=0.5, anchor="c")
    win.mainloop()

main()