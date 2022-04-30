# didn't work. ms is too slow

from machine import Pin, ADC
import _thread
from libraries.nec import NEC_16
from time import sleep_ms

remote_control_buttons = {
    0x45: 'POWER',
    0x15: '-',
    0x09: '+'
}

TOTAL_STEPS = 20
EACH_STEP_WAIT_MS = 250/TOTAL_STEPS
ZERO_CROSS_WAIT_MS = 20
# MIN_CHOP_MS = 60

incoming_opto = ADC(2) # Read AC current
outgoing_opto = Pin(16, Pin.OUT) # Command TRIAC to switch

_current_speed_step = 0
_last_pressed = None

def callback(data, addr, ctrl):
    print(' in callback')
    global _current_speed_step
    global _last_pressed
    
    if data == -1 and _last_pressed in remote_control_buttons and (remote_control_buttons[_last_pressed] == '-' or remote_control_buttons[_last_pressed] == '+'):
        data = _last_pressed
    elif data not in remote_control_buttons:
        return
    else:
        _last_pressed = data
        
    button = remote_control_buttons[data]
    print('Pressed', button)
    if button == '+':
        if _current_speed_step < TOTAL_STEPS:
            _current_speed_step = _current_speed_step + 1
    elif button == '-':
        _current_speed_step = (_current_speed_step - 1) if _current_speed_step > 0 else 0
    elif button == 'POWER':
        if _current_speed_step == 0:
            _current_speed_step = TOTAL_STEPS
        else:
            _current_speed_step = 0
    
    _thread.start_new_thread(monitor_and_regulate, ())
   

def ir_receiver():
    
    ir = NEC_16(Pin(27, Pin.IN), callback)
    print('thread called', ir)

# Bleep the built-in LED when connected
def blink():
    led = Pin(25, Pin.OUT)
    for i in range(4):
        led.value(not led.value())
        sleep_ms(100)
    led.off() # just to make sure that it is off. while debugging, it may happen that it stays on

def monitor_and_regulate():
    global _current_speed_step
    
    while _current_speed_step > 0 and _current_speed_step < TOTAL_STEPS:
        current_current = incoming_opto.read_u16()
        
        if current_current <= 5000:
            wait = ZERO_CROSS_WAIT_MS + int(EACH_STEP_WAIT_MS * _current_speed_step)
            if wait > 250:
                wait = 250
            print('current current', current_current, 'wait', wait)
            outgoing_opto.off()
            sleep_ms(wait)
            outgoing_opto.on()
        else:
            sleep_ms(10)
    
    if _current_speed_step == 0:
        outgoing_opto.off() # turn off since current speed step is 0
        print('OFF')
    elif _current_speed_step == TOTAL_STEPS:
        outgoing_opto.on()
        print('KEEP ON')
        
        
ir_receiver()
blink()
