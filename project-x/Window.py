#!/usr/bin/python
# coding=utf-8
from time import gmtime, strftime
from Logger import Logger
from DayInterval import DayInterval

class Window(object):
    WINDOW_OPEN     = "open"
    WINDOW_CLOSED   = "closed"

    windowStatus = WINDOW_CLOSED

    tempIn, tempOut = None, None
    logger = None
    dayInterval = None

    def main(self):
        # prüfe ob fenster geschlossen werden muss
        self.closeWindow()
        # prüfe ob fenster geoeffnet werden muss
        self.openWindow()


    def __init__(self, tempIn, tempOut):
        self.windowStatus   = self.WINDOW_CLOSED
        self.tempIn         = tempIn
        self.tempOut        = tempOut
        self.logger         = Logger()
        self.dayInterval    = DayInterval()


    """
    Open window if the following conditions are true
    """
    def openWindow(self):
        # check preconditions

        # 1: window already open?
        if self.windowStatus == self.WINDOW_OPEN: return # nothing to do

        # 2: max. window open time reached?

        # 3: temperature outside more than n degrees
        self.determineTemperature()
        if self.fetchTemperature("out") > -10: return # todo define constants

        # 4: temperature outside less than inside
        if not self.checkTemperature(): return # nothing to do

        # self.logger.write("open window")

    def closeWindow(self):
        pass

    """
    Partition one day in m pieces. In every partition the window should be open maximum n minutes
    """
    def checkWindowOpenIntervall(self):
        pass


    def determineTemperature(self):
        self.tempIn.readTemp()
        self.tempOut.readTemp()


    def fetchTemperature(self, type = "in"):
        if self.tempIn.hasSensorReadError or self.tempOut.hasSensorReadError:
            raise Exception("fail") # @todo ausnamhebehandlung

        if type == "in": return self.tempIn.temperature
        return self.tempOut.temperature


    """
    Temperature inside must be higher than outside
        -> if it returns True, otherwhise False
    """
    def checkTemperature(self):
        if self.tempIn.hasSensorReadError or self.tempOut.hasSensorReadError:
            return False

        if self.tempIn.temperature > self.tempOut.temperature:
            return True

        return False



if __name__ == "__main__":
    w = Window(None, None)
    w.openWindow()