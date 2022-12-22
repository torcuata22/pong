from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        

    def move(self): #increases in x and y corrd
        new_x = self.xcor() + self.x_move 
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    
    def bounce_y(self): 
        self.y_move *= -1  #for ball to bounce, y needs to reverse direction

    
    def bounce_x(self): 
        self.x_move *= -1  #for ball to bounce off the paddle, x needs to reverse direction
        
    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
    