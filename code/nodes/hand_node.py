#!/usr/bin/env python
import roslib; roslib.load_manifest('aiden')
import rospy
from aiden.srv import *

angle = [0,0,"false"]
joint_angle = [0,0,0,0]
def move(req):
	global angle
	rospy.Subscriber("/zed2/zed_node/imu/data", Imu, callbackIMU)
	angle[0] += 180
	while angle[0]+1<angle[1] or angle[0]+1<angle[1]:
		rospy.Subscriber("/zed2/zed_node/imu/data", Imu, callbackIMU)
		ard.write(bytes("0,60,-60,60,-60"))
	angle[2] ="false"
	print("vse")
	res = hand(req.a, req.b, req.c)
	return MessagesResponse("nah")

def callbackIMU1 (data):
	global angle
	if angle[2]!="false":
		angle[0] = data.orientation.z * 90/0.71
		angle[2] = "true"
	angle[1] = data.orientation.z * 90/0.71

def main_com():
	rospy.init_node("hand_node")
	main_srv = rospy.Service("hand_srv", Messages, move)
	print("ready")
	rospy.spin()

if __name__ == '__main__':
	main_com()
