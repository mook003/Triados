# Написание основной программы для управления роботом

``` python
#!/usr/bin/env python
import roslib; roslib.load_manifest('aiden')
import sys
import rospy
import serial
import math

#import message types
from aiden.srv import *
from sensor_msgs.msg import Image
from zed_interfaces.msg import Object
from zed_interfaces.msg import ObjectsStamped
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped

timer = 0
obj_data = [] #information about the detected object
goal_status = False
start_pose = 0
a = math.radians(28.9) # camera angle
zed_coor = [0.095,0.06,0.31] # camera coordinates relative to robot origin

# RIGHT_HANDED_Z_UP_X_FWD

def quaternion_to_euler(x, y, z, w):

        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll_x = math.atan2(t0, t1)
     
        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch_y = math.asin(t2)
     
        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw_z = math.atan2(t3, t4)

	roll_x *= 180/math.pi
	pitch_y *= 180/math.pi
	yaw_z *= 180/math.pi
 
	return roll_x, pitch_y, yaw_z

def go_to_object():
	global obj_data, goal_status
	
	x, y, z = obj_data[2][0], obj_data[2][1], obj_data[2][2]

	x = x * math.cos(a)  + z * math.sin(a) - zed_coor[0]
	y = y + zed_coor[1]
	z = z * math.cos(a) - x * math.sin(a) - zed_coor[2]
	rospy.loginfo("Coord: {}, {}, {} *".format(x,y,z))

	if y<-0.02 and x>0.25:
		rospy.loginfo("napravo")
		wheel_arduino.write(bytes('1,0,120,1,120,0,190,1,190'))
	elif y>0.02 and x>0.25:
		rospy.loginfo("nalevo")
		wheel_arduino.write(bytes('1,1,120,0,120,1,190,0,190'))
	elif y<0.02 and y>-0.02 and x>0.25:
		rospy.loginfo("vper")
		wheel_arduino.write(bytes('1,1,110,1,110,1,150,1,150'))
	if x<0.25:
		goal_status = True
		rospy.loginfo("stop")
		wheel_arduino.write(bytes('0'))

def pose_callback(data):
	global start_pose
	
	position = [data.pose.position.x,data.pose.position.y,data.pose.position.z]
	x,y,z = quaternion_to_euler(data.pose.orientation.x,data.pose.orientation.y,data.pose.orientation.z,data.pose.orientation.w)

	if not start_pose: start_pose = [position, [x,y,z]]
	
	else:
		rospy.loginfo("kruti, verti")	
	
	rospy.loginfo(start_pose)
				

def od_callback(data):
	global obj_data, t, start_pose, goal_status
	for i in data.objects:
		rospy.loginfo("***** New Object Find*****")
		rospy.loginfo(i.sublabel)
		rospy.loginfo([i.position[0], i.position[1], i.position[2]])
		if i.sublabel in ["Orange", "Apple"]:
			obj_data = [i.sublabel, i.label_id, [i.position[0], i.position[1], i.position[2]], i.confidence, i.tracking_state ]
			if not start_pose: rospy.Subscriber("/zed2/zed_node/pose", PoseStamped, pose_callback)
			break
	if goal_status:
		rospy.Subscriber("/zed2/zed_node/pose", PoseStamped, pose_callback)
	if obj_data and not goal_status:
		rospy.loginfo("***** Go To Object *****")
		go_to_object()
	else:
		if not timer:
			timer = rospy.Time.now() + rospy.Duration(1)
		if rospy.Time.now() > timer and timer:
			wheel_arduino.write(bytes('0'))
			timer = 0
	obj_data = []


def main():
	global obj_data
	rospy.Subscriber("/zed2/zed_node/obj_det/objects", ObjectsStamped, od_callback)
	rospy.spin()

#connection to Arduino
wheel_arduino = serial.Serial('/dev/ttyACM0', baudrate = 115200)
	
rospy.loginfo("***** Start *****")
	
#node initialization
rospy.init_node('main_node')

try:
	main()
except rospy.ROSInterruptException: pass
```

## Разбор кода

Создайте в выбранном вами редакторе файл `move_node.py` и откройте его.

Во-первых, давайте добавим последовательность shebang в самый верх файла, чтобы автоматически использовать интерпретатор Python:
``` python
#!/usr/bin/env python
```
Далее мы импортируем модули Python, которые будем использовать в коде.

#### Импорт модулей и типов сообщений

Добавьте `import` операторы для загрузки модулей `roslib`, `rospy` и манифеста вашего паекта.

``` python
import roslib; roslib.load_manifest('aiden')
import sys
import rospy
import serial
import math
```

Следующим этапом нужно импортировать типы сообщений, которые будут использоваться нодами:

``` python
from aiden.srv import *
from sensor_msgs.msg import Image
from zed_interfaces.msg import Object
from zed_interfaces.msg import ObjectsStamped
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
```

#### Функции обработки и передачи данных 

Приступим к написанию основной части прораммы.

Функция `quaternion_to_euler` принимает кватеринон и возвращает уогл поворота в кругах Эйлера. Кватрнионы - особый способ задания поворота объекта, о котором мы скоро подробно расскажем.  

``` python
def quaternion_to_euler(x, y, z, w):

        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll_x = math.atan2(t0, t1)
     
        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch_y = math.asin(t2)
     
        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw_z = math.atan2(t3, t4)

	roll_x *= 180/math.pi
	pitch_y *= 180/math.pi
	yaw_z *= 180/math.pi
``` 

Функция `go_to_object` управляет колёсам робота через Arduino и соответсвующий драйвер.

``` python
def go_to_object():
	global obj_data, goal_status
	
	x, y, z = obj_data[2][0], obj_data[2][1], obj_data[2][2]

	x = x * math.cos(a)  + z * math.sin(a) - zed_coor[0]
	y = y + zed_coor[1]
	z = z * math.cos(a) - x * math.sin(a) - zed_coor[2]
	rospy.loginfo("Coord: {}, {}, {} *".format(x,y,z))

	if y<-0.02 and x>0.25:
		rospy.loginfo("napravo")
		wheel_arduino.write(bytes('1,0,120,1,120,0,190,1,190'))
	elif y>0.02 and x>0.25:
		rospy.loginfo("nalevo")
		wheel_arduino.write(bytes('1,1,120,0,120,1,190,0,190'))
	elif y<0.02 and y>-0.02 and x>0.25:
		rospy.loginfo("vper")
		wheel_arduino.write(bytes('1,1,110,1,110,1,150,1,150'))
	if x<0.25:
		goal_status = True
		rospy.loginfo("stop")
		wheel_arduino.write(bytes('0'))
``` 

Далее идут функции `pose_callback` и `od_callback`, получающие данные от топиков `/zed2/zed_node/pose` и `/zed2/zed_node/obj_det/objects` соответственно. `pose_callback` получает положение робота отноительно начального положения: координаты (x,y,z) и ориентацию в виде кватарнионы
а (x,y,z,w).

``` python
def pose_callback(data):
	global start_pose
	
	position = [data.pose.position.x,data.pose.position.y,data.pose.position.z]
	x,y,z = quaternion_to_euler(data.pose.orientation.x,data.pose.orientation.y,data.pose.orientation.z,data.pose.orientation.w)

	if not start_pose: start_pose = [position, [x,y,z]]
	
	else:
		rospy.loginfo("")	
	
	rospy.loginfo(start_pose)
``` 

``` python
def od_callback(data):
	global obj_data, t, start_pose, goal_status
	for i in data.objects:
		rospy.loginfo("***** New Object Find*****")
		rospy.loginfo(i.sublabel)
		rospy.loginfo([i.position[0], i.position[1], i.position[2]])
		if i.sublabel in ["Orange", "Apple"]:
			obj_data = [i.sublabel, i.label_id, [i.position[0], i.position[1], i.position[2]], i.confidence, i.tracking_state ]
			if not start_pose: rospy.Subscriber("/zed2/zed_node/pose", PoseStamped, pose_callback)
			break
	if goal_status:
		rospy.Subscriber("/zed2/zed_node/pose", PoseStamped, pose_callback)
	if obj_data and not goal_status:
		rospy.loginfo("***** Go To Object *****")
		go_to_object()
	else:
		if not timer:
			timer = rospy.Time.now() + rospy.Duration(1)
		if rospy.Time.now() > timer and timer:
			wheel_arduino.write(bytes('0'))
			timer = 0
	obj_data = []
``` 

Последняя функция, `main`, запускает работу программы.

``` python
def main():
	global obj_data
	rospy.Subscriber("/zed2/zed_node/obj_det/objects", ObjectsStamped, od_callback)
	rospy.spin()
``` 

Следующей строчкой мы объявляем переменную для взаимодействия с Аrduino

``` python
wheel_arduino = serial.Serial('/dev/ttyACM0', baudrate = 115200)
```

Функция `init_node` инициирует ноду в пространстве ROS:

``` python
rospy.init_node('main_node')
```

Завершает программу обработчик исключений прерывания ROS

``` python
try:
	main()
except rospy.ROSInterruptException: pass
``` 

<p align="right">Дальше | <b><a href="start_in_gazebo.md">Начало работы с Gazebo</a></b>
<br/>
Назад | <b><a href="platform.md">Сборка подвижной платформы</a></b></p>

<p align="center"><sup>2021-2022 TRIADOS | </sup><a href="../README.md#содержание"><sup>Содержание</sup></a></p>
