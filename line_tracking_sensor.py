# This sensor can differentiate between while and
# black in front of it which is helpful to track
# a black line on white background or a white line
# on a black background.
# Digital (binary) values will be enough for detection.

from machine import Pin, ADC, I2C
from time import sleep
from libraries.pico_i2c_lcd import I2cLcd

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=4000)
print(i2c.scan())
lcd = I2cLcd(i2c, i2c.scan()[0], 2, 16)

sensor = ADC(26)
sensor_digital = Pin(26, Pin.IN)

while True:
    val = sensor.read_u16()
    val_digital = sensor_digital.value()
    print(val, val_digital)
    lcd.clear()
    lcd.putstr('{}, {}'.format(val, val_digital))
    sleep(0.1)
    
    
