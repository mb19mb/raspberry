#!/usr/bin/python
# coding=utf-8

import RPi.GPIO as GPIO
import time

pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)
GPIO.output(pin, GPIO.LOW)

p = GPIO.PWM(pin,50)
p.start(0)
try:
    while True:
        for i in range(100):
            p.ChangeDutyCycle(i)
            time.sleep(0.02)
        for i in range(100):
            p.ChangeDutyCycle(100-i)
            time.sleep(0.02)
			
except KeyboardInterrupt:
	pass

p.stop()
GPIO.cleanup()

