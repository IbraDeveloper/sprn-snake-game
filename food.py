from turtle import Turtle
import random
 

class Food(Turtle):
    def __init__(self, color_food, shape_food):
        super().__init__()
        self.shape(shape_food)
        self.color(color_food)
        self.penup()
        self.shapesize(0.9, 0.9)
        self.appear()
    def appear(self):
        random_x = random.randint(-460, 460)
        random_y = random.randint(-140, 740)
        self.goto(random_x, random_y)
        
 