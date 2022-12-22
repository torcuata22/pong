from turtle import Screen, Turtle
from player import Player
from car_manager import Car
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)

screen.tracer(0) #shuts off initial animation, but now I need to update screen after paddle moves

player = Player()

scoreboard = Scoreboard()

car = Car()

screen.listen()
screen.onkeypress(player.go_forward, "Up")
screen.onkeypress(player.go_back, "Down")
# screen.onkeypress(l_paddle.go_up, "w")
# screen.onkeypress(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(0.1) #causes a delay every time ball moves, it slows it down or speeds up depending on how we change delay
    screen.update() #need to do it in a while loop or it won't move
    
    

screen.exitonclick()