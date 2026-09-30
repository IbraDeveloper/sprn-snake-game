from turtle import Screen, Turtle
from mainmenu import MainMenu
from snake import Snake
from control import Control
from food import Food
from scoreboard import Scoreboard
import sound
import time


window = Screen()
window.setup(width=1000, height=1000)

snake = None
foods = []
control = None
score = None
def start_game():
    window.bgcolor("black")
    #رسم حدود اللعبة
    window.tracer(0)
    border = Turtle()
    border.hideturtle()
    border.color("darkgreen")
    border.pensize(20)
    border.penup()
    border.goto(-500, -200)
    border.pendown()
    for _ in range(2):
        border.forward(1000)
        border.circle(15, 90)
        border.forward(1000)
        border.circle(15, 90)
    window.update()
    global snake, control, score
    snake = Snake()
    score = Scoreboard(window)
    control = Control(snake, score)
    window.tracer(0)
    window.update()
    
    window.listen()
    window.onscreenclick(control.check_click)
    window.onkey(snake.up, "Up")
    window.onkey(snake.down, "Down")
    window.onkey(snake.right, "Right")
    window.onkey(snake.left, "Left")
    
   
    apple = Food("red", "circle")
    foods.append(apple)
    MIN_SLEEP_TIME = 0.02
    game_on = True
    while game_on:
        snake.move()
        window.update()
        if snake.head.distance(foods[0]) < 15:
            foods[0].appear()
            snake.extend()
            snake.defalute_speed = max(MIN_SLEEP_TIME, snake.defalute_speed * 0.99)
            score.increase_score()
            score.clear()
            score.score_player()
            sound.play_eat()
        if snake.head.xcor() >= 500  or snake.head.xcor() <= -500 or snake.head.ycor() >= 800 + 10 or snake.head.ycor() <= -190:
            game_on = False
            score.show_game_over()
            sound.play_game_over()
        for segment in snake.turtles[:-1]:            
            if snake.head.distance(segment) < 10:
                game_on = False
                score.show_game_over()
                sound.play_game_over()  
                  
                                                

                
window.tracer(0)
mainmenu = MainMenu(window, start_game)
window.update()

window.listen()
window.onscreenclick(mainmenu.check_click)

window.mainloop()

#الحمدلله على اتمام هل مشروع الكبير بالنسبة لي
# رجعت للمشروع بعد تعلم التعامل مع الملفات وطورته بحيث خليته يحفظ اعلى نتيجة اعلى نتيجة