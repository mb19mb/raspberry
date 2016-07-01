import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_PIN = 14
GPIO.setup(GPIO_PIN, GPIO.IN)

print "STRG+C to stop"

def ausgabeFunktion(null):
    print("Signal erkannt")

GPIO.add_event_detect(GPIO_PIN, GPIO.FALLING, callback=ausgabeFunktion, bouncetime=100)

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()