#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

BLACK = 0
BLUE = 1
GREEN = 2
YELLOW = 3
RED = 4
WHITE = 5
BROWN = 6

black_hsv = [0, 10, 0, 10, 0, 10]
blue_hsv = [0, 10, 0, 10, 0, 10]
green_hsv = [0, 10, 0, 10, 0, 10]
yellow_hsv = [0, 10, 0, 10, 0, 10]
red_hsv = [0, 10, 0, 10, 0, 10]
white_hsv = [0, 10, 0, 10, 0, 10]
brown_hsv = [0, 10, 0, 10, 0, 10]

ev3 = EV3Brick()
speed = 100
angle_b = 60
angle_c = 90
motor_b = Motor(Port.B, Direction.COUNTERCLOCKWISE, [8, 30])
motor_c = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 39])
color_sensor = ColorSensor(Port.S3)

def run_motor(motor, angle):
	motor.run_target(speed, angle)
	wait(500)

def conv_rgb2hsv(rgb):
	pass
	return

def detect_color():
	rgb = color_sensor.rgb()
	hsv = conv_rgb2hsv(rgb)
	if (black[0] <= hsv[0] and black[1] >= hsv[0])
							and (black[2] <= hsv[1] and black[3] >= hsv[1])
												and (black[4] <= hsv[2] and black[5] >= hsv[2]):
		return BLACK

# i = 0
# ev3.speaker.beep()
# while i < 7:
# 	run_motor(motor_b, angle_b)
# 	run_motor(motor_c, angle_c)
# 	run_motor(motor_b, 0)
	
# 	ev3.screen.print(detect_color())

# 	run_motor(motor_b, angle_b)
# 	run_motor(motor_c, 0)
# 	run_motor(motor_b, 0)
# 	ev3.speaker.beep()
# 	wait(5000)

# 	i += 1

# i = 0
# while i < 3:
# 	ev3.speaker.beep()
# 	wait(500)
# 	i += 1








# run_motor(motor_b, angle)
# run_motor(motor_c, angle)
# run_motor(motor_b, 10)

print(Color.RED)
print(type(Color.RED))
rgb = color_sensor.rgb()
print(rgb)
print(type(rgb))

possible_colors = [Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW]
i = 0
ev3.speaker.beep()
while True:
	color = color_sensor.color()
	ambient = color_sensor.ambient()
	reflection = color_sensor.reflection()
	rgb = color_sensor.rgb()
	ev3.screen.print(color)
	ev3.screen.print(ambient)
	ev3.screen.print(reflection)
	ev3.screen.print(rgb)
	ev3.screen.print(i)
	i += 1
	wait(1000)
	# if color in possible_colors:
	# 	ev3.screen.print(color)
	# 	ev3.screen.print(i)
	# 	i += 1
	# 	wait(2000)