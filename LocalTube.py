from pytube import YouTube
from tkinter import *

class LocalTubeGUI:
    def __init__(self, master):
        self.master = master
        master.title("LocalTube")

        Label(master, text="LocalTube").pack()

        # Enter youtube video URL here

        # Dropdown menu option

        # Download after selecting menu option

        Button(master, text="Exit Program", command=master.quit).pack()

root = Tk()
root.geometry("1000x700")
my_gui = LocalTubeGUI(root)
root.mainloop()
