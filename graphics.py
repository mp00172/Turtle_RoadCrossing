from turtle import Turtle
from config import *


class Graphics(Turtle):
	def __init__(self):
		super().__init__()
		self.speed(0)
		self.hideturtle()
		self.color(GRASS_COLOR)
		self.penup()
		self.pensize(1)

		self.goto(x=-(SCREEN_SIZE_X // 2), y=-(SCREEN_SIZE_Y // 2))

		self.begin_fill()
		self.pendown()
		self.goto(x=SCREEN_SIZE_X // 2, y=-(SCREEN_SIZE_Y // 2))
		self.goto(x=SCREEN_SIZE_X // 2, y=-(SCREEN_SIZE_Y // 2) + 80)
		self.goto(x=-(SCREEN_SIZE_X // 2), y=-(SCREEN_SIZE_Y // 2) + 80)
		self.goto(x=-(SCREEN_SIZE_X // 2), y=-(SCREEN_SIZE_Y // 2))
		self.end_fill()
		self.penup()

		self.goto(x=-(SCREEN_SIZE_X // 2), y=-SCREEN_SIZE_Y // 2)

		self.begin_fill()
		self.pendown()
		self.goto(x=-(SCREEN_SIZE_X // 2), y=SCREEN_SIZE_Y // 2 - 80)
		self.goto(x=SCREEN_SIZE_X // 2, y=SCREEN_SIZE_Y // 2 - 80)
		self.goto(x=SCREEN_SIZE_X // 2, y=SCREEN_SIZE_Y // 2)
		self.goto(x=-(SCREEN_SIZE_X // 2), y=SCREEN_SIZE_Y // 2)
		self.end_fill()
		self.penup()

		self.pensize(10)
		self.color(LINE_COLOR)
		self.goto(x=-(SCREEN_SIZE_X // 2), y=-(SCREEN_SIZE_Y // 2) + 80)
		self.pendown()
		self.goto(x=SCREEN_SIZE_X // 2, y=-(SCREEN_SIZE_Y // 2) + 80)
		self.penup()

		self.goto(x=-(SCREEN_SIZE_X // 2), y=SCREEN_SIZE_Y // 2 - 80)
		self.pendown()
		self.goto(x=SCREEN_SIZE_X // 2, y=SCREEN_SIZE_Y // 2 - 80)
		self.penup()

