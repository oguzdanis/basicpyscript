#Youtube'dan indirmek istediginiz videoyu istediginiz yol'a istediginiz cozunurluk ve formatda indiren program.
from pytube import YouTube
import sys
link=input("Enter the Youtube video URL")
yt = YouTube(link)
print("Please wait!----")
title = yt.title
print("The video Title is",title)
resolution=yt.streams.all()
for i in resolution:
	print(i)
no=int(input("Enter Video itag number-->"))
video=yt.streams.get_by_itag(no)
path=input("enter file path where to save The Video")
filename=input("Enter filename of the video\n")
video.download(path,filename)

print(filename+"is succesfully downloaded in"+path)
sys.exit()
