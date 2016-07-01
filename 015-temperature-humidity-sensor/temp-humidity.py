#!/usr/bin/python
# coding=utf-8

# Benoetigte Module werden importiert und eingerichtet
import RPi.GPIO as GPIO
import Adafruit_DHT
import time

sleeptime = 2

# Sensor should be set to Adafruit_DHT.DHT11, Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
DHTSensor = Adafruit_DHT.DHT11
#DHTSensor = Adafruit_DHT.AM2302

GPIO_Pin = 15

print('STRG +C to stop')

try:
    while(1):

        Luftfeuchte, Temperatur = Adafruit_DHT.read_retry(DHTSensor, GPIO_Pin)

        print("-----------------------------------------------------------------")
        if Luftfeuchte is not None and Temperatur is not None:
            print('Temperatur = {0:0.1f}°C  | rel. Luftfeuchtigkeit = {1:0.1f}%'.format(Temperatur, Luftfeuchte))
        else:
            print('Fehler beim Auslesen - Bitte warten auf nächsten Versuch!')
        print("-----------------------------------------------------------------")
        time.sleep(sleeptime)
except KeyboardInterrupt:
    GPIO.cleanup()