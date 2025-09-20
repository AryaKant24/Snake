from turtle import Turtle
import random

class Food(Turtle):
        def __init__(self):
                super().__init__()
                self.penup()
                self.shape("circle")
                self.color("red")
                self.speed("fastest")
                self.goto(random.randint(-220,220), random.randint(-220,220))
                self.penup()
                self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
                self.refresh()

        def refresh(self):
                self.goto(random.randint(-220,220), random.randint(-220,220))