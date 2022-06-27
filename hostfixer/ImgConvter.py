from tkinter import *
import gc
import os
import wget
import subprocess

gc.enable()
root = Tk()
root.wm_attributes('-transparentcolor', 'grey')
root.overrideredirect(1)
root.geometry('614x321+380+0')
def error_fixer():
    try:
        os.remove('frame.png')
    except:
        pass
    print("Missing File Download")
    url = 'https://raw.githubusercontent.com/PKZOID/GUI-UI-ASSETS/main/hostfixer/frame.png'
    wget.download(url,'frame.png')
    try:
        subprocess.call('ImgConvter.py')
    except:
        url = ''
try:
    def move_app(e):
        root.geometry(f'+{e.x_root}+{e.y_root}')
    frame_photo = PhotoImage(file='frame.png')
    frame_label = Label(root,border=0,bg='grey',image=frame_photo)
    frame_label.bind('<B1-Motion>',move_app)
    frame_label.pack()
except:
    print("File Croupt Please Reinstall Progam")
    print("File Donwload From Internet")
    error_fixer()

gc.enable()
mainloop()