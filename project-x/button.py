#!/usr/bin/python
# coding=utf-8

import RPi.GPIO as GPIO
import time
from motor import Motor

class Button(object):
    status = "off"
    vibPin = 25

    buttonPressed = False

    def printOutput(self,null):
        if self.buttonPressed:
            print "double execution prevented"
            return # prevent double execution, simple way- locking is still better
        self.buttonPressed = True
        print "Signal registered"
        Motor().demo()

        self.buttonPressed = False


    def run(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.vibPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.vibPin, GPIO.FALLING, callback=self.printOutput, bouncetime=100)
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print "bye bye"
            GPIO.cleanup()


if __name__ == "__main__":
    b = Button()
    b.run()

