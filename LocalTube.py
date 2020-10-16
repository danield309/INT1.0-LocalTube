from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

root = Tk()
root.title("LocalTube")
root.geometry("350x350")
root.columnconfigure(0, weight=1)

#Link Label
LinkLabel =  Label(root, text="Enter YouTube URL below!", font=("Helvetica", 15))
LinkLabel.grid()

# Link Input
LinkInputVar = StringVar()
LinkInput = Entry(root,width=50,textvariable=LinkInputVar)
LinkInput.grid()

#Error msg if unknown link is used
LinkError = Label(root,text="Error",fg="red",font=("Helvetica", 10))
LinkError.grid()

root.mainloop()
