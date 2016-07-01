
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin = 14
GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

delay = .2

print "STRG+C to stop"

try:
    while True:
        if GPIO.input(pin) == True:
            print "auf linie"
        else:
            print "ausserhalb linie"
        print "---------------------------------------"

        time.sleep(delay)

except KeyboardInterrupt:
        GPIO.cleanup()