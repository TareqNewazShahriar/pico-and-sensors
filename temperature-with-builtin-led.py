from machine import Pin
import utime

led = Pin(25, Pin.OUT)
sensor_temp = machine.ADC(4)

conversion_factor = 3.3 / (65535)
reading = sensor_temp.read_u16() * conversion_factor 
temperature = 27 - (reading - 0.706)/0.001721
temperatureInt = int(temperature)

print("Temperature: {} C".format(temperature))

secondDigit = temperatureInt % 10
temperatureInt = int(temperatureInt / 10)
firstDigit = temperatureInt % 10;

while firstDigit > 0:
    led.value(1)
    utime.sleep(0.2)
    led.value(0)
    utime.sleep(0.2)
    firstDigit -= 1
    
utime.sleep(2)

i = 0
while i < secondDigit:
    led.value(1)
    utime.sleep(0.2)
    led.value(0)
    utime.sleep(0.2)
    i += 1
    if i == 5:
        utime.sleep(0.5)
    #print(i)


