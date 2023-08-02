import turtle
import numpy as np

class Enemy:

    def __init__(self, length, speed):
        self.length = length
        self.speed = speed
    

    def spawn(self,pos):
        self.enemy = turtle.Turtle()
        self.enemy.penup()
        self.enemy.shape('circle')
        self.enemy.ht()
        self.enemy.color('green')
        self.enemy.shapesize(stretch_wid=self.length/2, stretch_len=self.length)
        self.enemy.degrees()
        self.enemy.setpos(pos)
        self.enemy.showturtle()

    

    def attack(self, cubey_pos_x, cubey_pos_y):
        self.enemy.setheading(self.enemy.towards(cubey_pos_x,cubey_pos_y))        
        self.enemy.forward(self.speed)

    def clone(self):
        return self.enemy.clone()

    def get_xcor(self):
        return self.enemy.xcor()

    def get_ycor(self):
        return self.enemy.ycor()

    def hide(self):
        self.enemy.hideturtle()

    def show(self):
        self.enemy.showturtle()

    def reset(self):
        self.enemy.reset()

    def goto(self, pos):
        self.enemy.goto(pos)


        

