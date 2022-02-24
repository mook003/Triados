#!/usr/bin/env python
import roslib; roslib.load_manifest('aiden')
import rospy
import serial
import math
from std_msgs.msg import String

rbt_coord = [0,0,0]

#ard = serial.Serial('/dev/ttyACM0', baudrate = 115200)

rospy.init_node('move_node')

def callback(data):
	global math
	coord = data.data.split()
	motion_coord = [math.atan2(float(coord[0]), float(coord[2])) * 180 / math.pi, (float(coord[0])**2 + float(coord[2])**2) **0.5]
	print(motion_coord)

def main_com():
	print("b")
	rospy.Subscriber("main_node_move", String, callback)
	print("c")
	rospy.spin()

def main():
	print("a")
	main_com()




if __name__ == '__main__':
	main()

#ard.write(bytes("0,50,-50,50,-50", "utf-8"))
