from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.penup()
        self.end()
        self.setheading(90)

    def up(self):
        # new_ycor = self.ycor() + 20
        # self.goto(self.xcor(), new_ycor)
        self.forward(MOVE_DISTANCE)

    def again(self):
        if self.ycor() > FINISH_LINE_Y:
            self.end()
            return True

    def end(self):
        self.goto(STARTING_POSITION)




