#!/usr/bin/python
# coding=utf-8

import RPi.GPIO as GPIO
import time

class TiltAngle(object):
    status = "off"
    vibPin = 14
    ledPin = 15

    def printOutput(self,null):
        print "Signal registered"
        #if self.status == "off":
        GPIO.output(self.ledPin, GPIO.HIGH)
        time.sleep(0.1)
        #    self.status = "on"
        #else:
        GPIO.output(self.ledPin, GPIO.LOW)

        #    self.status = "off"

    def run(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.vibPin, GPIO.IN)
        GPIO.setup(self.ledPin, GPIO.OUT)
        GPIO.output(self.ledPin, GPIO.LOW)
        GPIO.add_event_detect(self.vibPin, GPIO.FALLING, callback=self.printOutput, bouncetime=100)

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print "bye bye"
            GPIO.cleanup()


if __name__ == "__main__":
    ta = TiltAngle()
    ta.run()

