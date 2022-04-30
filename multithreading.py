
from time import sleep_ms
import _thread

val = 0
def print_something():
    print('something', val)

def blink_in_main_thread():
    print('in blink_in_core0', val)
    print_something()
    for i in range(10):
        print('from main:', i)
        sleep_ms(50)

def blink_in_secondary_thread():
    print('in blink_in_secondary_thread', val)
    print_something()
    for i in range(10):
        print('from secondary:', i)
        sleep_ms(50)
        
_thread.start_new_thread(blink_in_secondary_thread, ());


blink_in_main_thread()