import RPi.GPIO as GPIO
import time


class Motor(object):
    forwardPin = 7
    backwardPin = 8
    delay = 1

    def __init__(self, forwardPin = 7, backwardPin = 8, delay = 1):
        self.forwardPin = forwardPin
        self.backwardPin = backwardPin
        self.delay = delay

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.forwardPin, GPIO.OUT)
        GPIO.setup(self.backwardPin, GPIO.OUT)

    def forward(self):
        GPIO.output(self.forwardPin, GPIO.HIGH)
        time.sleep(self.delay)
        GPIO.output(self.forwardPin, GPIO.LOW)

    def backward(self):
        GPIO.output(self.backwardPin, GPIO.HIGH)
        time.sleep(self.delay)
        GPIO.output(self.backwardPin, GPIO.LOW)

    def demo(self):
        self.forward()
        self.backward()


if __name__ == "__main__":
    motor = Motor(7,8,1)
    motor.demo()
    GPIO.cleanup()
