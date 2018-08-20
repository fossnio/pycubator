#!/usr/bin/python3
import tkinter
import datetime


windows = tkinter.Tk()
windows.title('我的第一個視窗程式')

label = tkinter.Label(windows, text='我是 label')
label.pack()

def show_me_the_time():
    now = datetime.datetime.now()
    label.configure(text=str(now))

button = tkinter.Button(windows, text='顯示現在時間', command=show_me_the_time)
button.pack()

windows.mainloop()
