# Version 20250706 @ 14:28

from machine import SoftI2C, Pin, SoftSPI
import time
import tm1637

# Create array to display digits on 7 segment display
disp_decode = ['63','6', '91', '79', '102','109','124', '7', '127', '103']

tm1 = tm1637.TM1637(clk=Pin(2), dio=Pin(3))
tm1.brightness(0)
tm1.write([0,0,0,0,0])

pir = Pin(1, Pin.IN, Pin.PULL_DOWN)
sw_start = pir.value()
alt_boot = 0
count_down = 5
print("\nStarting 5 Second Delay...\n")
while count_down > 0: # Pause for 9 seconds and disp countdown timer

    if sw_start != pir.value(): # Check if 12/24 hour switch changes.
        count_down = 0
        alt_boot = 1
        
    count_down_disp = int(disp_decode[count_down])
    time.sleep(.5)
    tm1.write([1, count_down_disp, 109, 121,112])

    if sw_start != pir.value(): # Check if 12/24 hour switch changes.
        count_down = 0
        alt_boot = 1
    
    time.sleep(.5)
    tm1.write([64, count_down_disp, 0, 62,115])

    if sw_start != pir.value(): # Check if 12/24 hour switch changes.
        count_down = 0
        alt_boot = 1
    
    time.sleep(.5)
    tm1.write([8, count_down_disp, 0 , 0, 0])
    count_down -= 1
    
print("Resumed after 5 Second Delay!\n")
tm1.write([0,0,0,0,0])
if alt_boot == 1:
    print('Switch Toggled')
    tm1.write([111, 99, 109, 121,112])
    from clock_setup import *

# Continue to normal boot if 12/24 swith not togggled