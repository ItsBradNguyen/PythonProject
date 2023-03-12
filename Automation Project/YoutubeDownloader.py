from pytube import YouTube
from sys import argv

link = input("Please enter a YouTube link: ")
yt = YouTube(link)

print("Title: ", yt.title)
print(f"View: {yt.views}")

yd = yt.streams.get_highest_resolution()

question = input("Do you want to download this video (yes/no)? ").lower()

if question == "yes":
    output = input("Where do you want to store this video? ")
    yd.download(output)
else:
    quit()