from tkinter import *
root = Tk()
root.title("Custom Toggle Button")
root.geometry("300x300")

def off():
    toggle_photo.configure(file='Toggle Off.dll')
    toggle_button.configure(command=on)
    onoff.configure(text='Off')
def on():
    toggle_photo.configure(file='Toggle On.dll')
    toggle_button.configure(command=off)
    onoff.configure(text='On')

toggle_photo = PhotoImage(file='Toggle On.dll')
toggle_button = Button(root,image=toggle_photo,border=0,command=off)
toggle_button.place(x=150,y=30)


#on / off label
onoff = Label(root,text="On",border=0,font=('bold',18))
onoff.place(x=150,y=0)

root.mainloop()