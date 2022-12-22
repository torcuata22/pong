from turtle import Turtle

STARTING_POSITION = (0,-280)
MOVE_DISTANCE = 10
FINISH_LINE= 280

class Player(Turtle):

    def __init__(self): #add position param so we can have more than one paddle in different position
        super().__init__() #don't forget SUPERCLASS, after adding this don't need to initialize instance
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        


   

    def go_forward(self):
        self.forward(MOVE_DISTANCE)
    #     new_y = self.ycor() + 20
    #     self.goto(self.xcor(), new_y)

    def go_back(self):
         self.back(MOVE_DISTANCE)
    #     new_y = self.ycor() - 20
    #     self.goto(self.xcor(), new_y)