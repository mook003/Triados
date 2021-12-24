import serial
import time
import math
import pyzed.sl as sl
arduino = serial.Serial('/dev/ttyUSB0', baudrate = 115200 , timeout = 1)

#main features
wheels_radius = 21.5
wheels_dist=125
wheels_len = wheels_radius * math.pi

#variables
motors_pwm = ''

# type: turning / straight ; angel: -180 - 180 ; speed: 0-100%/ comming soon...
def go(type, angel, speed):
    if "%" in speed: speed = int(list(speed.split("%"))[0])/100
    if type == "turning":
        if angel<0: return [255*speed//1, -(255*speed//1)]
        if angel>0: return [-(255*speed//1), 255*speed//1]
    if type == "straight":return [255*speed//1, 255*speed//1]

while 1:
    try:
        type = input("type: turning / straight")
        angel = int(input("angel: -180 - 180"))
        speed = input("speed: 0-100%")
        motor_pwm = go(type, angel, speed)
        serial.printin(motor_pwm)
        print(*motor_pwm)
    except:
        ard.close()
