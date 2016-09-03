#!/usr/bin/python
# coding=utf-8

import RPi.GPIO as GPIO
import Adafruit_DHT
import time

class HumidityMeasure(object):
    def __init__(self, pin):
        self.pin = pin

    def readData(self):
        try:
            successful  = False
            sleeptime   = 3
            humidity    = 0.0
            temp        = 0.0
            retry       = 0

            while(not successful and retry < 5):
                humidity, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, self.pin)

                if humidity is not None and temp is not None:
                    successful = True

                retry +=1
                time.sleep(sleeptime)

            return [temp, humidity]

        except KeyboardInterrupt:
            GPIO.cleanup()

if __name__ == "__main__":
    hm = HumidityMeasure(18)
    print hm.read()
