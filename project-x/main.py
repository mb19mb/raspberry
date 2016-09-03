#!/usr/bin/python
# coding=utf-8

from DHTSensor import DHTSensor
from LED import LED
from Dispatcher import Dispatcher
from LCD import LCD
import RPi.GPIO as GPIO
import time

delay = 3 # in seconds
dht11Pin = 14
dht22Pin = 15

ledPinRed = 23
ledPinGreen = 24

d11 = DHTSensor(dht11Pin, 'DHT11', True)
d22 = DHTSensor(dht22Pin, 'DHT22', True)

ledRed = LED(ledPinRed)
ledGreen = LED(ledPinGreen)

lcd = LCD()

dispatcher = Dispatcher(d11, d22, ledRed, ledGreen, lcd)

try:

    while True:

        dispatcher.main()
        time.sleep(delay)

except KeyboardInterrupt:
    GPIO.cleanup()
    print "done"
finally:
    lcd.lcd_byte(0x01, lcd.LCD_CMD)



