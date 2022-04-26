from machine import Pin, ADC
from time import sleep

ac = ADC(0)

min_current = 65535
max_current = 0
total = 0
i = 0
while i < 100000:
    i += 1
    val = ac.read_u16()
    if val < min_current:
        min_current = val
    elif val > max_current:
        max_current = val
    
    total += val
    if i % 10000 == 0:
        print('min_current', min_current, 'max_current', max_current, 'avg', total/i)
        