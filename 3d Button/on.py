from tkinter import *
root = Tk()
root.title("Custom On/Off Button")
root.geometry('500x300')
root.resizable(False,False)

def on():
    on_photo.configure(file='Off.png')
    on_label.bind("<Button-1>", lambda e:off())
def off():
    on_photo.configure(file='On.png')
    on_label.bind("<Button-1>", lambda e:on())

on_photo = PhotoImage(file='On.png')

on_label = Label(root,image=on_photo,border=0)
on_label.place(x=20,y=10)
on_label.bind("<Button-1>", lambda e:on())
root.mainloop()