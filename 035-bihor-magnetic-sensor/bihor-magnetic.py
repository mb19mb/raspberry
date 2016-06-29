# coding=utf-8
#!/usr/bin/python


#############################################################################################################
### Copyright by Joy-IT
### Published under Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License
### Commercial use only after permission is requested and granted
###
### Single Analog Sensor - Raspberry Pi Python Code Example
###
#############################################################################################################


# Dieser Code nutzt die ADS1115 und die I2C Python Library fuer den Raspberry Pi
# Diese ist unter folgendem Link unter der BSD Lizenz veroeffentlicht
# [https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code]
from Adafruit_ADS1x15 import ADS1x15
from time import sleep

# Weitere benoetigte Module werden importiert und eingerichtet
import time, signal, sys, os, math
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Benutzte Variablen werden initialisiert
delayTime = 0.2
voltageMax = 3300 # maximal möglicher Spannungswert am ADC

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
# sps = 64   # 64 Samples pro Sekunde
# sps = 128  # 128 Samples pro Sekunde
sps = 250  # 250 Samples pro Sekunde
# sps = 475  # 475 Samples pro Sekunde
# sps = 860  # 860 Samples pro Sekunde

# ADC-Channel (1-4) wird ausgewaehlt
adc_channel = 0    # Channel 0
# adc_channel = 1    # Channel 1
# adc_channel = 2    # Channel 2
# adc_channel = 3    # Channel 3

# Hier wird der ADC initialisiert - beim KY-053 verwendeten ADC handelt es sich um einen ADS1115 Chipsatz
adc = ADS1x15(ic=ADS1115)

#############################################################################################################

# ########
# Hauptprogrammschleife
# ########
# Das Programm misst mit Hilfe des ADS1115 ADC den aktuellen Spannungswert am ADC, berechnet aus diesem
# und den bekannten Widerstandswert des Serien-Vorwiderstands den aktuellen Widerstandwert des Sensors
# und gibt diese in der Konsole aus.

try:
        while True:
                #Aktueller Wert wird aufgenommen,...
                voltage = adc.readADCSingleEnded(adc_channel, gain, sps)

                # ... der Widerstand wird berechnet...
                resitance = 10000 * voltage/(voltageMax - voltage)

                # ... und beides hier in die Konsole ausgegeben
                print "Spannungswert:", voltage,"mV, Widerstand:", resitance,"Ω"
                print "---------------------------------------"

                # Delay
                time.sleep(delayTime)



except KeyboardInterrupt:
        GPIO.cleanup()