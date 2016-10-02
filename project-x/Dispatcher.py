#!/usr/bin/python
# coding=utf-8
from time import gmtime, strftime

class Dispatcher(object):

    tempIn, tempOut, ledRed, ledGreen = None, None, None, None
    DEBUG = False

    def __init__(self, tempIn, tempOut, ledRed, ledGreen, lcd, windowOpen, windowClose, debug = False):
        self.tempIn = tempIn
        self.tempOut = tempOut
        self.ledRed = ledRed
        self.ledGreen = ledGreen
        self.lcd    = lcd
        self.windowOpen = windowOpen
        self.windowClose = windowClose
        self.DEBUG = debug

    def main(self):
        self.debug("################### %s " % strftime("%H:%M:%S", gmtime()))
        self.tempIn.readTemp()
        self.tempOut.readTemp()

        if self.tempIn.hasSensorReadError or self.tempOut.hasSensorReadError:
            self.visualizeAlert(True)
            return self

        self.visualizeAlert(False) # everything ok

        # print to lcd
        self.lcd.main('In:  %.1f C' % self.tempIn.temperature, 'Out: %.1f C' % self.tempOut.temperature)

        if self.tempIn.temperature > self.tempOut.temperature:
            self.windowOpen.connect()
        else:
            self.windowClose.connect()


    def visualizeAlert(self, type = False):
        if type:
            self.ledRed.on()
            self.ledGreen.off()
            return

        self.ledRed.off()
        self.ledGreen.on()

    def debug(self, msg):
        if self.DEBUG is False: return ''
        print msg



