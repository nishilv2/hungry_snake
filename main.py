__author__ = 'lenovo'
from snake_game import SnakeGame
from Tkinter import *


tk = Tk()


def start():
    snake_game = SnakeGame(tk, 500)
    tk.mainloop()

if __name__ == "__main__":
    start()