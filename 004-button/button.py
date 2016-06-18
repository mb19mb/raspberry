#!/usr/bin/python
# coding=utf-8

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
vibPin=14
ledPin=15
GPIO.setup(vibPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, GPIO.LOW)

print "CTRL+C to stop"

def printOutput(null):
    print "Signal registered"
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(ledPin, GPIO.LOW)
        
GPIO.add_event_detect(vibPin, GPIO.FALLING, callback=printOutput, bouncetime=100)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()

