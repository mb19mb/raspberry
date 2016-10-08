#!/usr/bin/python
# coding=utf-8

import unittest
from mock import MagicMock
from DHTSensor import DHTSensor

class WindowTest(unittest.TestCase):

    def test_foo(self):
        tempIn = DHTSensor(17)
        tempOut = DHTSensor(18)

        """
        !!! very important !!! prevent real call of readFromSensor()!
        """
        tempIn.readFromSensor = MagicMock(return_value=0)
        tempOut.readFromSensor = MagicMock(return_value=0)

        tempIn.getTemperature = MagicMock(return_value=10)
        tempOut.getTemperature = MagicMock(return_value=20)

        print tempIn.readFromSensor()


if __name__ == '__main__':
    unittest.main()