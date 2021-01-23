# Servr Co OS first boot UI. Installs and configures packages before allowing the shell to run.
from tkinter import *
from subprocess import call
import findPkg
import os

win = Tk()
win.title("Servr Co OS First Boot")

w, h = win.winfo_screenwidth(), win.winfo_screenheight()

win.geometry("%dx%d+0+0" % (w, h)) # This block of code sets win to fullscreen and as top priority.
win.attributes('-topmost', 1)
win.attributes('-type', 'splash')
win.focus_force()

# By now, we are ready to begin installing things. First, let's paint a nicer background.
Canvas(win, bg="#3b3b3b", width=w, height=h).place(anchor="c", relx=0.5, rely=0.5)
topLabel = Label(win, bg="#3b3b3b", text="Servr Co OS", fg="#ffffff")
topLabel.config(font=("Arial", 40))
topLabel.place(anchor="n", relx=0.5)

whatsHappeningLabel = Label(win, bg="#3b3b3b", text="Preparing to install Servr Co OS", fg="#ffffff")
whatsHappeningLabel.config(font=("Arial", 20))
whatsHappeningLabel.place(anchor="n", relx=0.5, rely=0.5)

actionLabel = Label(win, bg="#3b3b3b", text="Checking for installed packages", fg="#ffffff")
actionLabel.config(font=("Arial", 15))
actionLabel.place(anchor="n", relx=0.5, rely=0.55)

# Now we are checking for existance of several apt packages. They will be saved to a list if they need to be installed.
findPkg.findTkinter(False)
findPkg.findImageTk(False)

actionLabel.config(text="Installing packages.")

for pkg in findPkg.pkgsToInstall:
    print("Installing " + pkg)
    os.system("sudo apt install " + pkg)

actionLabel.config(text="Installed packages.")

def killSwitch(event):
    win.destroy()

win.bind_all("<F1>", func=killSwitch) # Closes out the window when f1 is pressed, just in case something happens.
win.mainloop()
