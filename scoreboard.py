from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-270, 250)
        self.level = 1
        self.score()

    def score(self):
        self.write(f"Level:{self.level}", align="left", font=FONT)  # 白ㄘ喔~測試時都忘記在 main.py call class最好會出現拉

    def level_up(self):
        self.level += 1
        self.clear()
        self.score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

