#Messagebox
import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("my window")
window.geometry('200x200')

def hit_me():
    #messagebox.showinfo(title = 'hi',message = 'hahaha')
    #messagebox.showinfo(title = 'hi',message = 'nonono')
    #messagebox.showerror(title = 'hi',message = 'stop!')
    #messagebox.askquestion(title = 'hi',message = 'ok？') #return yes no
    messagebox.askyesno(title = 'hi',message = 'ok?')#return true false
tk.Button(window,text = 'hit me',command = hit_me).pack()

window.mainloop()
