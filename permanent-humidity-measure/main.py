from dht22 import HumidityMeasure
from tm1637 import *
import time

if __name__ == "__main__":
    delay   = 300 # 5min
    temp    = 0.0
    hum     = 0.0

    hm      = HumidityMeasure(18)

    Display = TM1637(15, 14, BRIGHT_TYPICAL)
    Display.Clear()
    Display.ShowDoublepoint(True)

    try:

        while(1):

            temp, hum = hm.readData()
            #print temp, hum

            temp = "{:.0f}".format(temp).split(".")[0][:2]  # get first two characters
            hum = "{:.0f}".format(hum).split(".")[0][:2]  # get first two characters
            dataFile = open("/home/pi/workspace/raspi-sensorkit/permanent-humidity-measure/data", "a+")
            dataFile.write(str( int(time.time())) + "#" + temp + "#" + hum + "\n")
            dataFile.close()
            if len(temp) == 1: temp = "0" + temp
            if len(hum) == 1: hum = "0" + hum

	    Display.Clear()
	    Display.ShowDoublepoint(True)
            Display.Show1(0, int(temp[0]))
            Display.Show1(1, int(temp[1]))
            Display.Show1(2, int(hum[0]))
            Display.Show1(3, int(hum[1]))
            time.sleep(delay)

    except KeyboardInterrupt:
        Display.Clear()
        print "done"

