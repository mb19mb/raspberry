#!/usr/bin/python
# coding=utf-8

import RPi.GPIO as GPIO
import time

pin = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
state = False # means off
count = 0
try:
    while True:
        if GPIO.input(pin) == False:
            state = not state
            count +=1
            print "Button ist %s" % state
            print count

        time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()
