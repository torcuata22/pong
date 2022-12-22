from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0) #shuts off initial animation, but now I need to update screen after paddle moves


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0)) #position = tuple(x,y)

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(0.1) #causes a 0.1 second delay every time ball moves, so it slows it down
    screen.update() #need to do it in a while loop or it won't move
    ball.move()
    #detect collission with wall (top or bottom):
    if ball.ycor() > 280 or ball.ycor()< -280:
        ball.bounce_y()

    #detect collisions with paddles and make ball bounce off paddle:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect when paddle misses ball, keep score, and restart game in opposite direction:
    #right paddle miss: ball_x > 380:
    if ball.xcor() > 380:
        ball.reset_position()
        time.sleep(0.2)
     #left paddle miss: ball_x > 380:
    if ball.xcor() < -380:
        ball.reset_position()
        time.sleep(0.2)
    

screen.exitonclick()