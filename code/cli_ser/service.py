#!/usr/bin/env python
import roslib
roslib.load_manifest('Lesson2')
from Lesson2.srv import *
import rospy



def handle_add_three_ints(req):
	X = req.x
	Y = req.y
	ANGLE = req.angle
	STATUS = req.Status
	return MessagesResponse(X+Y, STATUS)


def add_three_server():
	rospy.init_node('add_two_ints_server')
	s = rospy.Service('add_three', Messages, handle_add_three_ints)
	print("Ready to add coord and Status")
	rospy.spin()

if __name__ == '__main__':
	add_three_server()
