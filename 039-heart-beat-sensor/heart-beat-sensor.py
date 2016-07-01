#!/usr/bin/python
# coding=utf-8

#############################################################################################################
### Copyright by Joy-IT
### Published under Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License
### Commercial use only after permission is requested and granted
###
### Parts of Code based on Dan Truong's KY039 Arduino Heartrate Monitor V1.0
### [https://forum.arduino.cc/index.php?topic=209140.msg2168654] Message #29
#############################################################################################################


# Dieser Code nutzt die ADS1115 und die I2C Python Library fuer den Raspberry Pi
# Diese ist unter folgendem Link unter der BSD Lizenz veroeffentlicht
# [https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code]
from Adafruit_ADS1x15 import ADS1x15
from time import sleep

# Weitere benoetigte Module werden importiert und eingerichtet
import time, signal, sys, os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Benutzte Variablen werden initialisiert
beatsPerMinute = 0
isPeak = False
result = False
delayTime = 0.01
maxValue = 0
schwelle = 25
beatTime = 0
oldBeatTime = 0

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
sps = 8    # 8 Samples pro Sekunde
# sps = 16   # 16 Samples pro Sekunde
# sps = 32   # 32 Samples pro Sekunde
# sps = 64   # 64 Samples pro Sekunde
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

# Hier wird der Ausgangs-Pin deklariert, an dem die LED angeschlossen ist.
LED_PIN = 24
GPIO.setup(LED_PIN, GPIO.OUT, initial= GPIO.LOW)


#############################################################################################################

# Hier wird der Ausgangs-Pin deklariert, an dem der Buzzer angeschlossen ist.
def heartBeatDetect(schwelle):
        global maxValue
        global isPeak
        global result
        global oldBeatTime

        # Hier wird der aktuelle Spannungswert am Fototransistor ausgelesen
        # und in der rawValue - Variable zwischengespeichert
        # Mit "adc_channel" wird der am ADC angeschlossene Channel ausgewaehlt
        rawValue = adc.readADCSingleEnded(adc_channel, gain, sps)

        # Reset der Ergebnis Variable
        if result == True:
            result = False

        # Sollte der aktuelle Wert vom letzten maximalen Wert zu weit abweichen
        # (z.B.da der Finger neu aufgesetzt oder weggenommen wurde)
        # So wird der MaxValue resetiert, um eine neue Basis zu erhalten.
        if rawValue * 4 < maxValue:              maxValue = rawValue * 0.8;        # Hier wurd der eigentliche Peak detektiert. Sollte ein neuer RawValue groeßer sein        # als der letzte maximale Wert, so wird das als Spitze der aufgezeichneten Daten erkannt.
        if rawValue > (maxValue - schwelle):

              if rawValue > maxValue:
                    maxValue = rawValue
              # Zum erkannten Peak soll nur ein Herzschlag zugewiesen werden
              if isPeak == False:
                    result = True

              isPeak = True

        else:
            if rawValue < maxValue - schwelle:
              isPeak = False
              # Hierbei wird der maximale Wert bei jedem Durchlauf
              # etwas wieder herabgesetzt. Dies hat den Grund, dass
              # nicht nur der Wert sonst immer stabil bei jedem Schlag
              # gleich oder kleiner als maxValue sein wuerde, sondern auch,
              # falls der Finder sich minimal bewegen sollte und somit
              # das Signal generell schwaecher sein sollte.
            maxValue = maxValue - schwelle/2

        # Wurde in der oberen Abfrage ein Herzschlag detektiert, so wird nun die Ausgabe freigegeben
        if result == True:

            # Berechnung des Puls
            # Hierbei wird bei jedem registrierten Herzschlag die System-Zeit aufgenommen
            # Beim naechsten Herzschlag wird dann die aktuelle Systemzeit mit der gespeicherten verglichen
            # Die Differenz der beiden ergibt dann die Zeit zwischen den Herz-Schlaegen
            # womit man dann auch den Puls berechnen kann.
            beatTime = time.time()
            timedifference = beatTime - oldBeatTime
            beatsPerMinute = 60/timedifference
            oldBeatTime = beatTime

            # Neben der Berechnung des Puls, wird der Herzschlag auch auf eine LED als kurzes Aufblinken ausgegeben
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(delayTime*10)
            GPIO.output(LED_PIN, GPIO.LOW)

            # Erechneter Puls wird der Funktion übergeben
            return beatsPerMinute

#############################################################################################################

# ########
# Hauptprogrammschleife
# ########
# Das Programm sieht vor, dass im Abstand der eingestellten "delayTime" (Standard: 10ms)
# die Funktion zur Herzschlagdetektion aufgerufen wird. Wurde ein Herzschlag erkannt,
# so wird der Puls ausgegeben.

try:
        while True:
                time.sleep(delayTime)
                beatsPerMinute = heartBeatDetect(schwelle)
                if result == True:
                    print "---Herzschlag erkannt !--- Puls:", int(beatsPerMinute),"(bpm)"



except KeyboardInterrupt:
        GPIO.cleanup()