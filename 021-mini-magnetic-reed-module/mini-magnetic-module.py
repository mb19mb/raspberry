#!/usr/bin/python
# coding=utf-8

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin = 14
GPIO.setup(pin, GPIO.IN)

print "STRG+C to stop"

def ausgabeFunktion(null):
        print("Magnetfeld detektiert")

GPIO.add_event_detect(pin, GPIO.FALLING, callback=ausgabeFunktion, bouncetime=100)


try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
        GPIO.cleanup()