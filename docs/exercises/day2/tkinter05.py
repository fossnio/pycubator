#!/usr/bin/python3
import tkinter
import urllib.request


windows = tkinter.Tk()
windows.title('顯示網頁')

text = tkinter.Text(windows)
text.pack()

def fetch_web():
    bot = urllib.request.urlopen('https://tw.yahoo.com')
    web_content = bot.read().decode('utf-8')
    text.insert(tkinter.END, web_content)

button = tkinter.Button(windows, text='抓網頁', command=fetch_web)
button.pack()

windows.mainloop()
