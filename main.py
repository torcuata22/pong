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
screen.onkeypress(player.go_right, "Right")
screen.onkeypress(player.go_left, "Left")

game_on = True
while game_on:
    time.sleep(0.1) 
    screen.update() 
    
    car_manager.create_car()
    car_manager.move_cars()

    #detect collision with a car:
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()

    #detect successful crossing, retun to start position and speed up cars
    #successful crossing (y=280):
    if player.is_at_finish():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


    

    

screen.exitonclick()