from turtle import Turtle

class MainMenu(Turtle):
    def __init__(self, window, start_game):
        super().__init__()
        self.hideturtle()
        self.color("lime", "dark gray")
        self.pensize(7)
        self.penup()
        self.start_game = start_game
        self.window = window
        self.window.bgcolor("burlywood")
        self.name_game()
        self.create_button()
    def name_game(self):
        self.goto(0, 200)
        self.color("forestgreen")
        self.write("SNAKE GAME", align="center", font=("arial", 25, "bold"))
    def create_button(self):
       self.goto(-100, -30)
       #يبدا تحديد الشكل اللي هيطليه بلون
       self.window.tracer(0)
       self.color("lime", "dark gray")
       self.pendown()
       self.begin_fill()
       #رسم اطار الشكل
       for _ in range(2):
           self.forward(250 - 15)
           self.circle(15, 90)
           self.forward(60 - 15)
           self.circle(15, 90)
       #نهاية تحديد الشكل وملء الشكل
       self.end_fill()
       #كتابة كلمة START في منتصف الزر
       self.color("white")
       self.penup()
       self.goto(15, -25)
       self.write("START", align="center", font=("arial", 10, "bold"))
    def check_click(self, x, y):
       if (x >= -130 and x <= 130) and (y >= - 35 and y <= 35):
           self.clear()
           self.start_game()


       
       