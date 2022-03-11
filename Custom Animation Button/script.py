from tkinter import *
import threading as th  


root = Tk()
root.title("Button Hover")
root.geometry("450x450")
root.config(bg='white')

def on_click():
    button_image.configure(file='button_active.png')
    def recall():
        button_image.configure(file='button.png')
    S = th.Timer(0.1, recall)  
    S.start() 


def on_rounded():
    rounded_button.configure(file='rounede_button_active.png')
    def recall():
        rounded_button.configure(file='rounded_button.png')
    S = th.Timer(0.1, recall)  
    S.start() 

def on_bar():
    bar_button.configure(file='bar_button_active.png')
    def recall():
        bar_button.configure(file='bar_button.png')
    S = th.Timer(0.1, recall)  
    S.start() 

#image
button_image = PhotoImage(file='button.png')
rounded_button = PhotoImage(file='rounded_button.png')
bar_button  = PhotoImage(file='bar_button.png')

#button label
label_button = Label(root,image=button_image,border=0)
label_button.place(x=100,y=100)

rounded_button_label = Label(root,image=rounded_button,border=0)
rounded_button_label.place(x=100,y=200)

bar_button_label = Label(root,image=bar_button,border=0,bg='white')
bar_button_label.place(x=300,y=200)

label_button.bind("<Button>",lambda e:on_click())
rounded_button_label.bind("<Button>",lambda e:on_rounded())
bar_button_label.bind("<Button>",lambda e:on_bar())

root.mainloop()