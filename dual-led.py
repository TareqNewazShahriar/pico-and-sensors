from machine import Pin, PWM
from time import sleep

rr = PWM(Pin(0))
gg = PWM(Pin(1))

rr.freq(60)
gg.freq(60)

i = 2
while i > 0:
    for x in range(2000, -1, -1):
        rr.duty_u16(x)
        sleep(0.001)
    
    for x in range(2000, -1, -1):
        gg.duty_u16(x)
        sleep(0.001)
    i = i - 1
    
rr.duty_u16(0)
gg.duty_u16(0)

#r = Pin(0, Pin.OUT)
#g = Pin(1, Pin.OUT)

# i = 5
# while i > 0:
#     r.on()
#     sleep(0.3)
#     r.off()
# 
#     g.on()
#     sleep(0.3)
#     g.off()
#     
#     i = i - 1


