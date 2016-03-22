__author__ = 'lenovo'
from snake import Snake
from random import randint
import tkMessageBox
from Tkinter import *
from api import Api


class SnakeGame(object):
    def __init__(self, tk, speed):
        self.food = (randint(0, 20), randint(0, 20))
        self.speed = speed
        self.snake = Snake()
        self.tk = tk
        self.button = Button(tk, text="start game!", command=self.run)
        self.canvas = Canvas(tk, width=410, height=410, bg="black")
        self.button.pack()
        self.canvas.pack()
        self.tk.bind("<KeyPress-Up>", self.up_event)
        self.tk.bind("<KeyPress-Down>", self.down_event)
        self.tk.bind("<KeyPress-Right>", self.right_event)
        self.tk.bind("<KeyPress-Left>", self.left_event)

    def run(self):
        if self.snake.eat(self.food):
            eat_flag = 1
            self.food = None
        else:
            eat_flag = 0
        self.snake.move(eat_flag)
        if self.not_over():
            self.canvas.delete("all")
            self.draw_food()
            self.draw_snake()
            self.tk.after(self.speed, self.run)
        else:
            r = tkMessageBox.showinfo("Oh,game over!")
            if r == "ok":
                sys.exit()

    def not_over(self):
        if self.is_rush_wall() or self.is_rush_self():
            return 0
        else:
            return 1

    def draw_snake(self):
        for i in range(0, self.snake.body.__len__()):
            x0, y0 = Api.position_to_pix(self.snake.body[i][0], self.snake.body[i][1])
            x1 = x0+10
            y1 = y0+10
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="white", outline=None, width=0)
            if i != (self.snake.body.__len__()-1):
                x2, y2 = Api.position_to_pix(self.snake.body[i+1][0], self.snake.body[i+1][1])
                x3 = (x0 + x2)/2
                y3 = (y0 + y2)/2
                x4 = x3+10
                y4 = y3+10
                self.canvas.create_rectangle(x3, y3, x4, y4, fill="white", outline=None, width=0)

    def change_snake_direction(self, direction):
        r = self.snake.change_direction(direction)
        if not r:
            print "you can't do that"

    def up_event(self, event):
        self.change_snake_direction("up")
        print "up"

    def down_event(self, event):
        self.change_snake_direction("down")
        print "down"

    def right_event(self, event):
        self.change_snake_direction("right")
        print "right"

    def left_event(self, event):
        self.change_snake_direction("left")
        print "left"

    def food_exist(self):
        if self.food is None:
            return 0
        else:
            return 1

    def draw_food(self):

        if not self.food_exist():
            world = []
            for i in range(0, 21):
                for j in range(0, 21):
                    world.insert(-1, (i, j))
            for item in self.snake.body:
                world.remove(item)
            self.food = world[randint(0, world.__len__()-1)]
        x0, y0 = Api.position_to_pix(self.food[0], self.food[1])
        x1 = x0+10
        y1 = y0+10
        self.canvas.create_rectangle(x0, y0, x1, y1, fill="white", outline=None, width=0)

    def is_rush_wall(self):
        if (self.snake.body[0][0] >= 0) and (self.snake.body[0][0] <= 20):
            if (self.snake.body[0][1] >= 0) and (self.snake.body[0][1] <= 20):
                return 0
            else:
                return 1
        else:
            return 1

    def is_rush_self(self):
        result = 0
        for i in range(1, self.snake.body.__len__()):
            if self.snake.body[0] == self.snake.body[i]:
                result = 1
                break
        return result