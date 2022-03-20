#!/usr/bin/env python
import roslib; roslib.load_manifest('aiden')
import rospy
import serial
import math

from std_msgs.msg import String
from sensor_msgs.msg import Imu

rbt_coord = [0,0,0]
rbt_angle = 0
s = 0
motion_coord = []



def callbackIMU (data):
	global rbt_angle, motion_coord
	rbt_angle = data.orientation.z * 90/0.71 + 100000
	
def callback(data):
	global math, motion_coord, rbt_angle 
	coord = list(map(float, data.data.split()))
	coord[0]-=0.0468
	coord[1]+=0.0585
	motion_coord = [math.atan(coord[1] / coord[0]) * 180 / math.pi, coord[0]]
	print("motion_coord: {}".format(motion_coord))
	if motion_coord[0] > 2:
		ard.write(bytes("0,80,-80,80,-80"))
	if motion_coord[0] < -2:
		ard.write(bytes("0,-80,80,-80,80"))
	if motion_coord[0] > -2 and motion_coord[0] < 2 and motion_coord[1] > 0.35:
		ard.write(bytes("0,-80,-80,-80,-80"))
	if motion_coord[1] <= 0.35:
		ard.write(bytes("0,0,0,0,0"))
def main():
	rospy.init_node('move_node')
	#rate = rospy.Rate(1)
	rospy.Subscriber("main_node_move", String, callback)
	rospy.spin()




if __name__ == '__main__':
	ard = serial.Serial('/dev/ttyACM0', baudrate = 115200)
	main()

#ard.write(bytes("0,50,-50,50,-50", "utf-8"))

#print("rbt_angle: {}".format(rbt_angle))
#print("data.orientation.z: {}".format(data.orientation.z))
#print("data.orientation.z r: {}".format(data.orientation.z * 90/0.71))
#print("data.orientation.z * 90/0.71 - rbt_angle: {}".format(data.orientation.z * 90/0.71 - rbt_angle))
#rospy.Subscriber("/zed2/zed_node/imu/data", Imu, callbackIMU)
