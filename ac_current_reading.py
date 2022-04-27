from machine import ADC
import time

ac = ADC(0)

min_current = 65535
max_current = 0
total = 0

start_time = time.ticks_ms()
i = 0
while i < 100000:
    i += 1
    val = ac.read_u16()
    total += val
    if val < min_current:
        min_current = val
    elif val > max_current:
        max_current = val
    
    
print('min current:', min_current, 'max current:', max_current, 'avg:', total/i)
print('Total', i, 'reading taken in', time.ticks_diff(time.ticks_ms(), start_time), 'ms')
