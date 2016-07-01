
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_PIN = 14
Sensor_PIN = 15
GPIO.setup(Sensor_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

print "STRG+C to stop"

def ausgabeFunktion(null):

    GPIO.output(LED_PIN, GPIO.HIGH)

GPIO.add_event_detect(Sensor_PIN, GPIO.FALLING, callback=ausgabeFunktion, bouncetime=10)

try:
    while True:
        time.sleep(1)
        if GPIO.input(Sensor_PIN):
            GPIO.output(LED_PIN, GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()