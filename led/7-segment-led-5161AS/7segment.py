#!/usr/bin/pyhton
# coding=utf-8

import RPi.GPIO as GPIO
import time


def init(pinList):
    GPIO.setmode(GPIO.BCM)
    for pin in pinList:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)


def switchOff(pinList):
    for pin in pinList:
        GPIO.output(pin, GPIO.LOW)


def switchOn(pinList):
    for pin in pinList:
        GPIO.output(pin, GPIO.HIGH)


delay = 1

pin1 = 14
pin2 = 15
pin3 = 18
pin4 = 23
pin5 = 24
pin6 = 25
pin7 = 8
pin8 = 7

pinList = [pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8]

init(pinList)

switchOn(pinList)
time.sleep(delay)
switchOff(pinList)


# count from 1...3
number1 = [pin3, pin5]
switchOn(number1)
time.sleep(delay)
switchOff(number1)

number2 = [pin6, pin5, pin8, pin1, pin2]
switchOn(number2)
time.sleep(delay)
switchOff(number2)

number3 = [pin6, pin5, pin8, pin3, pin2]
switchOn(number3)
time.sleep(delay)
switchOff(number3)

GPIO.cleanup()

