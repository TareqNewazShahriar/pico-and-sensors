from machine import Pin
from time import sleep, sleep_ms

relay = Pin(0, Pin.OUT)

relay.on()

sleep(5)

relay.off()
