from turtle import Turtle

STARTING_POSITION = (0,-280)
MOVE_DISTANCE = 10
FINISH_LINE= 280

class Player(Turtle):

    def __init__(self): #add position param so we can have more than one paddle in different position
        super().__init__() #don't forget SUPERCLASS, after adding this don't need to initialize instance
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)
        


    def go_forward(self):
        self.forward(MOVE_DISTANCE)
   

    def go_back(self):
         self.back(MOVE_DISTANCE)
   

    def go_right(self):
        self.right(90)
        # self.setheading(90)
        # self.forward
   

    def go_left(self): 
         self.left(90)

    def go_to_start(self):
        self.goto(STARTING_POSITION)
    
    def is_at_finish(self):
        if self.ycor() > 280:
            return True
        else:
            return False

    