# Initial (not raining) ADC value is the max int - 65535.
# The more the rain or water drops falls on the detector sheet,
# the less the value becomes.
# For binary Pin input, neutral value is 1, if heavy drops are
# detected, value will be 0; for light drops value will remain 0.
# N.B.: connect the sheet with the sensor.

from machine import Pin, ADC
from time import sleep

water_drop_sensor = ADC(26)
drop_sensor_binary = Pin(16, Pin.IN)

while True:
    print(water_drop_sensor.read_u16())
    print(drop_sensor_binary.value())
    sleep(0.3)
