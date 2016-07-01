#!/usr/bin/python
# coding=utf-8

import random, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

redPin      = 18
greenPin    = 15
bluePin     = 14

GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)

freq = 100

# init
pwmRed      = GPIO.PWM(redPin, freq)
pwmGreen    = GPIO.PWM(greenPin, freq)
pwmBlue     = GPIO.PWM(bluePin, freq)

pwmRed.start(0)
pwmGreen.start(0)
pwmBlue.start(0)

def ledColor(red, green, blue, delay):
    if red == 0 and green == 0 and blue == 0: return
    print (red,green,blue)
    pwmRed.ChangeDutyCycle(red)
    pwmGreen.ChangeDutyCycle(green)
    pwmBlue.ChangeDutyCycle(blue)

    time.sleep(delay)

    pwmRed.ChangeDutyCycle(0)
    pwmGreen.ChangeDutyCycle(0)
    pwmBlue.ChangeDutyCycle(0)

print "STRG+C to stop"

try:
    while True:
        for x in range(0,2):
            for y in range(0,2):
                for z in range(0,2):
                    for i in range(0,101):
                        ledColor((x*i),(y*i),(z*i),.1)
except KeyboardInterrupt:
        GPIO.cleanup()