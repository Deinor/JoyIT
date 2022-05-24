from microbit import button_a, sleep,
from motors import carStop, carDrive
from sensors import fetchSensorData
from LED import lightsBreakON, lightsIndicator
from us import distance

def stop():
    carStop()
    lightsBreakON()
    lightsIndicator(indicator_warning) 

def mode1():
    lightsON()
    while True:
        while fetchSensorData()['ObstclLeft'] == '0' or fetchSensorData()['ObstclRight'] == '0' or distance() < 50:
            carStop()
            lightsIndicator(indicator_warning)
            sleep(1000)
        carDrive(0, 100, 0, 100)
        if button_a.was_pressed() == 1:
            break
    return 1

while True:
    mode1()      