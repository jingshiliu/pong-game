from turtle import Turtle, Screen
from paddle import Paddle
from score import ScoreBoard
from ball import Ball



screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('My Pong Game')
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

score_board = ScoreBoard()

ball = Ball()

screen.listen()
screen.onkey(fun=left_paddle.up, key='w')
screen.onkey(fun=left_paddle.down, key='s')
screen.onkey(fun=right_paddle.up, key='i')
screen.onkey(fun=right_paddle.down, key='k')
screen.onkey(fun=screen.bye, key='p')


game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    if ball.xcor() < -400:
        score_board.right_score += 1
        score_board.update_score()
        ball.reset_pos()
    elif ball.xcor() > 400:
        score_board.left_score += 1
        score_board.update_score()
        ball.reset_pos()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()







