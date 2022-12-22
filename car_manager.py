from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(50,50)
        self.x_move = 5
        self.shapesize(stretch_len=2, stretch_wid=1)

        # self.y_move = 10
        # self.move_speed = 0.1
        

    # def move(self): #increases in x and y corrd
    #     new_x = self.xcor() + self.x_move 
    #     new_y = self.ycor() + self.y_move
    #     self.goto(new_x, new_y)

    
    # def bounce_y(self): 
    #     self.y_move *= -1  #for ball to bounce, y needs to reverse direction

    
    # def bounce_x(self): 
    #     self.x_move *= -1  #for ball to bounce off the paddle, x needs to reverse direction
    #     self.move_speed *= 0.9 #this is the delay time for sleep(), the lower it goes, the faster the ball moves
        


    # def reset_position(self):
    #     self.goto(0,0)
    #     self.bounce_x()
    