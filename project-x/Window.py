#!/usr/bin/python
# coding=utf-8
from time import gmtime, strftime
from Logger import Logger
from DayInterval import DayInterval

class Window(object):
    WINDOW_OPEN     = "open"
    WINDOW_CLOSED   = "closed"

    MAX_NEGATIVE_OUTSIDE_TEMPERATURE = -10

    windowStatus = WINDOW_CLOSED

    tempIn, tempOut = None, None
    logger = None
    dayInterval = None

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
        if self.checkWhetherWindowIsOpen(): return False

        if self.checkTemperaturePreconditionsOpenWindow():
            print "oeffne fenster"
            return

        print "fenster wird nicht geoeffnet"


    """
    """
    def checkTemperaturePreconditionsOpenWindow(self):
        # 2: max. window open time reached?

        # Eigentliche Temperaturabfrage
        # Temperatur abfragen
        self.determineTemperature()

        # check sensorerrors
        if self.tempIn.hasSensorReadError or self.tempOut.hasSensorReadError:
            return False

        # Max. negative Außentemperatur unterschritten? Fenster bleibt zu
        if self.fetchTemperature("out") <= self.MAX_NEGATIVE_OUTSIDE_TEMPERATURE: return False

        # Temperature inside must be higher than outside -> if it returns True, otherwhise False
        if self.tempOut.getTemperature() > self.tempIn.getTemperature():
            return False

        return True


    """
    """
    def checkWhetherWindowIsOpen(self):
        if self.windowStatus == self.WINDOW_OPEN: return True
        return False


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

        if type == "in": return self.tempIn.getTemperature()
        return self.tempOut.getTemperature()






if __name__ == "__main__":
    w = Window(None, None)
    w.openWindow()