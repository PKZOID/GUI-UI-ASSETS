from tkinter import *
import tkxui
root = tkxui.Tk(display=tkxui.FRAMELESS)
root.geometry('500x300')

def volumedown():
    voloume_photo.configure(file='Volume 0.png')

def volumeup():
    voloume_photo.configure(file='Volume 1.png')
    button2.configure(command=volumeup1)
def volumeup1():
    voloume_photo.configure(file='Volume 2.png')
    button2.configure(command=volumeup2)
def volumeup2():
    voloume_photo.configure(file='Volume 3.png')
    button2.configure(command=volumeup3)
def volumeup3():
    voloume_photo.configure(file='Volume 4.png')
    button2.configure(command=volumeup4)
def volumeup4():
    voloume_photo.configure(file='Volume 5.png')
    button2.configure(command=volumeup5)
def volumeup5():
    voloume_photo.configure(file='Volume 6.png')
    button2.configure(command=volumeup6)
def volumeup6():
    voloume_photo.configure(file='Volume 7.png')
    button2.configure(command=volumeup7)
def volumeup7():
    voloume_photo.configure(file='Volume 8.png')
    button2.configure(command=volumeup8)
def volumeup8():
    voloume_photo.configure(file='Volume 9.png')
    button2.configure(command=volumeup9)
def volumeup9():
    voloume_photo.configure(file='Volume 10.png')
    button2.configure(command=volumeup10)
def volumeup10():
    voloume_photo.configure(file='Volume 11.png')
    button2.configure(command=volumeup11)
def volumeup11():
    voloume_photo.configure(file='Volume full.png')
    button2.configure(command=volumeup1)
#image
voloume_photo = PhotoImage(file='Volume 0.png')
#button
volume_button = Label(root,image=voloume_photo,border=0).place(x=100,y=100)
button1 = Button(root,text="Volume Down",relief='groove',command=volumedown)
button1.place(x=110,y=360)
button2 = Button(root,text="Volume Up",relief='groove',command=volumeup)
button2.place(x=350,y=360)

root.mainloop()