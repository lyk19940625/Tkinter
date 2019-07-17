#Menubar
import tkinter as tk
window = tk.Tk()
window.title("my window")
window.geometry('200x200')

l = tk.Label(window,text = '操作',bg = 'yellow')
l.pack()
counter = 0
def do_job():
    global counter
    counter += 1
    l.config(text = 'do'+str(counter))

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar,tearoff = 0)
menubar.add_cascade(label = 'File',menu = filemenu)
filemenu.add_command(label = 'New',command = do_job)
filemenu.add_command(label = 'Open',command = do_job)
filemenu.add_command(label = 'Save',command = do_job)
filemenu.add_separator()
filemenu.add_command(label = 'exit',command = window.quit)
editmenu = tk.Menu(menubar,tearoff = 0)
menubar.add_cascade(label = 'Edit',menu = editmenu)
editmenu.add_command(label = 'Cut',command = do_job)
editmenu.add_command(label = 'Copy',command = do_job)
editmenu.add_command(label = 'Paste',command = do_job)
selectmenu = tk.Menu(menubar,tearoff = 0)
menubar.add_cascade(label = 'Select',menu = selectmenu)
submenu = tk.Menu(selectmenu)
selectmenu.add_cascade(label = 'Import',menu = submenu,underline = 0)
submenu.add_cascade(label = 'Submenu1',command = do_job)
submenu.add_cascade(label = 'Submenu3',command = do_job)

window.config(menu = menubar)

window.mainloop()
