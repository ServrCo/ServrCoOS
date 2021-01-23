# This is the Servr Co OS about menu. It's just great.
buildver="Jan19-2021"

from tkinter import *

def makeEggPopup():
    eggWin = Tk()
    eggWin.title("No.")
    eggWin.geometry("200x100")
    Label(eggWin, text="No.\nWhy would I tell you more?").place(anchor="n", relx=0.5, rely=0.2)
    Button(eggWin, text="Ok. I'll go now.", command=lambda: eggWin.destroy()).place(anchor="n", relx=0.5, rely=0.6)
    eggWin.mainloop()

win = Tk()
win.title("About SCOS")
win.attributes("-type", "utility")

win.geometry("400x150")
Label(win, text="Servr Co OS\nA desktop environment by Servr Co.").place(anchor="n", relx=0.5)
Label(win, text="Build version: " + buildver).place(anchor="n", relx=0.5, rely=0.25)
tellMeMore = Button(win, text="Tell me more", command=makeEggPopup)
tellMeMore.place(anchor="n", relx=0.5, rely=0.75)

try:
    win.mainloop()
except KeyboardInterrupt:
    print("There is no escape.")
