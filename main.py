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

black_hsv = [0, 360, 0, 100, 0, 30]
white_hsv = [0, 360, 0, 35, black_hsv[5] + 1, 100]
brown_hsv = [0, 10, 0, 10, 0, 10]
red_hsv_2 = [300, 360]
blue_hsv = [180, red_hsv_2[0] - 1, white_hsv[3] + 1, 100, black_hsv[5] + 1, 100]
green_hsv = [90, blue_hsv[0] - 1, white_hsv[3] + 1, 100, black_hsv[5] + 1, 100]
yellow_hsv = [30, green_hsv[0] - 1, white_hsv[3] + 1, 100, black_hsv[5] + 1, 100]
red_hsv = [0, yellow_hsv[0] - 1, white_hsv[3] + 1, 100, black_hsv[5] + 1, 100]

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
	r = rgb[0] / 100
	g = rgb[1] / 100
	b = rgb[2] / 100
	cmax = max(r, g, b)
	cmin = min(r, g, b)
	delta = cmax - cmin
	# ------------------------ H
	if delta == 0:
		h = 0
	elif cmax == r:
		h = 60 * ((g - b) / delta % 6)
	elif cmax == g:
		h = 60 * ((b - r) / delta + 2)
	else:
		h = 60 * ((r - g) / delta + 4)
	# ------------------------ S
	if cmax == 0:
		s = 0
	else:
		s = delta / cmax
	# ------------------------ V
	v = cmax
	return [int(round(h)), int(round(100 * s)), int(round(100 * v))]

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