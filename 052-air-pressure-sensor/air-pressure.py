#!/usr/bin/python
# coding=utf-8

import Adafruit_BMP.BMP085 as BMP085
import time
import RPi.GPIO as GPIO

delay = 5
# init sensor
try:
    BMPSensor = BMP085.BMP085()
except IOError:
    print("FAIL!")
    while(True):
        time.sleep(delay)
except KeyboardInterrupt:
    GPIO.cleanup()

try:
    while(True):
        print("------------------------------")
        print('Temperatur = {0:0.2f}°C'.format(BMPSensor.read_temperature()))
        print('Luftdruck = {0:0.2f}hPa'.format(BMPSensor.read_pressure()/100))
        print('Meereshöhe = {0:0.2f}m'.format(BMPSensor.read_altitude()))
        print("------------------------------")
        time.sleep(delay)
except KeyboardInterrupt:
    GPIO.cleanup()