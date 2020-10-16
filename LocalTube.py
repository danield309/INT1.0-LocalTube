from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name = ""

# File Location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        PathError.config(text=Folder_Name,fg="blue")
    else:
        PathError.config(text="Error select a file location",fg="black",bg="red")

#donwload video
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


    #download function
    select.download(Folder_Name)
    LinkError.config(text="Download Completed!!")

root = Tk()
root.title("LocalTube")
root.geometry("350x350")
root.configure(bg='red')
root.columnconfigure(0, weight=1)

#Link label
LinkLabel =  Label(root, text="Enter YouTube URL below!",bg="red",font=("Helvetica",15,"bold"))
LinkLabel.grid()

# Link input
LinkInputVar = StringVar()
LinkInput = Entry(root,width=50,textvariable=LinkInputVar)
LinkInput.grid()

# Error msg if unknown link is used
LinkError = Label(root,text="error unknown link",fg="black",bg="red",font=("Helvetica",10,"bold"))
LinkError.grid()

# Video save options label
SaveLabel = Label(root,text="Video save options:",bg="red",font=("Helvetica",15,"bold"))
SaveLabel.grid()

# File path browse button
SaveInput = Button(root,width=20,text="Select Download Location",bg="red",command=openLocation)
SaveInput.grid()

# Error msg if no path selected
PathError = Label(root,text="error select download location", fg="black",bg="red", font=("Helvetica",10,"bold"))
PathError.grid()

# Quality label
QualitySelect = Label(root,text="Select download quality",bg="red",font=("Helvetica",15,"bold"))
QualitySelect.grid()

#combobox
choices = ["720p","144p","Only Audio"]
qualityChoices = ttk.Combobox(root,values=choices)
qualityChoices.grid()

# Download button
downloadbtn = Button(root,text="Download",width=10,fg="red",command=DownloadVideo)
downloadbtn.grid()

# Dev Info
devLabel = Label(root,bg="red",text="Made by Daniel Duque using Python & Tkinter",font=("Helvetica",15,"bold"))
devLabel.grid()

root.mainloop()
