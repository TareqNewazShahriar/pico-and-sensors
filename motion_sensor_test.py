from machine import ADC
from time import sleep

pir = ADC(0)

while True:
    val = pir.read_u16()
    print(val)
    sleep(0.2)
