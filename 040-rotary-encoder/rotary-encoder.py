# coding=utf-8
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

clk     = 18
dt      = 15
button  = 14

counter = 0
direction   = True
clk_last    = 0
clk_current = 0
delay       = 0.01

GPIO.setup(clk, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(dt, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# init clk
clk_last = GPIO.input(clk)

def ausgabeFunktion(null):
    global counter

    clk_current = GPIO.input(clk)

    if clk_current != clk_last:

        if GPIO.input(dt) != clk_current:
            counter += 1
            direction = True;
        else:
            direction = False
            counter = counter - 1

        print "Drehung erkannt: "

        if direction:
            print "Drehrichtung: Im Uhrzeigersinn"
        else:
            print "Drehrichtung: Gegen den Uhrzeigersinn"

        print "Aktuelle Position: ", counter
        print "------------------------------"

def counterReset(null):
    global counter

    print "Position resettet!"
    print "------------------------------"
    counter = 0

GPIO.add_event_detect(clk, GPIO.BOTH, callback=ausgabeFunktion, bouncetime=50)
GPIO.add_event_detect(button, GPIO.FALLING, callback=counterReset, bouncetime=50)


print "STRG+C to stop"

try:
    while True:
        time.sleep(delay)

except KeyboardInterrupt:
        GPIO.cleanup()