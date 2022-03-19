# Написание основной программы для управления роботом

``` python
#!/usr/bin/env python
import roslib; roslib.load_manifest('aiden')
import sys
import rospy


from aiden.srv import *
from sensor_msgs.msg import Image
from zed_interfaces.msg import Object
from zed_interfaces.msg import ObjectsStamped
from std_msgs.msg import String



obj_data = [0, 0, [1,1, 2]]

# Hand node communication function
def hand_com(x, y, z):
	rospy.wait_for_service("hand_srv")
	try: 
		move_server = rospy.ServiceProxy("hand_srv", Messages)
		data = move_server(x, y, z)
		return data.report
	except rospy.ServiceException as e:
		return e

# Move node communication function
def move_com(x, y, z):
	global pub
	str  = "{} {} {}".format(x, y, z)
	pub.publish(String(str))
	print(str)

# Received data processing function
def callback(data):
	global obj_data
	obj_data = []
	rospy.loginfo("***** New Object *****")
	for i in range(0, len(data.objects)):
		if data.objects[i].lable == "Person":
			obj_data.append([data.objects[i].label, data.objects[i].label_id, [data.objects[i].position[0], data.objects[i].position[1], data.objects[i].position[2]], data.objects[i].confidence, data.objects[i].tracking_state ])
			break

def main():
	#rospy.Subscriber("/zed2/zed_node/obj_det/objects", ObjectsStamped, callback)
	global obj_data
	if obj_data:
		if obj_data[2][2]>1:
			move_com(obj_data[2][0], obj_data[2][1], obj_data[2][2])
		else:
			rep = hand_com(obj_data[2][0], obj_data[2][1], obj_data[2][2])
			if rep!="done":
				print("Manipulator error: {}".format(rep) )
			else:
				print("Mission completed")
	rospy.spin()

if __name__ == '__main__':
	pub = rospy.Publisher('main_node_move', String)
	rospy.init_node('main_node')
	
	main()
```

## Разбор кода

Создайте в выбранном вами редакторе файл `main_node.py` и откройте его.

Во-первых, давайте добавим последовательность shebang в самый верх файла, чтобы автоматически использовать интерпретатор Python:
``` python
#!/usr/bin/env python
```
Далее мы импортируем модули Python, которые будем использовать в коде.

#### Импорт модулей и типов сообщений

Добавьте `import` операторы для загрузки модулей `roslib`, `rospy` и манифеста вашего !!.

``` python
import roslib; roslib.load_manifest('aiden')
import sys
import rospy
```

Следующим этапом нужно импортировать типы сообщений, которые будут использоваться нодами:

``` python
from aiden.srv import *
from sensor_msgs.msg import Image
from zed_interfaces.msg import Object
from zed_interfaces.msg import ObjectsStamped
from std_msgs.msg import String
```

#### Функции обработки и передачи данных 
Приступим к написанию основной части прораммы.

Следующая функция обеспечивает связь между `main_node` и [`hand_node`](https://github.com/mook003/Triados/blob/main/code/nodes/hand_node.py), передавая координаты объекта и получая обратно отчёт от манипулятора.
``` python
def hand_com(x, y, z):
	rospy.wait_for_service("hand_srv")
	try: 
		move_server = rospy.ServiceProxy("hand_srv", Messages)
		data = move_server(x, y, z)
		return data.report
	except rospy.ServiceException as e:
		return 
```

> **note**: Подробный разбор кода для связи `Сервис и клиент` вы можете найти [здесь](https://vk.com/video519133527_456239749).

Функция `move_com` публикует координаты найденного объекта для [`move_node`](https://github.com/mook003/Triados/blob/main/code/nodes/move_node.py).

``` python
def move_com(x, y, z):
	global pub
	str  = "{} {} {}".format(x, y, z)
	pub.publish(String(str))
	print(str)
```

Для обработки данных, получаемых от узла `/zed2/zed_node/obj_det/objects`, используется функция `callback`.

``` python
def callback(data):
	global obj_data
	obj_data = []
	rospy.loginfo("***** New Object *****")
	for i in range(0, len(data.objects)):
		if data.objects[i].lable == "Person":
			obj_data.append([data.objects[i].label, data.objects[i].label_id, [data.objects[i].position[0], data.objects[i].position[1], data.objects[i].position[2]], data.objects[i].confidence, data.objects[i].tracking_state ])
			break
```
> **note**: Подробный разбор кода для связи `Publisher and Subscriber` вы можете найти [здесь](https://vk.com/video519133527_456239749).

Для запуска всех вышеперечисленных функций используется `main`.
``` python
def main():
	#rospy.Subscriber("/zed2/zed_node/obj_det/objects", ObjectsStamped, callback)
	global obj_data
	if obj_data:
		if obj_data[2][2]>1:
			move_com(obj_data[2][0], obj_data[2][1], obj_data[2][2])
		else:
			rep = hand_com(obj_data[2][0], obj_data[2][1], obj_data[2][2])
			if rep!="done":
				print("Manipulator error: {}".format(rep) )
			else:
				print("Mission completed")
	rospy.spin()
```

Завершает программу стартовая инструкция `__name__ == '__main__'`
``` python
if __name__ == '__main__':
	pub = rospy.Publisher('main_node_move', String)
	rospy.init_node('main_node')
	
	main()
```
