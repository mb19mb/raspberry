#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

segments = (14,15,18,23,24,25,8,7)

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)

digits = (22,10,9,11)

for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 0)

try:

    while True:
        for segment in segments:
            GPIO.output(segment, 1)
            time.sleep(0.5)

        time.sleep(2)

        for segment in segments:
            GPIO.output(segment, 0)

except KeyboardInterrupt:
    GPIO.cleanup()
