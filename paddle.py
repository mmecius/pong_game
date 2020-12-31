from turtle import Turtle

LEN = 1
WID = 5
MOVE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=WID, stretch_len=LEN)
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + MOVE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE
        self.goto(self.xcor(), new_y)
