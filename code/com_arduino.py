import serial
import time
import math
import pyzed.sl as sl
arduino = serial.Serial('/dev/ttyUSB0', baudrate = 115200 , timeout = 1)
