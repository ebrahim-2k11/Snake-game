from turtle import Turtle
import random


class Food(Turtle):
    
    #initializing the food
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(.3)
    
    #set it in a random place
    def random_place(self):
        x= random.randint(-385,385)
        y= random.randint(-385,385)
        self.goto(x,y)
####################################################
class Score(Turtle):

    #initializing the score
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.hideturtle()
        self.goto(-320,350)
        self.color("white")

    #display it
    def display_score(self):
        self.write(f"Score: {self.score}", align="center" ,font=("Arial",24,"normal"))

    #add to it
    def add_score(self):
        self.clear()
        self.score+=1

    #End the game    
    def game_over(self):
        self.goto(0,0)
        self.hideturtle()
        self.write(f"Game Over\nFinal Score: {self.score}",align="center" ,font=("Arial",24,"normal"))
        