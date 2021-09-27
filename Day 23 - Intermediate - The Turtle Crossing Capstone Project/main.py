import random
from turtle import Screen, Turtle
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("The Turtle Crossing Capstone")
screen.tracer(0)  # Close animation

player = Player()
screen.listen()
screen.onkey(player.go_up, "Up")

scoreboard = Scoreboard()
car_manager = CarManager()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move_cars()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.reset_position()
        car_manager.level_up()
        scoreboard.increase_level()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()