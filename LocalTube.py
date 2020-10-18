from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
# Importing modules needed / pip3 install pytube
Folder_Name = ""

# File Location function
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        PathError.config(text=Folder_Name,fg="blue")
    else:
        PathError.config(text="Error select a file location",fg="red")

# Donwload video function
def DownloadVideo():
    choice = qualityChoices.get()
    url = LinkInput.get()

    if(len(url)>1):
        LinkError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
           LinkError.config(text="Paste Link again!!",fg="red")


    # Download function
    select.download(Folder_Name)
    LinkError.config(text="Download Completed 100%")
# Tkinter GUI
root = Tk()
root.title("LocalTube")
root.geometry("350x350")
root.configure(bg='white')
root.columnconfigure(0, weight=1)

#Link label
LinkLabel =  Label(root, text="Enter YouTube URL below!",bg="white",font=("Helvetica",15,"bold"))
LinkLabel.grid()

# Link input
LinkInputVar = StringVar()
LinkInput = Entry(root,width=50,textvariable=LinkInputVar)
LinkInput.grid()

# Error msg if unknown link is used
LinkError = Label(root,text="",fg="red",bg="white",font=("Helvetica",10,"bold"))
LinkError.grid()

# Video save options label
SaveLabel = Label(root,text="Video save options:",bg="white",font=("Helvetica",15,"bold"))
SaveLabel.grid()

# File path browse button
SaveInput = Button(root,width=20,text="Select Download Location",bg="red",command=openLocation)
SaveInput.grid()

# Error msg if no path selected
PathError = Label(root,text="select download location before downloading! ", fg="red",bg="white", font=("Helvetica",10,"bold"))
PathError.grid()

# Quality label
QualitySelect = Label(root,text="Select download quality",bg="white",font=("Helvetica",15,"bold"))
QualitySelect.grid()

# Combobox 
choices = ["720p","144p","Only Audio"]
qualityChoices = ttk.Combobox(root,values=choices)
qualityChoices.grid()

# Download button
downloadbtn = Button(root,text="Download",width=10,fg="red",command=DownloadVideo)
downloadbtn.grid()

# Dev Info
devLabel = Label(root,bg="white",text="Made by Daniel Duque using Python & Tkinter",font=("Helvetica",15,"bold"))
devLabel.grid()

root.mainloop()
