from time import sleep
from machine import Pin
from libraries.nec import NEC_16

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

laser = Pin(16, Pin.OUT)
laser.value(True)

def callback(data, addr, ctrl):
    # print(data, addr, ctrl)
    if data <= 0:  # NEC protocol sends repeat codes.
        return None
    
    buttonName = remote_control_buttons[data];
    print(buttonName, ord(buttonName[0]))
    asciiVal = ord(buttonName[0])
    
    if (buttonName == 'POWER'):
        laser.value(not laser.value())
    elif (len(buttonName) == 1 and 48 <= asciiVal and asciiVal <= 57):
        number = asciiVal - 48
        while number > 0:
            laser.value(False)
            sleep(0.1)
            laser.value(True)
            sleep(0.1)
            number = number - 1
        
ir = NEC_16(Pin(26, Pin.IN), callback)

