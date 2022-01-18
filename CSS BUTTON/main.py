from tkinter import *
import tkxui
root = tkxui.Tk(display=tkxui.FRAMELESS)
root.geometry('570x400')+str(root.center())

background = Label(root,bg='white',width=500,height=500).pack()

def on():
    Off_photo.configure(file='on.png')
    on_btn.bind("<Button>",lambda e:off())
def on1():
    Off1_photo.configure(file='on1.png')
    on1_btn.bind("<Button>",lambda e:off1())
def off():
    Off_photo.configure(file='Off.png')
    on_btn.bind("<Button>",lambda e:on())
def off1():
    Off1_photo.configure(file='off1.png')
    on1_btn.bind("<Button>",lambda e:on1())

#image
Off_photo = PhotoImage(file='Off.png')
Off1_photo = PhotoImage(file='off1.png')

#button
on_btn = Label(root,image=Off_photo,border=0)
on_btn.place(x=50,y=100)
on1_btn = Label(root,image=Off1_photo,border=0)
on1_btn.place(x=300,y=160)

#label bind
on_btn.bind("<Button>",lambda e:on())
on1_btn.bind("<Button>",lambda e:on1())

root.mainloop()