# Didn't work well

from machine import Pin, PWM
import time
from libraries.nec import NEC_16

remote_control_buttons = {
    0x45: 'POWER',
    0x15: '-',
    0x09: '+'
}

optocoupler_moc3052 = PWM(Pin(16, Pin.OUT)) # OUT
optocoupler_moc3052.freq(1000)

MIN = 0
MAX = 200
current_val = 0
last_pressed = None

def callback(data, addr, ctrl):
    global MIN
    global MAX
    global current_val
    global last_pressed
    
    if data == -1 and last_pressed in remote_control_buttons and (remote_control_buttons[last_pressed] == '-' or remote_control_buttons[last_pressed] == '+'):
        data = last_pressed
    elif data not in remote_control_buttons:
        return
    else:
        last_pressed = data
        
    button = remote_control_buttons[data]
    if button == '+':
        if current_val < MIN:
            current_val = MIN
        elif current_val < MAX:
            current_val = current_val + 1
    elif button == '-':
        current_val = current_val - 1 if current_val > MIN else 0
    elif button == 'POWER':
        current_val = MAX if current_val == 0 else 0
    
    optocoupler_moc3052.duty_u16(current_val)
    print('-- to optocoupler-MOC3052:', current_val, 'pressed:', button, 'last pressed:', last_pressed)
    
    
ir = NEC_16(Pin(28, Pin.IN), callback)
