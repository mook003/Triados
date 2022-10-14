#!/usr/bin/env python
import roslib; roslib.load_manifest('aiden')
import sys
import rospy
import serial

from aiden.srv import *
from sensor_msgs.msg import Image
from zed_interfaces.msg import Object
from zed_interfaces.msg import ObjectsStamped
from std_msgs.msg import String



obj_data = []
#
#def hand_com(x, y, z):
#	rospy.wait_for_service("hand_srv")
#	try: 
#		move_server = rospy.ServiceProxy("hand_srv", Messages)
#		data = move_server(x, y, z)
#		return data.report
#	except rospy.ServiceException as e:
#		return e

# Move node communication function
#def move_com(x, y, z):
#	global pub
#	pub.publish(String("{} {} {}".format(x, y, z)))
#	print("{} {} {}".format(x, y, z))

# Received data processing function

# RIGHT_HANDED_Z_UP_X_FWD

def go_to_object():
	global obj_data
	x = obj_data[2][0]
	y = obj_data[2][1]
	z = obj_data[2][2]
	
	y_coef = 0.25 * y ** 3
	
	speed = y

	
def object_search():
	global obj_data
	rospy.loginfo("***** Search *****)
	wheel_arduino.write(bytes("0,20,-20,20,-20"))
	while not object_data:
		rospy.Subscriber("/zed2/zed_node/obj_det/objects", ObjectsStamped, callback)
	rospy.loginfo("***** Find *****)
	wheel_arduino.write(bytes("0,0,0,0,0"))		

def callback(data):
	global obj_data
	rospy.loginfo("***** New Object *****")
	for i in data.objects:
		rospy.loginfo("***** New Object Find*****")
		rospy.loginfo(i.sublabel)
		rospy.loginfo([i.position[0], i.position[1], i.position[2]])
		if i.sublabel == "Apple":
			obj_data = [i.sublabel, i.label_id, [i.position[0], i.position[1], i.position[2]], i.confidence, i.tracking_state ]
			break

def main():
	rospy.loginfo("Start")
	global obj_data
	rospy.Subscriber("/zed2/zed_node/obj_det/objects", ObjectsStamped, callback)
	
	if not obj_data: object_search()

	go_to_object()
		      
	rospy.spin()

if __name__ == '__main__':
	wheel_arduino = serial.Serial('/dev/ttyACM0', baudrate = 115200)
	rospy.loginfo("***** Start *****")
	#pub = rospy.Publisher('main_node_move', String)
	rospy.init_node('main_node')
	main()



########################################################################################################
#	for i in range(0, len(data.objects)):
#		if data.objects[i].lable_id == -1:
#			continue
#		obj_data.append([data.objects[i].label, data.objects[i].label_id, [data.objects[i].position[0], data.objects[i].position[1], #data.objects[i].position[2]], data.objects[i].confidence, data.objects[i].tracking_state ]) # 0: lable - 1: ID - 2:[x,y,z] - 3: confidence - 4: t_s
########################################################################################################
