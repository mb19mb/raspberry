#!/usr/bin/python
# coding=utf-8

import RPi.GPIO as GPIO
import Adafruit_DHT
import time

sleeptime = 2

DHTSensor = Adafruit_DHT.DHT22

pin = 15

print('STRG +C to stop')

try:
    while(1):
        humidity, temp = Adafruit_DHT.read_retry(DHTSensor, pin)

        if temp is not None:
            #print('Temperatur = {0:0.1f}°C  | rel. Luftfeuchtigkeit = {1:0.1f}%'.format(temp, humidity))
            print "DHT22: Temp = {0:0.1f}°C".format(temp)
        else:
            print('DHT22 - Fehler beim Auslesen ')
        #print("-----------------------------------------------------------------")
        time.sleep(sleeptime)
except KeyboardInterrupt:
    GPIO.cleanup()