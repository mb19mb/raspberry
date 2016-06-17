#!/usr/bin/python
# coding=utf-8

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pin = 23
GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
t = 0.05

def tuut(t):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(t)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(t)
try:
    while(True):
        max = 10
        for i in range(1,50):
            intval = i/(1000 * 1.0)
            tuut(intval)
            print intval
except KeyboardInterrupt:
    GPIO.cleanup()
