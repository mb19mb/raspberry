#!/usr/bin/python
# coding=utf-8

#import Adafruit_DHT
import unittest, time
from mock import MagicMock
from DHTSensor import DHTSensor

class DHTSensorTest(unittest.TestCase):
    def test_readTemp(self):
        thing = DHTSensor(17)
        thing.getTemperature = MagicMock(return_value=3)
        self.assertEqual(3, thing.getTemperature())


if __name__ == '__main__':
    unittest.main()