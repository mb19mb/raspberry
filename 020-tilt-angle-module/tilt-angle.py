#/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin = 14
GPIO.setup(pin, GPIO.IN)

print "STRG+C to stop"

def ausgabeFunktion(null):
    print("Signal erkannt")

GPIO.add_event_detect(pin, GPIO.FALLING, callback=ausgabeFunktion, bouncetime=100)

try:
    while True:
        time.sleep(.2)

except KeyboardInterrupt:
    GPIO.cleanup()