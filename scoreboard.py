from turtle import Turtle
from config import *


class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.current_level = 1
		self.highscore = 1
		self.hideturtle()
		self.penup()
		self.color(TURTLE_COLOR)
		self.goto(x=-(SCREEN_SIZE_X // 2) + 30, y=SCREEN_SIZE_Y // 2 - 50)
		self.write(f"Level: {self.current_level}", font=SCOREBOARD_FONT)

	def level_up(self):
		self.current_level += 1
		self.clear()
		self.write(f"Level: {self.current_level}", font=SCOREBOARD_FONT)

	def set_highscore(self):
		self.highscore = self.current_level

	def reset_current_level(self):
		self.current_level = 1
		self.clear()
		self.write(f"Level: {self.current_level}", font=SCOREBOARD_FONT)

