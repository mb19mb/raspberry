#!/usr/bin/python
# coding=utf-8

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin = 18
GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
print "CRTL+C to stop"
try:
    while True:
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()

