#!/usr/bin/env python
import roslib; roslib.load_manifest('aiden')
import rospy
from aiden.srv import *

booms = [0.1, 0.08, 0.04, 0.04]
joint_angle = [0,0,0,0]
def move(req):
	print(req.a, req.b, req.c)
	res = hand(req.a, req.b, req.c)
	return MessagesResponse("nah")

def hand(x, y, z):
	

def main_com():
	rospy.init_node("hand_node")
	main_srv = rospy.Service("hand_srv", Messages, move)
	print("ready")
	rospy.spin()

if __name__ == '__main__':
	main_com()
