#!/usr/bin/python
# coding=utf-8

import unittest
from mock import MagicMock
from DHTSensor import DHTSensor
from Window import Window

class WindowTest(unittest.TestCase):

    def preConfiguredTempObjects(self):
        tempIn = DHTSensor(17)
        tempOut = DHTSensor(18)

        """
        !!! very important !!! prevent real call of readFromSensor()!
        """
        tempIn.readFromSensor = MagicMock(return_value=0)
        tempOut.readFromSensor = MagicMock(return_value=0)

        tempIn.getTemperature = MagicMock(return_value=10)
        tempOut.getTemperature = MagicMock(return_value=20)
        return tempIn, tempOut


    def test_WindowOpen(self):
        tempIn, tempOut = self.preConfiguredTempObjects()

        w = Window(tempIn, tempOut)
        # TC: max. negative Außentemperatur ist unterschritten
        tempOut.getTemperature = MagicMock(return_value=-11)

        flag = w.checkTemperaturePreconditionsOpenWindow()
        self.assertEqual(-11, w.tempOut.getTemperature())
        self.assertEqual(False, flag)

        # TC: außen kälter als drinnen
        tempOut.getTemperature = MagicMock(return_value=10)
        tempIn.getTemperature = MagicMock(return_value=20)

        flag = w.checkTemperaturePreconditionsOpenWindow()
        self.assertEqual(10, w.tempOut.getTemperature())
        self.assertEqual(20, w.tempIn.getTemperature())
        self.assertEqual(True, flag)


    """
    """
    def test_checkWhetherWindowIsOpen(self):
        tempIn, tempOut = self.preConfiguredTempObjects()

        w = Window(tempIn, tempOut)
        w.windowStatus = w.WINDOW_OPEN
        self.assertEqual(True, w.checkWhetherWindowIsOpen())

        w.windowStatus = w.WINDOW_CLOSED
        self.assertEqual(False, w.checkWhetherWindowIsOpen())


if __name__ == '__main__':
    unittest.main()