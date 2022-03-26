from machine import Pin
from utime import sleep

green = Pin(0, Pin.OUT) #
relay = Pin(17, Pin.OUT) # use 5v for relay
green.on()

i = 5 
while i > 0:
    relay.high()
    sleep(1)
    relay.low()
    sleep(0.6)
    i = i - 1
