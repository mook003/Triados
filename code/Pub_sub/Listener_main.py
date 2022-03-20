#!/usr/bin/env python
import roslib; roslib.load_manifest('Lesson1')
import rospy
from std_msgs.msg import String
def callback(data):
	rospy.loginfo("I heard %s" % data.temperature)

def listener():
	rospy.init_node('listenerBoss')
	rospy.Subscriber("/zed2/zed_node/temperature/left", 10, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
