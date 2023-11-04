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

V_MIN = 30
S_MIN = 35

red_h = [300, 360]
blue_h = [180, red_h[0] - 1]
green_h = [90, blue_h[0] - 1]
yellow_h = [30, green_h[0] - 1]
red_h_2 = [0, yellow_h[0] - 1]
# brown_hsv = [20, 1.5 * yellow_h[0], 60, 66, 45, 55]

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
	if hsv[2] < V_MIN:
		return BLACK
	if hsv[1] < S_MIN:
		return WHITE
	if hsv[0] >= blue_h[0] and hsv[0] <= blue_h[1]:
		return BLUE
	if hsv[0] >= green_h[0] and hsv[0] <= green_h[1]:
		return GREEN
	if hsv[0] >= yellow_h[0] and hsv[0] <= yellow_h[1]:
		# pass # либо желтый, либо коричневый
		return YELLOW
	if hsv[0] >= red_h[0] and hsv[0] <= red_h[1] or hsv[0] >= red_h_2[0] and hsv[0] <= red_h_2[1]:
		# pass # либо красный, либо коричневый
		return RED
	return -1

i = 0
ev3.speaker.beep()
while i < 7:
	run_motor(motor_b, angle_b)
	run_motor(motor_c, angle_c)
	run_motor(motor_b, 0)
	
	ev3.screen.print(detect_color())

	run_motor(motor_b, angle_b)
	run_motor(motor_c, 0)
	run_motor(motor_b, 0)
	ev3.speaker.beep()
	wait(5000)

	i += 1

i = 0
while i < 3:
	ev3.speaker.beep()
	wait(500)
	i += 1
