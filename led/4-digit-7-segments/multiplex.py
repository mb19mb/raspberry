#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import characterMatrix as cm

class Multiplexer(object):
    # define associated pins to segments
    segA = 14
    segB = 15
    segC = 18
    segD = 23
    segE = 24
    segF = 25
    segG = 8
    segH = 7
    segments = [segA, segB, segC, segD, segE, segF, segG, segH]

    # define associated pins to digits
    dig1 = 10
    dig2 = 11
    dig3 = 9
    dig4 = 22
    digits = [dig4, dig3, dig2, dig1]

    displayTime = 0.0025

    """ init segment and digit pins"""
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.initPins(self.segments, GPIO.OUT, False)
        self.initPins(self.digits, GPIO.OUT, True)

    """ init segment and digit pins """
    def initPins(self, pinList = [], direction = 0, status = False):
        # set GPIO direction IN(1) or OUT(0) for every pin in list
        # set pin output True or False
        for pin in pinList:
            GPIO.setup(pin, direction)
            GPIO.output(pin, status)

    """ read user input and print it out to LED display"""
    def main(self):
        try:
            while True:
                try:
                    input = raw_input("Input:")
                    self.printWord(input)
                except KeyError:
                    print "unknown character"

        except KeyboardInterrupt:
            print "cleanup... bye"
            GPIO.cleanup()

    """
    iterates the word and print current + next 3 characters out to LED display
    """
    def printWord(self, word=''):
        w = [] # helper list, which includes the 4 characters of the word to display

        word = "   " + word # to start output on the right side of LED display, we prepend three spaces to the input.

        for l in range(0, len(word)):

            # get four characters from inputword
            w = word[l:l + 4]

            # if inputword is too short, we append 1 to 3 spaces at the end
            if len(w) < 2: w += ' '
            if len(w) < 3: w += ' '
            if len(w) < 4: w += ' '

            # print w with multiplex technique
            self.multiplex(w)

    """
    display word with 4 character
        exact one character is shown at one time
        we just switch beetween digit1 to digit4 as fast as human eyes won't recognise the change
    """
    def multiplex(self, w, timePerChar = 1):
        # calculate number of iterations, based on the timePerChar parameter
        iterCount = int(timePerChar / (4 * self.displayTime))
        for r in range(0, iterCount):
            for n in range(0, 4):
                self.printChar(w[n], self.digits[n], self.displayTime) # display the nthd char on the nthd digit

    """ display char on digit for delay seconds"""
    def printChar(self, char, digit, delay = 0.0025):
        # digit on
        GPIO.output(digit, False)

        # print char
        charIndex = cm.characterMatrix[char.upper()]
        for index in range(0, len(self.segments)):
            segment = self.segments[index]
            segmentStatus = charIndex[index]
            GPIO.output(segment, segmentStatus)

        time.sleep(delay)

        # digit off
        GPIO.output(digit, True)


if __name__ == "__main__":
    m = Multiplexer()
    m.main()
