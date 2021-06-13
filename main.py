import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()  #漏掉沒寫跑不動
screen.onkey(player.up, "Up")

time_sleep = 0.1
game_is_on = True
while game_is_on:
    time.sleep(time_sleep)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    for car in car_manager.car_list:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.again():
        scoreboard.level_up()
        time_sleep *= 0.7


screen.exitonclick()








