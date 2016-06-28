#!/usr/bin/python
# coding=utf-8

from Adafruit_ADS1x15 import ADS1x15
from time import sleep

import time, signal, sys, os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Benutzte Variablen werden initialisiert
delayTime = 1

# Adresszuweisung ADS1x15 ADC

ADS1015 = 0x00  # 12-bit ADC
ADS1115 = 0x01  # 16-bit

# Verstaerkung (Gain) wird ausgewaehlt
gain = 4096  # +/- 4.096V
# gain = 2048  # +/- 2.048V
# gain = 1024  # +/- 1.024V
# gain = 512   # +/- 0.512V
# gain = 256   # +/- 0.256V

# Abtasterate des ADC (SampleRate) wird ausgewaehlt
# sps = 8    # 8 Samples pro Sekunde
# sps = 16   # 16 Samples pro Sekunde
# sps = 32   # 32 Samples pro Sekunde
sps = 64   # 64 Samples pro Sekunde
# sps = 128  # 128 Samples pro Sekunde
# sps = 250  # 250 Samples pro Sekunde
# sps = 475  # 475 Samples pro Sekunde
# sps = 860  # 860 Samples pro Sekunde

# ADC-Channel (1-4) wird ausgewaehlt
adc_channel = 0    # Channel 0
# adc_channel = 1    # Channel 1
# adc_channel = 2    # Channel 2
# adc_channel = 3    # Channel 3

# Hier wird der ADC initialisiert - beim KY-053 verwendeten ADC handelt es sich um einen ADS1115 Chipsatz
adc = ADS1x15(ic=ADS1115)

# Hier waehlt man den Eingangs-Pin des digitalen Signals aus
Digital_PIN = 18
GPIO.setup(Digital_PIN, GPIO.IN, pull_up_down = GPIO.PUD_OFF)

#############################################################################################################

# ########
# Hauptprogrammschleife
# ########
# Das Programm liest die aktuellen Werte der Eingang-Pins
# und gibt diese in der Konsole aus

try:
    while True:
        #Aktuelle Werte werden aufgenommen
        analog = adc.readADCSingleEnded(adc_channel, gain, sps)

        # Ausgabe auf die Konsole
        if GPIO.input(Digital_PIN) == False:
                print "Analoger Spannungswert:", analog,"mV, ","Grenzwert: noch nicht erreicht"
        else:
                print "Analoger Spannungswert:", analog, "mV, ", "Grenzwert: erreicht"
        print "---------------------------------------"

        # Reset + Delay
        button_pressed = False
        time.sleep(delayTime)

except KeyboardInterrupt:
        GPIO.cleanup()