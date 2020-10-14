from pytube import YouTube

# Handles user input
link = input("Enter YT video link: ")
yt = YouTube(link)

# Video Title
print("Title of video: ",yt.title)

# Number of views of video
print("Number of views: ",yt.views)

# Length of video
print("Length of video: ",yt.length, "seconds")

# Description of video
print("Description: ",yt.description)

# Video Rating
print("Ratings: ",yt.rating)
