from turtle import Turtle

BOARD_COLOR = 'white'


def create_middle_dash_line():
    line = Turtle()
    line.hideturtle()
    line.speed('fastest')
    line.color('white')
    line.penup()
    line.sety(300)
    line.pendown()
    line.pensize(10)

    pen_down = True
    y_pos = 285
    while y_pos > -300:
        y_pos -= 25
        line.sety(y_pos)

        if pen_down:
            line.penup()
            pen_down = False
        else:
            line.pendown()
            pen_down = True


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.color(BOARD_COLOR)
        self.penup()
        self.speed('fastest')
        self.sety(250)
        self.update_score()
        create_middle_dash_line()

    def update_score(self):
        self.clear()
        self.write(arg=f'{self.left_score}  {self.right_score}', align='center', font=('Helvetica', 50, 'normal'))
