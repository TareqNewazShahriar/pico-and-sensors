from machine import ADC, Pin
from time import sleep

X = ADC(26)
Y = ADC(27)
button = Pin(16, Pin.IN, Pin.PULL_UP)

while True:
    x = X.read_u16()
    y = Y.read_u16()
    b = button.value()
    
    print(x, y, b)
    
    sleep(0.2)