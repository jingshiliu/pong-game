from turtle import Turtle

BALL_COLOR = 'pink'
BALL_SPEED = 4


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color(BALL_COLOR)
        self.penup()
        self.shape('circle')
        self.x_move = BALL_SPEED
        self.y_move = BALL_SPEED

    def move(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce_y()

        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_pos(self):
        self.bounce_x()
        self.goto(0, 0)
