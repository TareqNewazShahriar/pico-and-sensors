from machine import Pin
from time import sleep

# Note: connect the laser firmly.
# 3.3v and 5v - both will lit the laser.

laser = Pin(17, Pin.OUT)

laser.value(False) # True - off, False - on
sleep(2)
laser.value(True)

