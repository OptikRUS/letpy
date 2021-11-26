import tkinter
import random
import time


class TicTacToe(tkinter.Canvas):
    def __init__(self, window):
        super().__init__(window, width=300, height=300)
        self.state = [None, ] * 9
        self.bind('<Button-1>', self.click)

    def click(self, event):
        col = int(event.x / 100)
        row = int(event.y / 100)
        index = row * 3 + col
        self.index_x = index
        if self.state[index] is None:
            self.state[index] = 'x'
            self.add_x(col, row)

            if self.get_winner() is not None:
                if self.get_winner() == 'x_win':
                    self.create_text(150, 150, text='Победили крестики!', font=('Monospace 36', 30), fill='blue')
                    self.restart_game()
                elif self.get_winner() == 'o_win':
                    self.create_text(150, 150, text='Победили нолики!', font=('Monospace 36', 30), fill='red')
                    self.restart_game()
                else:
                    self.create_text(150, 150, text='Ничья!', font=('Monospace 36', 25))
                    self.restart_game()
            else:
                self.bot_move()

    def bot_move(self):
        col = random.randint(0, 2)
        row = random.randint(0, 2)
        index = row * 3 + col
        if self.state[index] is None:
            self.state[index] = 'o'
            self.add_o(col, row)
        else:
            return self.bot_move()

    def get_winner(self):
        variants = []
        for i, j in enumerate(range(0, 9, 3)):
            variants.append(self.state[j:j + 3])
            variants.append(self.state[i::3])
        variants.append(self.state[::4])
        variants.append(self.state[2:7:2])

        if ['x', ] * 3 in variants:
            return 'x_win'
        elif ['o', ] * 3 in variants:
            return 'o_win'
        elif None not in self.state:
            return 'draw'

    def add_x(self, column, row):
        self.create_line(
            column * 100 + 5,
            row * 100 + 95,
            column * 100 + 95,
            row * 100 + 5,
            width=5,
            fill='blue')
        self.create_line(
            column * 100 + 5,
            row * 100 + 5,
            column * 100 + 95,
            row * 100 + 95,
            width=5,
            fill='blue')

    def add_o(self, column, row):
        self.create_oval(
            column * 100 + 5,
            row * 100 + 5,
            column * 100 + 95,
            row * 100 + 95,
            width=5,
            outline='red')

    def restart_game(self):
        time.sleep(5)
        self.delete('all')
        self.state = [None, ] * 9
        self.draw_lines()

    def draw_lines(self):
        self.create_line(100, 0, 100, 300, fill='black')
        self.create_line(200, 0, 200, 300, fill='black')
        self.create_line(0, 100, 300, 100, fill='black')
        self.create_line(300, 200, 0, 200, fill='black')


tk_window = tkinter.Tk()
game = TicTacToe(tk_window)
game.pack()
game.draw_lines()

tk_window.mainloop()