from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0) #shuts off initial animation, but now I need to update screen after paddle moves

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0)) #position = tuple(x,y)

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_on = True
while game_on:
    screen.update() #need to do it in a while loop or it won't move





screen.exitonclick()