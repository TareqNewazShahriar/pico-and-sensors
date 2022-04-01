from machine import Pin, ADC, I2C
from time import sleep
from libraries.pico_i2c_lcd import I2cLcd
import math

def light_condition(val):
    val = math.trunc(val / 1000)
    
    if(60 <= val):
        return 'Dark'
    elif(55 <= val):
        return 'Low Light'
    elif(48 <= val):
        return 'Medium Light'
    elif(40 <= val):
        return 'Bright Light'
    elif(20 <= val):
        return 'Very Bright Light'
    else:
        return 'Intense Light'



sensor = ADC(Pin(26, Pin.IN))

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=60000)
print(I2C(0).scan())
rows	= 2
cols	= 16
lcd = I2cLcd(i2c, i2c.scan()[0], rows, cols)

while True:
    val = sensor.read_u16()
    condition = light_condition(val)
    print(val, condition)
    lcd.clear()
    lcd.putstr(condition)
    sleep(0.3)
    