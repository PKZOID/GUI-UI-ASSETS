from tkinter import *
from PIL import Image

root = Tk()
root.title("Image Hover")
root.geometry("450x450")

#on_enter
def on_enter(e):
    pickhu_image.configure(file='picku_hover.png')
#on_leave
def on_leave(e):
    pickhu_image.configure(file='picku_orignal.png')

#image
pickhu_image = PhotoImage(file='picku_orignal.png')
pickhu_label = Label(root,image=pickhu_image,border=0)
pickhu_label.place(x=80,y=100)
 
#label bind
pickhu_label.bind("<Enter>",on_enter)
pickhu_label.bind("<Leave>",on_leave)

root.mainloop()