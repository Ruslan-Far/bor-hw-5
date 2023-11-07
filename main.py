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

V_MIN = 3
V_MIN_BROWN = 8
S_MIN = 50

red_h = [300, 360]
blue_h = [180, red_h[0] - 1]
green_h = [65, blue_h[0] - 1]
yellow_h = [25, green_h[0] - 1]
red_h_2 = [0, yellow_h[0] - 1]

ev3 = EV3Brick()
speed = 100
angle_b = 80
angle_c = 90
motor_b = Motor(Port.B, Direction.COUNTERCLOCKWISE, [8, 30])
motor_c = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 39])
color_sensor = ColorSensor(Port.S3)

def run_motor(motor, angle):
	motor.run_target(speed, angle)
	motor.reset_angle(0)
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
	ev3.screen.print(hsv)
	if hsv[2] < V_MIN:
		return BLACK
	if hsv[1] < S_MIN:
		return WHITE
	if hsv[0] >= blue_h[0] and hsv[0] <= blue_h[1]:
		return BLUE
	if hsv[0] >= green_h[0] and hsv[0] <= green_h[1]:
		return GREEN
	if hsv[0] >= yellow_h[0] and hsv[0] <= yellow_h[1]:
		if hsv[2] < V_MIN_BROWN:
			return BROWN
		return YELLOW
	if hsv[0] >= red_h[0] and hsv[0] <= red_h[1]:
		return RED
	if hsv[0] >= red_h_2[0] and hsv[0] <= red_h_2[1]:
		if hsv[2] < V_MIN_BROWN:
			return BROWN
		return RED
	return -1

i = 0
repeats = 7
ev3.speaker.beep(1000, 700)
while i < repeats:
	run_motor(motor_b, angle_b)
	run_motor(motor_c, angle_c)
	run_motor(motor_b, -(angle_b + 3))
	
	wait(1000)
	ev3.screen.clear()
	ev3.screen.print(detect_color())

	run_motor(motor_b, angle_b + 3)
	run_motor(motor_c, -angle_c)
	run_motor(motor_b, -angle_b)

	if i + 1 != repeats:
		ev3.speaker.beep(600, 300)
		wait(5000)

	i += 1

i = 0
while i < 3:
	ev3.speaker.beep(300, 100)
	wait(500)
	i += 1




# run_motor(motor_b, 3)
# run_motor(motor_b, 0)
# run_motor(motor_c, -90)

# run_motor(motor_b, angle_b)
# run_motor(motor_c, -angle_c)
# run_motor(motor_b, -angle_b)
# run_motor(motor_b, 0)
# wait(10000)
# run_motor(motor_b, angle_b)
# run_motor(motor_c, -angle_c)
# run_motor(motor_b, 0)



# possible_colors = [Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW]
# i = 0
# ev3.speaker.beep()
# while True:
# 	color = color_sensor.color()
# 	# ambient = color_sensor.ambient()
# 	# reflection = color_sensor.reflection()
# 	# rgb = color_sensor.rgb()
# 	# ev3.screen.print(color)
# 	# ev3.screen.print(ambient)
# 	# ev3.screen.print(reflection)
# 	# ev3.screen.print(rgb)
# 	ev3.screen.print(detect_color())
# 	ev3.screen.print(i)
# 	i += 1
# 	wait(1000)
# 	ev3.screen.clear()
