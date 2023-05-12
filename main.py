import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.03)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

# Detect when the Turtle collides with a Car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

# Detect when the Player has reached the other side
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.level_up()


screen.exitonclick()
