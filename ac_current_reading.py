from machine import ADC
import time

ac = ADC(2)

start_time = time.ticks_ms()
i = 0
while i < 500:
    i += 1
    val = ac.read_u16()
    # put a hyphen to point out each near zero crossing values
    print(val, 'amp', time.ticks_diff(time.ticks_ms(), start_time), 'ms')
    time.sleep(0.01)
    
print('reading taken in', time.ticks_diff(time.ticks_ms(), start_time), 'ms')
