#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

segA = 14
segB = 15
segC = 18
segD = 23
segE = 24
segF = 25
segG = 8
segH = 7
segments = [segA, segB, segC, segD, segE, segF, segG, segH]

dig1 = 10
dig2 = 11
dig3 = 9
dig4 = 22

#digits = [dig1, dig2, dig3, dig4]
digits = [dig4, dig3, dig2, dig1]


characterMatrix = {
    "A": [1, 1, 1, 0, 1, 1, 1, 0],
    "B": [1, 1, 1, 1, 1, 1, 1, 0],
    "C": [1, 0, 0, 1, 1, 1, 0, 0],
    "D": [1, 1, 1, 1, 1, 1, 0, 1],
    "E": [1, 0, 0, 1, 1, 1, 1, 0],
    "F": [1, 0, 0, 0, 1, 1, 1, 0],
    "G": [1, 0, 1, 1, 1, 1, 1, 1],
    "H": [0, 1, 1, 0, 1, 1, 1, 0],
    "I": [0, 1, 1, 0, 0, 0, 0, 0],
    "J": [0, 0, 0, 0, 0, 0, 0, 1],

    "K": [0, 0, 0, 0, 0, 0, 0, 1],
    "L": [0, 0, 0, 1, 1, 1, 0, 0],
    "M": [0, 0, 0, 0, 0, 0, 0, 1],
    "N": [0, 0, 0, 0, 0, 0, 0, 1],
    "O": [1, 1, 1, 1, 1, 1, 0, 0],

    "P": [1, 1, 0, 0, 1, 1, 1, 0],
    "Q": [1, 1, 1, 1, 1, 1, 0, 1],
    "R": [0, 0, 0, 0, 0, 0, 0, 1],
    "S": [1, 0, 1, 1, 0, 1, 1, 1],
    "T": [0, 0, 0, 0, 0, 0, 0, 1],

    "U": [0, 1, 1, 1, 1, 1, 0, 0],
    "V": [0, 0, 0, 0, 0, 0, 0, 1],
    "W": [0, 0, 0, 0, 0, 0, 0, 1],
    "X": [0, 0, 0, 0, 0, 0, 0, 1],
    "Y": [0, 1, 1, 1, 0, 1, 1, 1],
    "Z": [1, 1, 0, 1, 1, 0, 1, 1],

    "0": [1, 1, 1, 1, 1, 1, 0, 0],
    "1": [0, 1, 1, 0, 0, 0, 0, 0],
    "2": [1, 1, 0, 1, 1, 0, 1, 0],
    "3": [1, 1, 1, 1, 0, 0, 1, 0],
    "4": [0, 1, 1, 0, 0, 1, 1, 0],
    "5": [1, 0, 1, 1, 0, 1, 1, 0],
    "6": [1, 0, 1, 1, 1, 1, 1, 0],
    "7": [1, 1, 1, 0, 0, 0, 0, 0],
    "8": [1, 1, 1, 1, 1, 1, 1, 0],
    "9": [1, 1, 1, 1, 0, 1, 1, 0],
    " ": [0, 0, 0, 0, 0, 0, 0, 0],
}

def printChar(char, digit, delay = 0.25):

    # digit on
    GPIO.output(digit, False)

    # print char
    charIndex = characterMatrix[char.upper()]
    for index in range(0, len(segments)):
        segment = segments[index]
        segmentStatus = charIndex[index]
        GPIO.output(segment, segmentStatus)

    time.sleep(delay)

    # digit off
    GPIO.output(digit, True)


def initPins(pinList, direction, status):
    for pin in pinList:
        GPIO.setup(pin, direction)
        GPIO.output(pin, status)


def multiplex2(c = '', dig = 1, delay = 0.0025):
    ############
    # digit on
    GPIO.output(dig, False)

    # print char
    charIndex = characterMatrix[c.upper()]
    for index in range(0, len(segments)):
        segment = segments[index]
        segmentStatus = charIndex[index]
        GPIO.output(segment, segmentStatus)

    # wait
    time.sleep(delay)

    # digit off
    GPIO.output(dig, True)


def printWord(word = ''):
    word = "   " + word
    w = []
    for l in range(0, len(word)):
        offset = 3
        if (l + 1 < len(word)): offset = 2
        if (l + 2 < len(word)): offset = 3
        if (l + 3 < len(word)): offset = 4

        w = word[l:l + offset]

        if len(w) < 2: w += ' '
        if len(w) < 3: w += ' '
        if len(w) < 4: w += ' '

        # multiplex
        for r in range(0,40):
            for i in range(0,4):
                multiplex2(w[i], digits[i])


initPins(segments, GPIO.OUT, False)
initPins(digits, GPIO.OUT, True)

#GPIO.output(22, 0)
#for c in 'abcdefghijklmnopqrstuvwxyz0123456789':
#    printChar(c)
#    time.sleep(0.1)

try:
    while True:
        try:
            input = raw_input("Input:")
            #printChar(input, dig2)
            printWord(input)
        except KeyError:
            print "unknown character"

except KeyboardInterrupt:
    GPIO.cleanup()

GPIO.cleanup()
