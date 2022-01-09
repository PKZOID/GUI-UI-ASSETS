from tkinter import *
root = Tk()

def active1():
    radiobutton_text.configure(text="UnCheck")
    active_photo.configure(file='inactive.png')
    active_button.configure(command=active2)
def active2():
    radiobutton_text.configure(text="Check")
    active_photo.configure(file='active.png')
    active_button.configure(command=active1)
    
active_photo  = PhotoImage(file='active.png')
active_button = Button(root,image=active_photo,command=active1,border=0)
active_button.place(x=0,y=0)

radiobutton_text = Label(root,text="Check",border=0,font=('bold',18))
radiobutton_text.place(x=40,y=60)

root.mainloop()
