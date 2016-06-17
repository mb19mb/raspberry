#!/usr/bin/python
# coding=utf-8


import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)


GPIO_PIN = 23
GPIO.setup(GPIO_PIN, GPIO.OUT)

Frequenz = 500 #hz
pwm = GPIO.PWM(GPIO_PIN, Frequenz)
pwm.start(50)

def up(min = 50, max = 1000, sleep = 0.0001):
    for i in range(min, max):
        pwm.ChangeFrequency(i)
        time.sleep(sleep)

def down(min = 50 , max = 1000, sleep = 0.0001):

    for i in range(min, max):
        pwm.ChangeFrequency(max -i)
        time.sleep(sleep)
try:

    while(True):
        for i in range(0, 2):
            up(min = 100, max = 2000, sleep=0.005)
            down(min = 100, max = 2000, sleep=0.005)

        #for i in range(0, 20):
        #    up()
        #    down()

#    while(True):
#        print "Aktuelle Frequenz: %d" % Frequenz
#        Frequenz = input("Bitte neue Frequenz eingeben (50-5000):")
#        pwm.ChangeFrequency(Frequenz)

except KeyboardInterrupt:
    GPIO.cleanup()
