# Motion sensor has two other adjusting nobs
# to set pause time of detection and other nob
# to increase/decrease the sensitivity; increased
# sensitivity will detect motion from long distance
# and decreasing it will cause to detect motion from
# less distant area.

from machine import ADC, Pin
from time import sleep

motion = ADC(0)
pir = Pin(26, Pin.IN)
buzzer = Pin(16, Pin.OUT)

buzzer.value(True) # turn off the buzzer first

while True:
    val = pir.value()
    buzzer.value(False if val == 1 else True)
    print('pir', val, '| motion', motion.read_u16(), '| buzzer', buzzer.value())
    sleep(0.2)
