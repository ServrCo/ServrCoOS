import os

pkgsToInstall = []

true=True
false=False

def findImageTk(resolveIfNeeded):
    "Finds the existance of ImageTK on your system, and installs it if requested."
    try:
        print("Finding ImageTK.")
        from PIL import ImageTk, Image
        return true

    except ImportError:
        if resolveIfNeeded:
            print("Resolving package.")
            os.system("sudo apt install python3-pil.imagetk")
            return true
        else:
            pkgsToInstall.append("python3-pil.imagetk")
            return false

def findTkinter(resolveIfNeeded):
    "Finds the existance of Tkinter on your system, and installs it if requested."
    try:
        print("Finding Tkinter.")
        from tkinter import Tk
        return true

    except ImportError:
        if resolveIfNeeded:
            print("Resolving package.")
            os.system("sudo apt install python3-tk")
            return true
        else:
            pkgsToInstall.append("python3-tk")
            return false
