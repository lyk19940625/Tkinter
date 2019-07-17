#Checkbutton
import tkinter as tk
window = tk.Tk()
window.title("my window")
window.geometry('200x200')

l = tk.Label(window,bg = 'yellow',width = 20,text = 'empty')
l.pack()

var1 = tk.IntVar()
var2 = tk.IntVar()
def print_selection():
    if(var1.get() == 1)&(var2.get() == 0):
        l.config(text = 'i love only Python')
    elif(var1.get() == 0)&(var2.get() == 1):
        l.config(text = 'i love only C++')
    elif(var1.get() == 0)&(var2.get() == 0):
        l.config(text = 'i do not love either')
    else:
        l.config(text = 'i love both')

c1 = tk.Checkbutton(window,text = 'Python',variable = var1,
                onvalue = 1,offvalue = 0,command = print_selection)
c2 = tk.Checkbutton(window,text = 'C++',variable = var2,
                onvalue = 1,offvalue = 0,command = print_selection)
c1.pack()
c2.pack()
window.mainloop()
