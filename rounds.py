import tkinter
import random

window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()

colors = ('red', 'green', 'blue', 'purple', 'yellow', 'black', 'orange')

def my_click(event):
    radius = random.randint(10, 50)
    canvas.create_oval(
        event.x - radius,
        event.y - radius,
        event.x + radius,
        event.y + radius,
        outline=random.choice(colors))
    canvas.update()

canvas.bind('<Button-1>', my_click)
window.mainloop()