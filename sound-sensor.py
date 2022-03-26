from machine import Pin, ADC
from utime import sleep

#sensor = ADC(26)

#sensor_pin = Pin(26, Pin.IN)
sensor_pin = Pin(20, Pin.IN)

#sensor_pin.value(0)
while True:
    #print(sensor.read_u16())
    
    print(sensor_pin.value())
    #sensor_pin.value(0)
    
    sleep(0.2)
    