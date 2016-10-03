#!/usr/bin/python
# coding=utf-8
from time import gmtime, strftime
from Logger import Logger
from DayInterval import DayInterval

class Window(object):
    WINDOW_OPEN = "open"
    WINDOW_CLOSED = "closed"

    windowStatus = WINDOW_CLOSED

    tempIn, tempOut = None, None
    logger = None
    dayInterval = None

    def __init__(self, tempIn, tempOut):
        self.windowStatus = self.WINDOW_CLOSED
        self.tempIn = tempIn
        self.tempOut = tempOut
        self.logger = Logger()
        self.dayInterval =  DayInterval()

    def openWindow(self):
        self.logger.write("open window")

    def closeWindow(self):
        pass

    """
    Partition one day in 4 pieces. In every partition the window should be open maximum n minutes
    """
    def checkWindowOpenIntervall(self):
        pass

    """
    Temperature inside must be higher than outside
        -> if it returns True, otherwhise False
    """
    def checkTemperature(self):
        self.tempIn.readTemp()
        self.tempOut.readTemp()

        if self.tempIn.hasSensorReadError or self.tempOut.hasSensorReadError:
            return False

        if self.tempIn.temperature > self.tempOut.temperature:
            return True

        return False



if __name__ == "__main__":
    w = Window(None, None)
    w.openWindow()