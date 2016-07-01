
import random, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

redLed = 15
greenLed = 14
blueLed = 18

GPIO.setup(redLed, GPIO.OUT)
GPIO.setup(greenLed, GPIO.OUT)
GPIO.setup(blueLed, GPIO.OUT)

Freq = 100 #Hz

red = GPIO.PWM(redLed, Freq)
green = GPIO.PWM(greenLed, Freq)
blue = GPIO.PWM(blueLed, Freq)
red.start(0)
green.start(0)
blue.start(0)


def ledColor(Rot, Gruen,Blau, pause):
    if Rot == 0 and Gruen == 0 and Blau == 0: return
    red.ChangeDutyCycle(Rot)
    green.ChangeDutyCycle(Gruen)
    blue.ChangeDutyCycle(Blau)
    time.sleep(pause)

    red.ChangeDutyCycle(0)
    green.ChangeDutyCycle(0)
    blue.ChangeDutyCycle(0)

print "STRG+C to stop"

try:
    while True:
        for x in range(0,2):
            for y in range(0,2):
                for z in range(0,2):
                    print (x,y,z)
                    for i in range(0,101):
                        ledColor((x*i),(y*i),(z*i),.02)

except KeyboardInterrupt:
        GPIO.cleanup()