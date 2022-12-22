from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        

    def move(self): #increases in x and y corrd
        new_x = self.xcor() + 10 #I can reduce this to 1 and it will make ball slower, too
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)