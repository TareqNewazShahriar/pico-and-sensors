from machine import Pin, PWM, ADC
from time import sleep
from libraries.nec import NEC_16

remote_control_buttons = {
    0x45: 'POWER',
    0x15: '-',
    0x09: '+'
}

optocoupler_4n35 = ADC(28)
optocoupler_moc3052 = PWM(Pin(22)) # OUT
optocoupler_moc3052.freq(1000)

MIN = 70
MAX = 120
current_val = 0
last_pressed = ''

def callback(data, addr, ctrl):
    global MIN
    global MAX
    global current_val
    global last_pressed
    
    print('current value:', current_val, 'from optocoupler-4n35:', optocoupler_4n35.read_u16(), 'key pressed:', data, 'last pressed:', last_pressed)
    
    if data == -1 and last_pressed in remote_control_buttons and (remote_control_buttons[last_pressed] == '-' or remote_control_buttons[last_pressed] == '+'):
        data = last_pressed
    elif data not in remote_control_buttons:
        return
    else:
        last_pressed = data
    
    if remote_control_buttons[data] == '+':
        if current_val < MIN:
            current_val = MIN - 1
        current_val = current_val + 1
    elif remote_control_buttons[data] == '-':
        current_val = current_val - 1
        if current_val < MIN:
            current_val = 0
    elif remote_control_buttons[data] == 'POWER':
        if current_val == 0:
            current_val = MAX
        else:
            current_val = 0
    
    optocoupler_moc3052.duty_u16(current_val)
    print('current value:', current_val)
    
    
ir = NEC_16(Pin(28, Pin.IN), callback)

