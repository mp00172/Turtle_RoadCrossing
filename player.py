from turtle import Turtle
from config import *


class Player(Turtle):
	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.speed(0)
		self.penup()
		self.shape("turtle")
		self.color(TURTLE_COLOR)
		self.goto(x=0, y=-(SCREEN_SIZE_Y // 2) + 50)
		self.setheading(90)
		self.showturtle()

	def move(self):
		self.goto(x=0, y=self.ycor() + TURTLE_MOVE_STEP)

	def move_to_start(self):
		self.goto(x=0, y=-(SCREEN_SIZE_Y // 2) + 50)

	def reached_finish(self):
		if self.ycor() >= SCREEN_SIZE_Y // 2 - 40:
			return True
		return False

	def get_position(self):
		return self.position()


class Blood(Turtle):
	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.penup()
		self.speed(0)
		self.shape("circle")
		self.color(BLOOD_COLOR)
		self.shapesize(stretch_wid=2, stretch_len=2)

	def draw(self, x, y):
		self.goto(x, y)
		self.showturtle()

	def cclear(self):
		self.hideturtle()
