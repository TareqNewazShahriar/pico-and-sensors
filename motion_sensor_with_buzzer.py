# Motion sensor has two other adjusting nobs.
# -One is to set time length of pausing the detection. When upside down, the left nob.
# -Other nob is to increase/decrease the sensitivity of infrared detection. when upside down, the irght nob.
#  Decreasing sensitivity will detect only strong presence of infrared; in other words, if the source is nearby like couple of feet, only then it will be detected by the sensor.
#  Increasing it will cause to detect light motion of infrared from a long distance area like couple of meters.

from machine import ADC, Pin
import time

motion = ADC(0)
pir = Pin(26, Pin.IN)
buzzer = Pin(16, Pin.OUT)

buzzer.value(True) # turn off the buzzer first

detectAgain = False
detectedAt = time.time()

while True:
    val = pir.value()
    buzzer.value(False if val == 1 else True)
    # print('pir', val, '| motion', motion.read_u16(), '| buzzer', buzzer.value())
    time.sleep(0.2)
    
    
    if val == 1 and detectAgain:
        print('Elapsed time:', time.time() - detectedAt)
        detectedAt = time.time()
        detectAgain = False
    elif val == 0:
        detectAgain = True
        