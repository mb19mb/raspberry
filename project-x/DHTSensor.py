#!/usr/bin/python
# coding=utf-8

import Adafruit_DHT

class DHTSensor(object):

    allowedSensorTypes  = ['DHT11', 'DHT22']
    sensorType          = 'DHT11'
    pin                 = 14
    DEBUG               = False
    currentTemp         = None
    previousTemp        = -100.0
    hasSensorReadError  = False
    registerDelta       = 0.5
    hasDeltaChange      = False


    def __init__(self, pin, sensorType = "DHT11", debug = False):
        self.DEBUG = debug

        if pin is None:
            raise Exception('Pin required')

        if sensorType not in self.allowedSensorTypes:
            raise Exception('SensorType %s is not allowed' % sensorType)

        self.sensorType = Adafruit_DHT.DHT11
        if sensorType == 'DHT22': self.sensorType = Adafruit_DHT.DHT22

        self.pin = pin


    def read(self):
        h, temp = Adafruit_DHT.read_retry(self.sensorType, self.pin)

        if temp is not None:
            self.debug("DHT%s: Temp = %f°C"%(self.sensorType, temp))
            self.currentTemp = temp
            self.hasSensorReadError = False
            if abs(self.previousTemp - self.currentTemp) >= self.registerDelta:
                self.previousTemp = self.currentTemp
            print self.deltaChange()
        else:
            self.hasSensorReadError = True
            self.debug('DHT%s - Fehler beim Auslesen.' % self.sensorType)


    def deltaChange(self):
        return abs(self.previousTemp - self.currentTemp)


    def debug(self, msg):
        if self.DEBUG is False: return ''
        print msg

if __name__ == '__main__':
    import time

    try:
        d11 = DHTSensor(14, 'DHT11', True)
        # d12 = DHTSensor(15, 'DHT22', False)
        while True:
            d11.read()

            #d12.read()
            time.sleep(5)
    except KeyboardInterrupt:
        print "done"