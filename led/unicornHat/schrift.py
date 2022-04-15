#!/usr/bin/env python
import random
import time
import unicornhat as unicorn
import letters

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(180)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()

r=255
g=0
b=0
sleep = .025

def fetchTupleLetter(letter):
    pixel = []
    leds = letters.switchLetter(letter)
    for y in range(0, 8):
        for x in range(0,8):
            if leds[y][x] == 1: # !!!
                pixel.append((x,y))
    return pixel

def printLetter(pixelList, r, g, b):
    unicorn.clear()
    unicorn.show()
    for i in pixelList:
        if (i[0]>7) :continue
        unicorn.set_pixel(i[0], i[1], r, g, b)
        unicorn.show()
    time.sleep(sleep)

def postponePixel(pixellist):
    pixelCopy = []
    for i in pixellist:
        pixelCopy.append((i[0]+8, i[1]))
    return pixelCopy

def printRunningLetter(pixelList, r, g, b):
    pixelList = postponePixel(pixelList)

    for i in range(0,16):
        #print (pixelList)
        printLetter(pixelList, r, g, b)
        pixelList = eleminieren(pixelList)

def eleminieren(pixel):
    pixelCopy = []
    for i in pixel:
        if (i[0]) == 0: continue # fliegt raus
        pixelCopy.append((i[0]-1,i[1]))
    return pixelCopy

def runningFont(word, r,g ,b):
    for letter in list(word):
        if " " == letter: continue
        pixelList = fetchTupleLetter(letter.upper())
        printRunningLetter(pixelList, r, g, b)

while True:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    runningFont("luke ich bin dein vater", r, g, b)
    time.sleep(0.5)
