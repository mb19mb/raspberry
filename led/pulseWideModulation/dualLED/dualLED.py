#!/usr/bin/python

import RPi.GPIO as GPIO
import time, sys, signal

class Timer(object):
    def killAfterTime(self, sec):
        signal.signal(signal.SIGALRM, self.handler)
        signal.alarm(sec)

    def handler(self, *args):
        self.p1.stop()
        self.p2.stop()
        GPIO.cleanup()
        sys.exit()

    def disable(self):
        signal.alarm(0)

    def setPcm(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
        

def main():
    try:
        while True:
            for i in range(tRange):
                p1.ChangeDutyCycle(i)
                p2.ChangeDutyCycle(tRange-i)
                time.sleep(sleep)
            for i in range(tRange):
                p1.ChangeDutyCycle(tRange-i)
                p2.ChangeDutyCycle(i)
                time.sleep(sleep)
			
    except KeyboardInterrupt:
	    pass

    p1.stop()
    p2.stop()
    GPIO.cleanup()

if __name__ == "__main__":

    pin1 = 18
    pin2 = 17

    sleep = 0.01
    tRange = 50 #min 0 max 100
    maxRunTime = 15 # in seconds
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin1,GPIO.OUT)
    GPIO.output(pin1, GPIO.LOW)

    GPIO.setup(pin2,GPIO.OUT)
    GPIO.output(pin2, GPIO.LOW)

    p1 = GPIO.PWM(pin1,50)
    p1.start(0)

    p2 = GPIO.PWM(pin2,50)
    p2.start(0)

    timer = Timer()
    timer.setPcm(p1,p2)
    timer.killAfterTime(maxRunTime)
    main()

