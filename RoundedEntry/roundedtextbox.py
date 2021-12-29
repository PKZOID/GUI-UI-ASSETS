from tkinter import *
root = Tk()
root.geometry('600x500')
#background
white = Label(root,bg='white',width=600,height=500,border=0)
white.pack()

entry_name = PhotoImage(file='Rectangle 1.png')
entry_image = Label(root,image=entry_name,border=0,bg='white')
entry_image.place(x=260,y=140)

name_entry = Entry(root,width=27,border=0,font=('bold',11))
name_entry.place(x=267,y=144)

Email = Label(root,bg='white',font=('Bold',16),border=0,text="Email")
Email.place(x=345,y=170)

root.mainloop()