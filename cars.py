from config import *
from turtle import Turtle
import random


class Car(Turtle):
	def __init__(self):
		super().__init__()
		self.car_speed = random.randint(STARTING_CAR_SPEED[0], STARTING_CAR_SPEED[1])
		self.hideturtle()
		self.penup()
		self.shape("square")
		self.shapesize(stretch_wid=1, stretch_len=3)
		self.color(random.choice(CAR_COLORS))
		self.goto(x=-(SCREEN_SIZE_X // 2) - random.randint(100, 150), y=random.randint(-(SCREEN_SIZE_Y // 2) + 120, SCREEN_SIZE_Y // 2 - 120))
		self.showturtle()

	def move(self):
		if self.xcor() > SCREEN_SIZE_X // 2 + 100:
			self.goto(x=-(SCREEN_SIZE_X // 2) - random.randint(100, 150),
					  y=random.randint(-(SCREEN_SIZE_Y // 2) + 100, SCREEN_SIZE_Y // 2 - 100))
		else:
			self.goto(x=self.xcor() + self.car_speed, y=self.ycor())

	def cclear(self):
		self.hideturtle()
		self.clear()