from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

root = Tk()
root.title("LocalTube")
root.geometry("350x350")
root.columnconfigure(0, weight=1)

#Link label
LinkLabel =  Label(root, text="Enter YouTube URL below!", font=("Helvetica", 15))
LinkLabel.grid()

# Link input
LinkInputVar = StringVar()
LinkInput = Entry(root,width=50,textvariable=LinkInputVar)
LinkInput.grid()

# Error msg if unknown link is used
LinkError = Label(root,text="error unknown link",fg="red",font=("Helvetica", 10))
LinkError.grid()

# Video save options label
SaveLabel = Label(root,text="Video save options:",font=("Helvetica", 15))
SaveLabel.grid()

# File path browse button
SaveInput = Button(root,width=20,bg="blue",fg="white", text="Select Download Location")
SaveInput.grid()

# Error msg if no path selected
PathError = Label(root,text="error select download location", fg="red", font=("Helvetica",10))
PathError.grid()

root.mainloop()
