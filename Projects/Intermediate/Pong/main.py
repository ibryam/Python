from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


# Detect hit with a wall and bounce

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y() # bounce

# Detect hit with a paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

# Detect right paddle misses

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

# Detect right paddle misses
    if ball.xcor() < - 380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()