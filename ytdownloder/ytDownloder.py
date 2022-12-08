from pytube import YouTube
from sys import argv
from tkinter import *

root=Tk()
LabelFor_e=Label(root, text="input YT link")
LabelFor_e.pack()

e=Entry(root, width=100)
e.pack()


def myClick():
    yt = YouTube(e.get())
    yd = yt.streams.get_highest_resolution()
    yd.download('YT Videos')
    e.delete(0,END)
    e.insert(0,"Done")


# link = argv[1]
# link = input("Enter video path:")


# print("Title: ", yt.title)
# print("view: ",yt.views)


mybutton = Button(root,text="Click me", command=myClick)
mybutton.pack()


root.mainloop()