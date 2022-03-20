#!/usr/bin/env python
import roslib
roslib.load_manifest('Lesson2')
import sys
import rospy
from Lesson2.srv import *


def add_three_client(x, y, angle, Status):
	rospy.wait_for_service('add_three')
	try:
		add_two_ints = rospy.ServiceProxy('add_three', Messages)
		resp1 = add_two_ints(x, y, angle, Status)
		return resp1.Sum, resp1.Status_out
	except rospy.ServiceException as e:
		print("Service call failed: %s" % e)


def usage():
	return "%s [x y angle Status]" % sys.argv[0]

if __name__ == '__main__':
	if len(sys.argv) == 5:
		x = int(sys.argv[1])
		y = int(sys.argv[2])
		angle = float(sys.argv[3])
		Status = str(sys.argv[4])
	else:
		print(usage())
		sys.exit(1)
	print("Requesting %s+%s+%s" % (x, y, angle))
	print("Status:", Status)
	print(add_three_client(x, y, angle, Status))
