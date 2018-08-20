#!/usr/bin/python3
import tkinter


windows = tkinter.Tk()
windows.title('顯示網頁')

text = tkinter.Text(windows)
text.pack()

button = tkinter.Button(windows, text='抓網頁')
button.pack()

windows.mainloop()
