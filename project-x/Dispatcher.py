#!/usr/bin/python
# coding=utf-8

class Dispatcher(object):

    tempIn, tempOut, ledRed, ledGreen = None, None, None, None

    def __init__(self, tempIn, tempOut, ledRed, ledGreen, lcd):
        self.tempIn = tempIn
        self.tempOut = tempOut
        self.ledRed = ledRed
        self.ledGreen = ledGreen
        self.lcd    = lcd

    def main(self):
        self.tempIn.read()
        self.tempOut.read()

        if self.tempIn.hasSensorReadError or self.tempOut.hasSensorReadError:
            print "ERROR"
            self.ledRed.on()
            return self

        if self.tempIn.currentTemp > self.tempOut.currentTemp:
            self.ledRed.off()
            self.ledGreen.on()
        else:
            self.ledRed.on()
            self.ledGreen.off()

        # print to lcd
        self.lcd.main('In:  %.1f C' % self.tempIn.currentTemp, 'Out: %.1f C' % self.tempOut.currentTemp)
        print "------------------------"



