#!/usr/bin/python
# coding=utf-8

from DHTSensor import DHTSensor
from Button import Button
from LED import LED
from Dispatcher import Dispatcher
from LCD import LCD
from Relais import Relais
import RPi.GPIO as GPIO
import time


delay = 15 # in seconds

dht11Pin = 14
dht22Pin = 15

relaisPinOpen = 17
relaisPinClose = 27

ledPinRed = 23
ledPinGreen = 24

d11 = DHTSensor(dht11Pin, 'DHT11', True)
d22 = DHTSensor(dht22Pin, 'DHT22', True)

windowOpen = Relais(relaisPinOpen, 5)
windowClose = Relais(relaisPinClose, 5)

lcd = LCD()
ledRed = LED(ledPinRed)
ledGreen = LED(ledPinGreen)

dispatcher = Dispatcher(d11, d22, ledRed, ledGreen, lcd, windowOpen, windowClose, True)

#button = Button()
#button.run()

try:

    while True:
        dispatcher.main()
        time.sleep(delay)

except KeyboardInterrupt:
    print "done"
finally:
    lcd.lcd_byte(0x01, lcd.LCD_CMD)
    GPIO.cleanup()



