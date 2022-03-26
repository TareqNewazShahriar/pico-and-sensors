from machine import Pin, I2C
from pico_i2c_lcd import I2cLcd
import utime

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=10000)
print(I2C(0).scan())

address	= i2c.scan()[0]
rows	= 2
cols	= 16

utime.sleep(2)
lcd = I2cLcd(i2c, address, rows, cols)
lcd.putstr("Amar Baba")
utime.sleep(2)
lcd.clear()
lcd.move_to(5,0)
lcd.putstr("hey baba")
lcd.move_to(8,1)
lcd.putstr("kakko")

