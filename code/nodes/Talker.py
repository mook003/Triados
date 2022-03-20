#!/usr/bin/env python
import roslib; roslib.load_manifest('Lesson1')
import rospy
from std_msgs.msg import String
def talker():
	pub = rospy.Publisher('chatter', String)
	rospy.init_node('talker1')
	while not rospy.is_shutdown():
		str  = 'Hello world %s' %rospy.get_time
		rospy.loginfo(str)
		pub.publish(String(str))
		rospy.sleep(1.0)

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException: pass
