from turtle import Turtle
import sound
 
class Control:
    def __init__(self, snake, score):
        self.snake = snake
        self.score = score
        self.setup_buttons()
    def setup_buttons(self):
        self.button(
        pen_color = "Dark Gray",
        color = "Light Gray",
        button_coordinates = (150, -500),
        button_width = 150,
        button_height = 100,
        word_color = "white",
        the_word = "►",
        word_coordinates = (225 + 5, -450 - 50),
        word_font = ("Arial", 24, "bold")
        )
        #زر لضغط Down
        self.button(
        pen_color = "Dark Gray",
        color = "Light Gray",
        button_coordinates = (0 - 40 , -500),
        button_width = 150,
        button_height = 100,
        word_color = "white",
        the_word = "▼",
        word_coordinates = (35, -500 + 5),
        word_font = ("Arial", 18, "bold")
        )
        #زر لضغط Left
        self.button(
        pen_color = "Dark Gray",
        color = "Light Gray",
        button_coordinates = (-190 - 40, -500),
        button_width = 150,
        button_height = 100,
        word_color = "white",
        the_word = "◄",
        word_coordinates = (-150 - 5, -500),
        word_font = ("Arial", 25, "bold")
        )
        #زر لضغط اعلى
        self.button(
        pen_color = "Dark Gray",
        color = "Light Gray",
        button_coordinates = (0 - 40, -360),
        button_width = 150,
        button_height = 100,
        word_color = "white",
        the_word = "▲",
        word_coordinates = (35, -360),
        word_font = ("Arial", 25, "bold")
        )
    
    def button(self, pen_color, color, button_coordinates, button_width, button_height, word_color, the_word, word_coordinates, word_font):  
        drawer = Turtle()  
        drawer.hideturtle()  
        drawer.color(pen_color, color)  
        #نوجه لمكان يلي رح نرسم فيه الزر  
        drawer.penup()  
        drawer.goto(button_coordinates)  
        drawer.pendown()  
        drawer.pensize(5)  
        drawer.begin_fill()  
        for _ in range(2):  
            drawer.forward(button_width)  
            drawer.circle(15, 90)  
            drawer.forward(button_height)  
            drawer.circle(15, 90)  
        drawer.end_fill()  
        #نكتبة كلمة داخل الزر  
        drawer.color(word_color)  
        drawer.penup()  
        drawer.goto(word_coordinates)  
        drawer.pendown()  
        drawer.write(the_word, align="center", font=word_font)  
    def check_click(self, x, y):      
        if (x >= 150  and x <= 300 + 100) and (y >= -500 and y <= -400 + 50):  
            self.snake.right()
            if not self.score.game_over:
                sound.play_click()
        elif (x >= (-190 -40) - 50 and x <= - 80 ) and (y >= - 500 and y <= -400 + 50):  
            self.snake.left()  
            if not self.score.game_over:
                sound.play_click()
        elif (x >= (0 - 40) - 40  and x <= 110 + 10) and (y >= -500 and y <=-400 + 20):  
            self.snake.down() 
            if not self.score.game_over:
                sound.play_click() 
        elif (x >= (0 - 40) - 40 and x <= 110 + 50) and (y > -360 and y <= - 260 + 60):  
            self.snake.up()  
            if not self.score.game_over:
                sound.play_click()
    
    
 