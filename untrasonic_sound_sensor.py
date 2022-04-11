from machine import Pin, Timer
import utime

SOUND_SPEED = 0.0343 # in second
CM_TO_INCH = 0.393701
CM_TO_FEET = 0.0328084

trigger = Pin(16, Pin.OUT)
echo = Pin(17, Pin.IN)

def get_distance(timer):
    trigger.high()
    utime.sleep(0.0001)
    trigger.low()
    
    start = 0
    stop = 0
    
    while echo.value() == 0:
        start = utime.ticks_us()
    while echo.value() == 1:
        stop = utime.ticks_us()
        
    duration = stop - start
    distance = (duration * SOUND_SPEED) / 2  # Make the round trip to one way trip
    distance_in_inch = round(distance * CM_TO_INCH, 1)
    
    print(distance_in_inch, 'inch, ', round(distance, 1), 'cm')
    return distance

# Trying in a different way with Timer instead of "while" loop.
timer = Timer()
timer.init(freq=1, mode=Timer.PERIODIC, callback=get_distance)
