from tkinter import *
root = Tk()
root.title("Rounded Button")
root.geometry('300x300')

#button

def test():
    print("Button Working")

round = PhotoImage(file='Rounded Button.png')
round_button = Button(root,image=round,border=0,command=test)
round_button.place(x=50,y=60)

root.mainloop()