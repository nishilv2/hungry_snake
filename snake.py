__author__ = 'lenovo'


class Snake(object):
    def __init__(self):
        self.body = [(13, 12), (12, 12), (11, 12)]
        self.direction = "right"

    def move(self, eat_flag):
        head_new_x = None
        head_new_y = None
        if self.direction == "right":
            head_new_x = self.body[0][0]+1
            head_new_y = self.body[0][1]
        elif self.direction == "left":
            head_new_x = self.body[0][0]-1
            head_new_y = self.body[0][1]
        elif self.direction == "up":
            head_new_x = self.body[0][0]
            head_new_y = self.body[0][1]-1
        elif self.direction == "down":
            head_new_x = self.body[0][0]
            head_new_y = self.body[0][1]+1
        head_new = (head_new_x, head_new_y)
        self.body.insert(0, head_new)
        if not eat_flag:
            self.body.pop()

    def eat(self, food):
        if (self.body[0][0] == food[0]) and (self.body[0][1] == food[1]):
            return 1
        else:
            return 0

    def change_direction(self, direction):
        if direction == "right":
            if self.direction != "left":
                self.direction = direction
                return 1
            else:
                return 0
        elif direction == "left":
            if self.direction != "right":
                self.direction = direction
                return 1
            else:
                return 0
        elif direction == "up":
            if self.direction != "down":
                self.direction = direction
                return 1
            else:
                return 0
        elif direction == "down":
            if self.direction != "up":
                self.direction = direction
                return 1
            else:
                return 0
        else:
            return 0