#!/usr/bin/python
# coding=utf-8

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

triggerPinOut = 17
echoPinIn = 27

sleeptime = 1

GPIO.setup(triggerPinOut, GPIO.OUT)
GPIO.setup(echoPinIn, GPIO.IN)
GPIO.output(triggerPinOut, False)

try:
    while True:
        GPIO.output(triggerPinOut, True)
        time.sleep(0.00001)
        GPIO.output(triggerPinOut, False)

        timeOn = time.time()
        while GPIO.input(echoPinIn) == 0:
            timeOn = time.time()

        while GPIO.input(echoPinIn) == 1:
            timeOff = time.time()

        duration = timeOff - timeOn

        distance = (duration * 34300) / 2

        if distance < 2 or (round(distance) > 300):
            print ("komma ma naeher ran, das is mir zu weit weg")
        else:
            distance = format(distance, '.2f')
            print ("Abstand ist"), distance, ("cm")

        time.sleep(sleeptime)

except KeyboardInterrupt:
    GPIO.cleanup()

