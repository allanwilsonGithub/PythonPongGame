from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Allan's Pong Game")
screen.tracer(0)

paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball((0, 0))
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")
screen.onkey(paddle_right.up, "o")
screen.onkey(paddle_right.down, "k")

game_is_on = True

while game_is_on:
    ball.move()
    time.sleep(0.1)
    screen.update()

    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.bounce_y()

    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect if left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()