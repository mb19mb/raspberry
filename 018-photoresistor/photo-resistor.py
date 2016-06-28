#!/usr/bin/python
# coding=utf-8

####
### @todo ... messwerte sind FAIL
###

from Adafruit_ADS1x15 import ADS1x15
from time import sleep

import time, signal, sys, os, math
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

t = 1.5
uMax = 3300
ADS1115 = 0x01

gain = 2048
sps = 8
adc_channel = 0

adc = ADS1x15(ic=ADS1115)

try:
    while True:
        u = adc.readADCSingleEnded(adc_channel, gain, sps)


        r = 10000 * u/(uMax - u)
        print "Spannungswert: %d mv" %u
        print "Widerstand   : %d Ohm" % r
        print "---------------------------------------"

        time.sleep(t)

except KeyboardInterrupt:
        GPIO.cleanup()
