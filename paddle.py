from turtle import Turtle

PADDLE_COLOR = 'white'
PADDLE_SPEED = 30


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.shape('square')
        self.color(PADDLE_COLOR)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos)

    def up(self):
        self.goto(self.xcor(), self.ycor() + PADDLE_SPEED)

    def down(self):
        self.goto(self.xcor(), self.ycor() - PADDLE_SPEED)

