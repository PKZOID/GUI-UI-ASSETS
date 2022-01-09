from tkinter import *
root = Tk()
root.title("Custom Radio Button")
root.geometry('300x300')

#active radio button
def active1():
    radiobutton_photo.configure(file='inactive.png')
    radiobutton_Btn.configure(command=inactive1)
def inactive1():
    radiobutton_Btn.configure(command=active1)
    radiobutton_photo.configure(file='active.png')

#radio button
radiobutton_photo = PhotoImage(file='active.png')
radiobutton_Btn = Button(root,image=radiobutton_photo,border=0,command=active1)
radiobutton_Btn.pack()

root.mainloop()