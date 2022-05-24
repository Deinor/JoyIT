from microbit import *
from LED import carON
from car_modes import mode1, stop
import gc

mode = 0

sleep(500)
carON()

while True:
    if button_a.was_pressed() == 1:
        mode += 1
        if mode > 2:
            mode = 0
    display.show(mode)
    
    if mode == 0:
        stop()
        
    elif mode == 1:
        mode1()

    elif mode == 2:
        lightsON()
        carDrive(100, 0, 100, 0)
        sleep(2000)
        lightsBreakON()
        sleep(1000)
        carStop()
        sleep(3000)
    
    gc.collect()