from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

root = Tk()
root.title("LocalTube")
root.geometry("350x350")
root.columnconfigure(0, weight=1)

#Link label
LinkLabel =  Label(root, text="Enter YouTube URL below!", font=("Helvetica",15,"bold"))
LinkLabel.grid()

# Link input
LinkInputVar = StringVar()
LinkInput = Entry(root,width=50,textvariable=LinkInputVar)
LinkInput.grid()

# Error msg if unknown link is used
LinkError = Label(root,text="error unknown link",fg="red",font=("Helvetica",10,"bold"))
LinkError.grid()

# Video save options label
SaveLabel = Label(root,text="Video save options:",font=("Helvetica",15,"bold"))
SaveLabel.grid()

# File path browse button
SaveInput = Button(root,width=20,bg="blue",fg="white", text="Select Download Location")
SaveInput.grid()

# Error msg if no path selected
PathError = Label(root,text="error select download location", fg="red", font=("Helvetica",10))
PathError.grid()

# Quality label
QualitySelect = Label(root,text="Select download quality",font=("Helvetica",15,"bold"))
QualitySelect.grid()

# Quality choices
qualityChoice = ["1080p - (mp4)","720p - (mp4)","480p - (mp4)","144p - (mp4)","Audio -  (mp3)"]
QualityChoices = ttk.Combobox(root,values=qualityChoice)
QualityChoices.grid()

# Download button
downloadbtn = Button(root,text="Download",width=10,bg="red",fg="white")
downloadbtn.grid()

root.mainloop()
