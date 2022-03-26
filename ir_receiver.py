import time
from machine import Pin
from nec import NEC_16

remote_control_buttons = {
    0x45: 'POWER',
    0x46: 'MODE',
    0x47: 'MUTE',
    0x44: 'PLAY',
    0x40: 'PREV',
    0x43: 'NEXT',
    0x07: 'EQ',
    0x15: 'MINUS',
    0x09: 'PLUS',
    0x16: '0',
    0x19: 'REPEAT',
    0x0D: 'U/SD',
    0x0C: '1',
    0x18: '2',
    0x5E: '3',
    0x08: '4',
    0x1C: '5',
    0x5A: '6',
    0x42: '7',
    0x52: '8',
    0x4A: '9'    
}

buzzer = Pin(16, Pin.OUT)
# Probably the active buzzer from HiPi has problem.
# It turns on with False/0/off/low, turns off with True/1/on/high
buzzer.value(True) 

def callback(data, addr, ctrl):
    if data > 0:  # NEC protocol sends repeat codes.
        print(data, addr, ctrl, buzzer.value(), not buzzer.value())
        print(remote_control_buttons[data])
        if(remote_control_buttons[data] == 'POWER'):
            buzzer.value(not buzzer.value())

ir = NEC_16(Pin(26, Pin.IN), callback)
