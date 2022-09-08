# Написание программы для управления манипулятором

``` python
#!/usr/bin/env python

import sys
import copy
import rospy
from math import pi
import moveit_msgs.msg
from aiden.srv import *
import moveit_commander
import geometry_msgs.msg
from std_msgs.msg import String
import roslib; roslib.load_manifest('aiden')
from moveit_commander.conversions import pose_to_list

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python', anonymous=True)

robot = moveit_commander.RobotCommander()

scene = moveit_commander.PlanningSceneInterface()

group_name = "<название группы руки>"
move_group = moveit_commander.MoveGroupCommander(group_name)

display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                               moveit_msgs.msg.DisplayTrajectory,
                                               queue_size=20)

angle = [0,0,"false"]
joint_angle = [0,0,0,0]
def move(req):

	pose_goal = geometry_msgs.msg.Pose()
	pose_goal.orientation.w = 1.0
	pose_goal.position.x = reg[0]
	pose_goal.position.y = reg[1]
	pose_goal.position.z = reg[2]

	move_group.set_pose_target(pose_goal)

	plan = move_group.go(wait=True)

	move_group.stop()

	move_group.clear_pose_targets()

	pose = move_group.execute(plan, wait=True)

	ard.write(bytes("0,pose[0],pose[1],pose[2],pose[3]"))
	
	return MessagesResponse("done")

def main_com():
	rospy.init_node("hand_node")
	main_srv = rospy.Service("hand_srv", Messages, move)
	print("ready")
	rospy.spin()

if __name__ == '__main__':
	ard = serial.Serial('/dev/ttyACM0', baudrate = 115200)
	main_com()
```

## Разбор кода

Создайте в выбранном вами редакторе файл `hand_node.py` и откройте его.

Во-первых, давайте добавим последовательность shebang в самый верх файла, чтобы автоматически использовать интерпретатор Python:
``` python
#!/usr/bin/env python
```
Далее мы импортируем модули Python, которые будем использовать в коде.

#### Импорт модулей и типов сообщений

Добавьте `import` операторы для загрузки модулей `roslib`, `rospy` и манифеста вашего !!.

``` python
import roslib; roslib.load_manifest('aiden')
import rospy
```

Следующим этапом нужно импортировать тип сообщений, который будет использоваться нодами:

``` python
from aiden.srv import *
```

#### Функции обработки и передачи данных 
Приступим к написанию основной части прораммы.

Следующая функция обрабатывает данные, получаемые от [клиента](main_node.md)
``` python
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
```

Функция `callbackIMU` получает данные от уза `/zed2/zed_node/imu/data` и обрабатывает их.

``` python
def callbackIMU1 (data):
	global angle
	if angle[2]!="false":
		angle[0] = data.orientation.z * 90/0.71
		angle[2] = "true"
	angle[1] = data.orientation.z * 90/0.71
```

> **note**: Подробный разбор кода для связи `Сервис и клиен` вы можете найти [здесь](service_and_client.md).

Для запуска всех вышеперечисленных функций используется `main`.
``` python
def main_com():
	rospy.init_node("hand_node")
	main_srv = rospy.Service("hand_srv", Messages, move)
	print("ready")
	rospy.spin()
```

Завершает программу стартовая инструкция `__name__ == '__main__'`
``` python
if __name__ == '__main__':
	main_com()
```

> **note**: Обьяснение строчки `ard = serial.Serial('/dev/ttyACM0', baudrate = 115200)` вы можете найти [здесь](arduino.md).

<p align="right">
<br/>
Back | <b><a href="move_node.md">Move node</a></b></p>
<p align="center"><sup>2021-2022 TRIADOS | </sup><a href="../README.md#содержание"><sup>Содержание</sup></a></p>
