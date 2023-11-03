#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
speed = 100
angle = 90

motor_b = Motor(Port.B, Direction.COUNTERCLOCKWISE, [8, 30])
motor_c = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 39])

def run_motor(motor, angle):
	ev3.speaker.beep()
	motor.run_target(speed, angle)
	ev3.speaker.beep()

run_motor(motor_b, angle)
wait(2000)
run_motor(motor_c, angle)
wait(2000)
run_motor(motor_b, 0)
wait(5000)

run_motor(motor_b, angle)
wait(2000)
run_motor(motor_c, 0)
wait(2000)
run_motor(motor_b, 0)
