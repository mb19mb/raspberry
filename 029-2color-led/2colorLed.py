#!/usr/bin/python
# coding utf-8

import random, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

ledRed = 14
ledGreen = 15

GPIO.setup(ledRed, GPIO.OUT)
GPIO.setup(ledGreen, GPIO.OUT)

freq = 100 #Hz

red = GPIO.PWM(ledRed, freq)
green = GPIO.PWM(ledGreen, freq)
red.start(0)
green.start(0)

def ledColor(r, g, pause):
    red.ChangeDutyCycle(r)
    green.ChangeDutyCycle(g)
    time.sleep(pause)
    red.ChangeDutyCycle(0)
    green.ChangeDutyCycle(0)


print "strg +c to stop"

try:
    while True:
        for x in range(0,5):
            for y in range(0,5):
                print (x,y)
                for i in range(0,5):
                    ledColor((x*i),(y*i),0.02)


except KeyboardInterrupt:
    GPIO.cleanup()