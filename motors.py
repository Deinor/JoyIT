# Import of the micro:bit module
from microbit import *

# Initialization of the I2C interface
i2c.init(freq = 400000, sda = pin20, scl = pin19)

# Initialisierung des PWM Controllers
i2c.write(0x70, b'\x00\x01')
i2c.write(0x70, b'\xE8\xAA')

# Control motors using the PWM controller
# PWM0 and PWM1 for the left and PWM2 and PWM3 for the right motor
def drive(PWM0, PWM1, PWM2, PWM3):
    i2c.write(0x70, b'\x02' + bytes([PWM0])) # Transfer value for PWM channel (0-255) to PWM controller. 0x70 is the I2C address of the controller. b'\x02 is the byte for PWM channel 1. To the byte for the channel the byte with the PWM value is added.
    i2c.write(0x70, b'\x03' + bytes([PWM1])) # Repeat the process for all 4 channels
    i2c.write(0x70, b'\x04' + bytes([PWM2]))
    i2c.write(0x70, b'\x05' + bytes([PWM3]))

# stop all motors
def carStop():
    drive(0, 0, 0, 0)