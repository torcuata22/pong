from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)

screen.tracer(0) #shuts off initial animation, but now I need to update screen after paddle moves

player = Player()

scoreboard = Scoreboard()

car_manager = CarManager()

screen.listen()
screen.onkey(player.go_forward, "Up")
screen.onkey(player.go_back, "Down")
# screen.onkeypress(l_paddle.go_up, "w")
# screen.onkeypress(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(0.1) 
    screen.update() 
    
    car_manager.create_car()
    car_manager.move_cars()
    

screen.exitonclick()