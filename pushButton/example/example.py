#!/usr/bin/python
# coding=utf-8

import RPi.GPIO as GPIO
import time

pin = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(pin) == False:
            print "pressed"
        else:
            print "not pressed"
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
