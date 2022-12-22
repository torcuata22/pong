from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.write("test",align="center", font=FONT )
        
    # #we need separate function to update scoreboard (outside init)
    # def update_scoreboard(self):
    #     self.clear() #before we update scoreboard so numbers don't print on top of each other
    #     self.goto(-150, 200)
    #     self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
    #     self.goto(150, 200)
    #     self.write(self.r_score, align="center", font=("Courier", 80, "normal"))


    # def lpoint(self):
    #     self.l_score += 1
    #     self.update_scoreboard()

    # def rpoint(self):
    #     self.r_score += 1
    #     self.update_scoreboard()