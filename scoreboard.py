from turtle import Turtle, Screen

class Scoreboard(Turtle):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.color("white")
        self.hideturtle()
        self.penup()
        self.highscore = self.get_highscore()
        self.score = 0
        self.game_over = False
        self.goto(0, 850)
        self.score_player()   
    def get_highscore(self):
        with open("data/highscore.txt", "r") as file:
            return int(file.read())
    def save_highscore(self):
        with open("data/highscore.txt", "w") as file:
            file.write(str(self.highscore))              
    def score_player(self):
        self.write(f"Score: {self.score}             Highscore: {self.highscore}", align="center", font=("arial", 13, "normal"))
    def show_game_over(self):
        self.game_over = True
        self.clear()
        self.window.bgcolor("darkred")
        self.goto(0,0)
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()
        self.write(f"--------Game over!--------\n\nFinally score: {self.score}\n\nHighscore: {self.highscore}", align="center", font=("arial", 18, "normal"))
    def increase_score(self):
        self.score += 1 
                
