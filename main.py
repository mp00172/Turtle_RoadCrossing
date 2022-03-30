from turtle import Screen
from player import Player, Blood
from scoreboard import Scoreboard
from cars import Car
from graphics import *
from tkinter import messagebox

screen = Screen()
screen.colormode(255)
screen.title("Turtle Road Crossing")
screen.bgcolor(BACKGROUND_COLOR)
screen.setup(width=SCREEN_SIZE_X, height=SCREEN_SIZE_Y)
screen.tracer(0)
screen.listen()

graphics = Graphics()
scoreboard = Scoreboard()

messagebox.showinfo(title="Turtle Road Crossing", message="Welcome! :)\n"
														  "\n"
														  "Move the turtle using UP Arrow key and help it cross the road.\n"
														  "Turtle can only move forward.\n"
														  "\n"
														  "Good luck, and watch out for the cars!")

player = Player()
blood = Blood()
screen.onkey(key="Up", fun=player.move)

car_list = []


def create_cars():
	for i in range(5):
		car = Car()
		car_list.append(car)


def collision(p, c):
	if p.distance(c) <= 20:
		return True
	return False


program_running = True
match_running = True

while program_running:

	create_cars()
	while match_running:

		for car in car_list:
			car.move()
		screen.update()

		for car in car_list:
			if collision(player, car):
				blood.draw(player.xcor() - 10, player.ycor() + 10)
				screen.update()
				match_running = False

		if player.reached_finish():
			scoreboard.level_up()
			player.move_to_start()
			for i in range(2):
				car = Car()
				car_list.append(car)
			if scoreboard.current_level % 5 == 0:
				for car in car_list:
					car.car_speed += 1

	if scoreboard.current_level > scoreboard.highscore:
		scoreboard.set_highscore()

	play_again = messagebox.askyesno(title="Game over.", message=f"OUCH!\n"
																 "\n"
																 f"You've reached Level {scoreboard.current_level}.\n"
																 f"Highscore: {scoreboard.highscore}\n"
																 "\n"
																 "Play again?")

	if play_again:
		match_running = True
		for car in car_list:
			car.cclear()
		car_list = []
		blood.cclear()
		player.move_to_start()
		scoreboard.reset_current_level()

	else:
		program_running = False

messagebox.showinfo(title="Goodbye!", message="Thank you for playing! :)")
screen.bye()
