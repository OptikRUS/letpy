import tkinter
import random

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=400, height=400)
canvas.pack()

colors = ('Red', 'gold1', 'forest green', 'gold', 'cyan', 'Blue', 'Purple')
circles = []
for i in range(5):
    size = random.randint(0, 50)
    x = random.randint(100, 400)
    y = random.randint(100, 400)
    color = random.choice(colors)
    circles.append({
        'dx': random.randint(-10, 10),
        'dy': random.randint(-10, 10),
        'id': canvas.create_oval(x, y, x + size, y + size, fill=color),
    })

while True:
    for circle in circles:
        x0, y0, x1, y1 = canvas.coords(circle['id'])

        if x0 < 0 or x1 > 400:
            circle['dx'] = -circle['dx']

        if y0 < 0 or y1 > 400:
            circle['dy'] = -circle['dy']
        canvas.move(circle['id'], circle['dx'], circle['dy'])

    canvas.update()