#4x relay board v1.0p test code

from machine import Pin
from pyb import CAN
import utime


print("starting relay board test")
print("v1.0")
print("initializing")
can = CAN(1, CAN.NORMAL)
can.setfilter(0, CAN.LIST16, 0, (123, 124, 125, 126))


#Setup Pins
hbt_led = Pin("D13", Pin.OUT)
func_butt = Pin("D5", Pin.IN, Pin.PULL_UP) 
can_wakeup = Pin("D6", Pin.OUT)
can_wakeup.value(0)


RELAY_1 = Pin("E1", Pin.OUT)
RELAY_2 = Pin("E2", Pin.OUT)
RELAY_3 = Pin("D1", Pin.OUT)
RELAY_4 = Pin("D0", Pin.OUT)

BUTTON_A = Pin("E15", Pin.IN, Pin.PULL_UP) 
BUTTON_B = Pin("E14", Pin.IN, Pin.PULL_UP) 
BUTTON_C = Pin("E13", Pin.IN, Pin.PULL_UP) 
BUTTON_D = Pin("E12", Pin.IN, Pin.PULL_UP) 

    
    
#Setup hbt timer
hbt_state = 0
hbt_interval = 500
start = utime.ticks_ms()
next_hbt = utime.ticks_add(start, hbt_interval)
hbt_led.value(hbt_state)


print("starting")


def chk_hbt():
    global next_hbt
    global hbt_state
    now = utime.ticks_ms()
    if utime.ticks_diff(next_hbt, now) <= 0:
        if hbt_state == 1:
            hbt_state = 0
            hbt_led.value(hbt_state)
            #print("hbt")
        else:
            hbt_state = 1
            hbt_led.value(hbt_state)  
        
        next_hbt = utime.ticks_add(next_hbt, hbt_interval)

      

def send():
    can.send('EVZRTEST', 123)   # send a message with id 123
    
def get():
    mess = can.recv(0)
    print(mess)
    relay_chase()

        
def relay_chase():
    RELAY_1.value(1)
    utime.sleep_ms(300) 
    RELAY_1.value(0)
    RELAY_2.value(1)
    utime.sleep_ms(300) 
    RELAY_2.value(0)
    RELAY_3.value(1)
    utime.sleep_ms(300) 
    RELAY_3.value(0)
    RELAY_4.value(1)
    utime.sleep_ms(300) 
    RELAY_4.value(0)
    RELAY_1.value(1)
    utime.sleep_ms(300) 
    RELAY_1.value(0)
    RELAY_2.value(1)
    utime.sleep_ms(300) 
    RELAY_2.value(0)
    RELAY_3.value(1)
    utime.sleep_ms(300) 
    RELAY_3.value(0)
    RELAY_4.value(1)
    utime.sleep_ms(300) 
    RELAY_4.value(0)
      
while True:
    chk_hbt()
    if not (func_butt.value()):
        print("function button")
        send()
        relay_chase()
        utime.sleep_ms(200)
    
    if(can.any(0)):
        get()
    
    if not (BUTTON_A.value()):
        print("BUTTON A pressed")
        RELAY_1.value(1)
        utime.sleep_ms(500) 
        RELAY_1.value(0)
    if not (BUTTON_B.value()):
        print("BUTTON B pressed")
        RELAY_2.value(1)
        utime.sleep_ms(500) 
        RELAY_2.value(0)
    if not (BUTTON_C.value()):
        print("BUTTON C pressed")
        RELAY_3.value(1)
        utime.sleep_ms(500) 
        RELAY_3.value(0)
    if not (BUTTON_D.value()):
        print("BUTTON D pressed")
        RELAY_4.value(1)
        utime.sleep_ms(500) 
        RELAY_4.value(0)
        
        
        
        