from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# class CarManager(Turtle):
#想像一下，一開始你把一台車做出來放在，attribute上，然而一開始的畫面你不適就不希望有任何車嗎，所有會動的車子也就是behavior都應該放在method裡~
class CarManager:
    def __init__(self):
        super().__init__()
        self.car_list = []

#這裡同樣，你有想過為何上面不 inherit class 嗎，因為這樣當你在 main.py call this class，初始設定的烏龜就會出現拉，所以記住，attribute = appearance；method = behavior
    def create_car(self):
        random_number = random.randrange(1, 6)
        if random_number == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, random.randrange(-250, 250, 10))
            new_car.setheading(180)
            self.car_list.append(new_car)

    def move_car(self):
        for car in self.car_list:
            car.forward(MOVE_INCREMENT)





# class CarManager(Turtle):
#
#     def __init__(self):
#         super().__init__()
#         self.shape("square")
#         self.shapesize(stretch_wid=1, stretch_len=2)
#         self.color(random.choice(COLORS))
#         self.penup()
#         self.goto(300, random.randrange(-250, 250, 10))
#         self.setheading(180)
#         self.car_list = []   #很棒!!!!有想到怎麼把所有object蒐集在一起
#
#     def cars(self):
#         self.forward(MOVE_INCREMENT)
#
#     def all_car(self):
#         for _ in range(random.randrange(0, 10)):
#             car_manager = CarManager()
#             self.car_list.append(car_manager)
#             for car in self.car_list:
#                 if car.xcor() > -320:
#                     car.cars()
