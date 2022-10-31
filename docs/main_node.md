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

if __name__ == '__main__':

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



Функция `go_to_object` управляет колёсам робота через Arduino и соответсвующий драйвер.



Далее идут функции `pose_callback` и `od_callback`, получающие данные от топиков `/zed2/zed_node/pose` и `/zed2/zed_node/obj_det/objects` соответственно. `pose_callback` получает положение робота отноительно начального положения: координаты (x,y,z) и ориентацию в виде кватарнионы
а (x,y,z,w).

Последняя функция, `main`, запускает работу программы.


Следующая функция обеспечивает связь между `main_node` и [`hand_node`](https://github.com/mook003/Triados/blob/main/code/nodes/hand_node.py), передавая координаты объекта и получая обратно отчёт от манипулятора.
``` python
def hand_com(x, y, z):
	rospy.wait_for_service("hand_srv")
	try: 
		move_server = rospy.ServiceProxy("hand_srv", Messages)
		data = move_server(x, y, z)
		return data.report
	except rospy.ServiceException as e:
		return e
```

> **note**: Подробный разбор кода для связи `Сервис и клиент` вы можете найти [здесь](ros.md#сервис-и-клиент).

Функция `move_com` публикует координаты найденного объекта для [`move_node`](https://github.com/mook003/Triados/blob/main/code/nodes/move_node.py).

``` python
def move_com(x, y, z):
	global pub
	pub.publish(String("{} {} {}".format(x, y, z)))
	print("{} {} {}".format(x, y, z))
```

Для обработки данных, получаемых от узла `/zed2/zed_node/obj_det/objects`, используется функция `callback`.

``` python
def callback(data):
	global obj_data
	obj_data = []
	rospy.loginfo("***** New Object *****")
	for i in data.objects:
		print("find")
		print(i.sublabel)
		if i.sublabel == "Orange":
			obj_data.append([i.label, i.label_id, [i.position[0]-0.0468, i.position[1]+0.0585, i.position[2]], i.confidence, i.tracking_state ])
			break
	if obj_data:
		print(obj_data)
		if obj_data[0][2][0]>0.35:
			move_com(obj_data[0][2][0], obj_data[0][2][1], obj_data[0][2][2])
		if obj_data[0][2][0]<0.35:
			print(hand_com(obj_data[0][2][0], obj_data[0][2][1], obj_data[0][2][2]))
```
> **note**: Подробный разбор кода для связи `Publisher and Subscriber` вы можете найти [здесь](ros.md#publisher-и-subscriber).

Для запуска всех вышеперечисленных функций используется `main`.
``` python
def main():
	rospy.Subscriber("/zed2/zed_node/obj_det/objects", ObjectsStamped, callback)
	print("asa")
	global obj_data
	print(obj_data)
```

Завершает программу стартовая инструкция `__name__ == '__main__'`
``` python
if __name__ == '__main__':
	pub = rospy.Publisher('main_node_move', String)
	rospy.init_node('main_node')
	main()
```

<p align="right">Дальше | <b><a href="move_node.md">Move node</a></b>
<br/>
Назад | <b><a href="platform.md">Сборка подвижной платформы</a></b></p>

<p align="center"><sup>2021-2022 TRIADOS | </sup><a href="../README.md#содержание"><sup>Содержание</sup></a></p>
