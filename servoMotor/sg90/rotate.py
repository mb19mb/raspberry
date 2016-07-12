#!/usr/bin/python
# coding=utf-8

import RPi.GPIO as GPIO
import time


def position(degree = 0, freq = 50):
    if freq <= 0: freq = 50 # prevent DivByZero

    if degree == 0:  # Impulse length = 0.5ms
        return 0.05 / (1.0 / freq)
    if degree == 180:  # Impulse length = 2.5ms
        return 0.25 / (1.0 / freq)

    return 0.15 / ( 1.0 / freq) # neutral position -> Impulse length = 1.5ms


pin = 14
frequency = 50 # min: 1, max: 100
sleep = 0.25
degreeList = [180, -1, 0 , -1]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(pin, frequency)
pos = position(-1, frequency)
p.start(pos) # neutral position

try:
    while True:

        for i in degreeList:
            print i
            pos = position(i, frequency)
            p.ChangeDutyCycle(pos)
            time.sleep(sleep)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
