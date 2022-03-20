#!/usr/bin/env python
import roslib; roslib.load_manifest('Lesson1')
import rospy
from std_msgs.msg import String
def callback(data):
	rospy.loginfo(rospy.get_name()+"$s I heard %s", data.data)

def listener():
	rospy.init_node('listenerBoss')
	rospy.Subscriber("main_node_move", String, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
