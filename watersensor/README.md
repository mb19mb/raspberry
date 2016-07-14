# Funduino Watersensor 

## @Raspberry Pi

### AnalogDigitalConverter

An ADC is required, for example ADS1115.

#### Configure I2C Kernel Support

Edit
~ $ nano /etc/modules

and add two lines to the file

i2c-bcm2708&nbsp
i2c-dev

Verify that /etc/modprobe.d/raspi-blacklist.conf don't(!) blacklist 
the following modules

blacklist spi-bcm2708
blacklist i2c-bcm2708

If so, put a # in front of them.

Edit
~ $ nano /boot/config.tx

and add

dtparam=i2c1=on
dtparam=i2c_arm=on

Ready?
~ $ reboot

#### Testing I2C
Run
~ $ i2cdetect -y 1

#### Wiring ADC to Raspberry
- ADS1115 VDD to RaspPi 3.3V
- ADS1115 GND to RaspPi GND
- ADS1115 SCL to RaspPi SCL
- ADS1115 SDA to RaspPi SDA

#### Source install
Run
~ $ apt-get update
~ $ apt-get install build-essential python-dev python-smbus git
~ $ git clone https://github.com/adafruit/Adafruit_Python_ADS1x15.git
~ $ cd Adafruit_Python_ADS1x15
~ $ python setup.py install


#### Library Usage
Run
~ $ cd ~/Adafruit_Python_ADS1x15/examples
~ $ python simpletest.py


### Watersensor

Connect sensor to Raspberry like in Fritzing Schema and rerun simpletest.py 