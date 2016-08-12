#!/usr/bin/python

import RPi.GPIO as GPIO
import time

pin1 = 23 # red
pin2 = 24 # green

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1,GPIO.OUT)
GPIO.output(pin1, GPIO.LOW)

GPIO.setup(pin2,GPIO.OUT)
GPIO.output(pin2, GPIO.LOW)

duration = 0.2

for x in range(20):
    GPIO.output(pin1, GPIO.HIGH)
    GPIO.output(pin2, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(pin1, GPIO.LOW)
    GPIO.output(pin2, GPIO.LOW)
    time.sleep(duration)

GPIO.cleanup()
