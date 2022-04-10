from machine import Pin, ADC, I2C
from utime import sleep
from libraries.pico_i2c_lcd import I2cLcd

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=10000)
print('I2C address: {}'.format(i2c.scan()))

lcd = I2cLcd(i2c, i2c.scan()[0], 2, 16)

gas = Pin(16, Pin.IN)
gas_sense = ADC(Pin(26))
while True:
    val = gas_sense.read_u16()
    val2 = 3.3 / 1024 * val
    val3 = val / 1024 * 3.3
    print(val, gas.value(), val2, val3)
    lcd.putstr(str(val) + ', ' + str(gas.value()) + ', ' + str(val2))
    lcd.move_to(0, 0)
    sleep(0.7)
    