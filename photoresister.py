from machine import Pin, ADC, I2C
from time import sleep
from libraries.pico_i2c_lcd import I2cLcd

sensor = ADC(Pin(26, Pin.IN))

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=60000)
print(I2C(0).scan())
rows	= 2
cols	= 16
lcd = I2cLcd(i2c, i2c.scan()[0], rows, cols)

light_condition = {
    6: 'Very Low Light',
    5: 'Low Light',
    4: 'Medium Light',
    3: 'Bright Light',
    2: 'Very Bright Light',
    1: 'High Intense Light'
}

while True:
    firstChar = str(sensor.read_u16())[0]
    firstDigit = ord(firstChar) - 48;
    print(firstDigit)
    lcd.clear()
    lcd.putstr(light_condition[firstDigit])
    sleep(0.3)
    