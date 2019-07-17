#Canvas
import tkinter as tk
window = tk.Tk()
window.title("my window")
window.geometry('500x500')

canvas = tk.Canvas(window,bg = 'blue',width = 400,height = 400)
imagefile = tk.PhotoImage(file =
                'H:\PythonWorkSpace\homework\Tkinter\img.gif')
image = canvas.create_image(0,0,anchor = 'nw',image = imagefile)
x0,y0,x1,y1 = 50,50,80,80
oval = canvas.create_oval(x0,y0,x1,y1,fill = 'red')
canvas.pack()

def moveit():
    canvas.move(oval,0,2)

b = tk.Button(window,text = 'move',command = moveit)
b.pack()



window.mainloop()
