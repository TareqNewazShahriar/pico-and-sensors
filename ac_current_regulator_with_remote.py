from machine import Pin, PWM, ADC
import time
import _thread
from libraries.nec import NEC_16

remote_control_buttons = {
    0x45: 'POWER',
    0x15: '-',
    0x09: '+'
}

optocoupler_4n35 = ADC(0)
optocoupler_moc3052 = PWM(Pin(26)) # OUT
optocoupler_moc3052.freq(1000)

# for 65w stand fan, range is: 101 - 140
# for 100w bulb, range is: 70 - 160
# for 0.5w dim led, range is: 90 - 180
MIN = 80
MAX = 180
current_val = 0
last_pressed = ''

def callback(data, addr, ctrl):
    global MIN
    global MAX
    global current_val
    global last_pressed
    global is_mute_pressed
    
    #print('pressed:', data, 'last pressed:', last_pressed, 'from optocoupler-4n35:', optocoupler_4n35.read_u16())
    
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
    print('-- to optocoupler-MOC3052:', current_val)
    
    
ir = NEC_16(Pin(28, Pin.IN), callback)


