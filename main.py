from machine import Pin, I2C
from pico_i2c_lcd import I2cLcd
import utime

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=10000)
print(I2C(0).scan())

address	= i2c.scan()[0]
rows	= 2
cols	= 16
lcd = I2cLcd(i2c, address, rows, cols)

lcd.move_to(0,0)
lcd.putstr("Temperature")
while True:
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = 27 - (reading - 0.706)/0.001721
    temperature = round(temperature, 1)
    lcd.move_to(0,1)
    lcd.putstr(str(temperature) + " C")
    utime.sleep(0.5)
    