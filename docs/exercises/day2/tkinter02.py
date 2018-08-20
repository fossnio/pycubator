#!/usr/bin/python3
import tkinter


windows = tkinter.Tk()
windows.title('我的第一個視窗程式')

label = tkinter.Label(windows, text='我是 label')
label.pack()

button = tkinter.Button(windows, text='我是 button')
button.pack()

windows.mainloop()
