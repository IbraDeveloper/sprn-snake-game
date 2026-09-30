from turtle import Turtle
import time

class Snake:
    def __init__(self):
        self.positions = [(-40, 0), (-20, 0), (0,0)]
        self.turtles = []
        self.creat_snake()
        self.head = self.turtles[-1]
        self.defalute_speed = 0.1
    def creat_snake(self):
        for i in range(len(self.positions)):
            new_turtle = Turtle(shape="square")
            new_turtle.penup()
            new_turtle.color("Green")
            new_turtle.goto(self.positions[i])
            
            self.turtles.append(new_turtle)
        self.turtles[-1].color("DarkGreen")
    def move(self):
        for i in range(len(self.turtles) -1):
            self.turtles[i].goto(self.turtles[i + 1].pos())
        self.head.forward(20)
        time.sleep(self.defalute_speed)
    def extend(self):
        new_segment = Turtle(shape="square")
        new_segment.color("Green")
        new_segment.penup()
        new_segment.goto(self.turtles[0].pos())
        self.turtles.insert(0, new_segment)
        self.positions.insert(0, new_segment)
        
        
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
        