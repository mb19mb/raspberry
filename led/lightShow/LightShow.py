#!/usr/bin/python

import RPi.GPIO as GPIO
import time
#from Timer import Timer

class LightShow(object):

    #p1, p2, p3, p4, p5, p6 = None

    #all = []

    def __init__(self, p1, p2, p3, p4, p5, p6):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5
        self.p6 = p6
        self.all = [self.p1, self.p2, self.p3, self.p4, self.p5, self.p6]

        GPIO.setmode(GPIO.BCM)
        self.setup()


    def on(self, pinlist):
        for pin in pinlist:
            GPIO.output(pin, GPIO.HIGH)

    def off(self, pinlist):
        for pin in pinlist:
            GPIO.output(pin, GPIO.LOW)

    def gsleep(self, duration):
        time.sleep(duration)

    def setup(self):
        for pin in self.all:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

    def seqLeftToRight(self, repeat, t):
        self.off(self.all)
        for x in range(repeat):
            self.off(self.all)
            self.on([self.p1])

            self.gsleep(t)
            self.off(self.all)
            self.on([self.p2])

            self.gsleep(t)
            self.off(self.all)
            self.on([self.p3])

            self.gsleep(t)
            self.off(self.all)
            self.on([self.p4])

            self.gsleep(t)
            self.off(self.all)
            self.on([self.p5])

            self.gsleep(t)
            self.off(self.all)
            self.on([self.p6])

            self.gsleep(t)

            self.off(self.all)


    def seqRightToLeft(self, repeat, t):
        self.off(self.all)
        for x in range(repeat):
            self.off(self.all)
            self.on([self.p6])

            self.gsleep(t)
            self.off(self.all)
            self.on([self.p5])

            self.gsleep(t)
            self.off(self.all)
            self.on([self.p4])

            self.gsleep(t)
            self.off(self.all)
            self.on([self.p3])

            self.gsleep(t)
            self.off(self.all)
            self.on([self.p2])

            self.gsleep(t)
            self.off(self.all)
            self.on([self.p1])

            self.gsleep(t)

        self.off(self.all)


    def seqLeftToRightViceVersa(self, repeat, t):
        for x in range(repeat):
            self.seqLeftToRight(1,t)
            self.seqRightToLeft(1,t)

    def seqStropo(self, repeat, t):
        self.off(self.all)
        for x in range(repeat):
            self.off(self.all)
            self.gsleep(t)
            self.on(self.all)
            self.gsleep(t)

            self.off(self.all)


    def seqPWM(self, pins, frequency = 10, t = 0.02, r = 100):

        if r > 100: r = 100

        self.off(self.all)
        pwmList = []
        for pin in pins:
            pwm = GPIO.PWM(pin,frequency)
            pwmList.append(pwm)
            pwm.start(0)


        for i in range(100):
            for pwm in pwmList:
                pwm.ChangeDutyCycle(i)
                time.sleep(t)
        for i in range(100):
            for pwm in pwmList:
                pwm.ChangeDutyCycle(100-i)
                time.sleep(t)

        for pwm in pwmList:
            pwm.stop()

        self.off(self.all)


    def main(self):
        try:
            print "CTRL+C to stop"
            while (True):
                self.seqPWM([self.p1, self.p6])
                self.seqStropo(20, 0.04)
                self.seqLeftToRight(10, 0.05)
                self.seqStropo(10, 0.05)
                self.seqRightToLeft(10, 0.05)
                self.seqStropo(10, 0.05)
                self.seqLeftToRightViceVersa(10, 0.05)
                self.seqStropo(20, 0.04)
                self.seqPWM(self.all)

        except KeyboardInterrupt:
            pass
        print "done"
        GPIO.cleanup()




if __name__ == "__main__":

    p1 = 4
    p2 = 17
    p3 = 27
    p4 = 22
    p5 = 10
    p6 = 9

    #all = [p1,p2,p3,p4,p5,p6]


    #GPIO.setmode(GPIO.BCM)
    ub = LightShow(p1,p2,p3,p4,p5,p6)

    #ub.setup([p1,p2,p3,p4,p5,p6])

#    timer = Timer()
#    timer.killAfterTime(5)
    ub.main()
