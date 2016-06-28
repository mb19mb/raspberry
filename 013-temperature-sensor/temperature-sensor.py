# coding=utf-8
#!/usr/bin/python


#############################################################################################################
### Copyright by Joy-IT
### Published under Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License
### Commercial use only after permission is requested and granted
###
### KY-013 Temperatur Sensor - Raspberry Pi Python Code Example
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

delayTime = 0.5

ADS1115 = 0x01  # 16-bit

# Verstaerkung (Gain) wird ausgewaehlt
gain = 4096  # +/- 4.096V

# Abtasterate des ADC (SampleRate) wird ausgewaehlt
sps = 860  # 860 Samples pro Sekunde

# ADC-Channel (1-4) wird ausgewaehlt
adc_channel = 1    # Channel A1

adc = ADS1x15(ic=ADS1115)


try:
    while True:
        #Aktuelle Werte werden aufgenommen...
        voltage = adc.readADCSingleEnded(adc_channel, gain, sps)
        # ... umgerechnet ...
        temperatur = math.log((10000/voltage)*(3300-voltage))
        temperatur = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 * temperatur * temperatur)) * temperatur);
        temperatur = temperatur - 273.15;
        # ... und ausgegeben
        print "Temperatur:", temperatur,"°C"
        print "---------------------------------------"

        # Delay
        time.sleep(delayTime)

except KeyboardInterrupt:
        GPIO.cleanup()