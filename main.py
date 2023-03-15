# importing necessary modules
import tkinter
from tkinter import *
import pyshorteners

# GUI code
root = tkinter.Tk()
root.geometry('1100x360')
root.title('URL Shortener')
root.iconbitmap('icon.ico')

# function for url shortening
def shorten():
    url = pyshorteners.Shortener().tinyurl.short(longurl_entry.get())
    shorturl_entry.insert(END, url)

long = tkinter.Label(root, text='Enter the URL', font=('calibre', 15, 'bold')).pack(pady=20)
longurl_entry = tkinter.Entry(root, font=('calibre', 15, 'normal'), width=90)
longurl_entry.pack(pady=10)

button = tkinter.Button(root, text='Submit', font=('calibre', 13, 'bold',), width=8, bg='green', fg='white', command=shorten).pack(pady=10)

short = tkinter.Label(root, text="Shortened URL", font=('calibre', 15, 'bold')).pack(pady=30)
shorturl_entry = tkinter.Entry(root, font=('calibre', 15, 'normal'), width=50, bd=0, bg='systembuttonface', justify=CENTER)
shorturl_entry.pack()

root.mainloop()