
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
delayTime = 1

pin = 25
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, False)

print "STRG+C to stop"

try:
    while True:
        print "on"
        GPIO.output(pin, True) # NO kurzgeschlossen
        time.sleep(delayTime)
        print "off"
        GPIO.output(pin, False) # NC kurzgeschlossen
        time.sleep(delayTime)
except KeyboardInterrupt:
        GPIO.cleanup()