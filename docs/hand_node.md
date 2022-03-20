# Написание программы для управления манипулятором

``` python
#!/usr/bin/env python
import roslib; roslib.load_manifest('aiden')
import rospy
from aiden.srv import *

angle = [0,0,"false"]
joint_angle = [0,0,0,0]
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

def callbackIMU1 (data):
	global angle
	if angle[2]!="false":
		angle[0] = data.orientation.z * 90/0.71
		angle[2] = "true"
	angle[1] = data.orientation.z * 90/0.71

def main_com():
	rospy.init_node("hand_node")
	main_srv = rospy.Service("hand_srv", Messages, move)
	print("ready")
	rospy.spin()

if __name__ == '__main__':
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
