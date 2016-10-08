#!/usr/bin/python

import RPi.GPIO as GPIO
import time

class LED(object):

    pin = 23
    status = False # means "off"

    def __init__(self, pin = 23):
        self.pin = pin
        GPIO.setwarnings(False)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)


    def on(self):
        if self.status: return # nothing to do

        GPIO.output(self.pin, GPIO.HIGH)
        self.status = True # means 'on'

    def off(self):
        if not self.status: return # nothing to do
        GPIO.setmode(GPIO.BCM)
        GPIO.output(self.pin, GPIO.LOW)
        self.status = False # means 'off'


    def __del__(self):
        self.off()
        #GPIO.cleanup()



if __name__ == '__main__':

    delay = 2

    ledRed = LED(23)
    ledGreen = LED(24)

    ledRed.on()
    time.sleep(delay)
    ledRed.off()

    ledGreen.on()
    time.sleep(delay)
    ledGreen.off()
