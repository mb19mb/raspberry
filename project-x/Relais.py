#!/usr/bin/python
# coding=utf-8

import RPi.GPIO as GPIO
import time

class Relais(object):
    pin = 0
    delay = 5
    isConnectedThrough = False
    hasError = False

    def __init__(self, pin = 17, delay = 5):
        self.pin = pin
        self.delay = delay
        self.initGPIO()

    def initGPIO(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, False)

    def __del__(self):
         GPIO.cleanup()

    def connect(self):
        try:
            if self.isConnectedThrough: return # nothing to do

            self.isConnectedThrough = True    # set status flag
            GPIO.output(self.pin, True)     # connect through
            time.sleep(self.delay)          # wait n seconds
            GPIO.output(self.pin, False)    # stop circuit connection
            self.isConnectedThrough = False   # reset status flag
        except KeyboardInterrupt:
            raise
        except:
            GPIO.output(self.pin, False)
            self.hasError = True

if __name__ == '__main__':
    r = Relais()
    r.connect()