#!/usr/bin/pyhton
# coding=utf-8

import glob, time
from time import sleep
import RPi.GPIO as GPIO

pin = 8
sleeptime = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# init
print "init the sensors"

baseDir = '/sys/bus/w1/devices/'
while True:
    try:
        deviceFolder = glob.glob(baseDir + '28*')[0]
        break
    except IndexError:
        sleep(0.5)
        continue

deviceFile = deviceFolder + '/w1_slave'

def measureTemp():
    f = open(deviceFile, 'r')
    lines = f.readlines()
    f.close()
    return lines

# initial temp measure
measureTemp()

def getTemp():
    lines = measureTemp()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = measureTemp()

    equalsPos = lines[1].find('t=')
    if equalsPos != -1:
        tempStr = lines[1][equalsPos+2:]
        tempC   = float(tempStr) / 1000.0
        return tempC


# main
try:
    while True:
        print '>---------------------<'
        print 'Temperatur= ', getTemp(), ' °C'
        time.sleep(sleeptime)
except KeyboardInterrupt:
    GPIO.cleanup()