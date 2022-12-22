from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position): #add position param so we can have more than one paddle in different position
        super().__init__() #don't forget SUPERCLASS, after adding this don't need to initialize instance
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1, outline=None) #turtle size is 20px, stretch is a multiplication factor to stretche it to desired size, not the new size
        self.goto(position)

   

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)