#!/usr/bin/python
# coding=utf-8

import random, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

redPin      = 18
greenPin    = 15

GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)

freq = 100

# init
pwmRed      = GPIO.PWM(redPin, freq)
pwmGreen    = GPIO.PWM(greenPin, freq)

pwmRed.start(0)
pwmGreen.start(0)

def ledColor(red, green, delay):
    if red == 0 and green == 0: return
    print (red,green)
    pwmRed.ChangeDutyCycle(red)
    pwmGreen.ChangeDutyCycle(green)

    time.sleep(delay)

    pwmRed.ChangeDutyCycle(0)
    pwmGreen.ChangeDutyCycle(0)

print "STRG+C to stop"

try:
    while True:
        for x in range(0,2):
            for y in range(0,2):
                for i in range(0,101):
                    ledColor((x*i),(y*i),.1)
except KeyboardInterrupt:
        GPIO.cleanup()