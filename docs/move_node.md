# Написание основной программы для управления роботом

``` python
import roslib; roslib.load_manifest('aiden')
import rospy
import serial
import math
from std_msgs.msg import String
from sensor_msgs.msg import Imu

rbt_coord = [0,0,0]
rbt_angle = 0
s = 0
motion_coord = []



def callbackIMU (data):
	global rbt_angle, motion_coord
	rbt_angle = data.orientation.z * 90/0.71 + 100000
	
def callback(data):
	global math, motion_coord, rbt_angle 
	coord = list(map(float, data.data.split()))
	coord[0]-=0.0468
	coord[1]+=0.0585
	motion_coord = [math.atan(coord[1] / coord[0]) * 180 / math.pi, coord[0]]
	print("motion_coord: {}".format(motion_coord))
	if motion_coord[0] > 2:
		ard.write(bytes("0,80,-80,80,-80"))
	if motion_coord[0] < -2:
		ard.write(bytes("0,-80,80,-80,80"))
	if motion_coord[0] > -2 and motion_coord[0] < 2 and motion_coord[1] > 0.35:
		ard.write(bytes("0,-80,-80,-80,-80"))
	if motion_coord[1] <= 0.35:
		ard.write(bytes("0,0,0,0,0"))
def main():
	rospy.init_node('move_node')
	#rate = rospy.Rate(1)
	rospy.Subscriber("main_node_move", String, callback)
	rospy.spin()




if __name__ == '__main__':
	ard = serial.Serial('/dev/ttyACM0', baudrate = 115200)
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
import rospy
import serial
import math
```

Следующим этапом нужно импортировать типы сообщений, которые будут использоваться нодами:

``` python
from std_msgs.msg import String
from sensor_msgs.msg import Imu
```

#### Функции обработки и передачи данных 
Приступим к написанию основной части прораммы.

Следующая функция обрабатывает данные, получаемые от узла `/zed2/zed_node/imu/data`
``` python
def callbackIMU (data):
	global rbt_angle, motion_coord
	rbt_angle = data.orientation.z * 90/0.71 + 100000
```

Функция `callback` получает данные от [`main_node`](main_node.md) и передаёт команды Arduino.

``` python
def callback(data):
	global math, motion_coord, rbt_angle 
	coord = list(map(float, data.data.split()))
	coord[0]-=0.0468
	coord[1]+=0.0585
	motion_coord = [math.atan(coord[1] / coord[0]) * 180 / math.pi, coord[0]]
	print("motion_coord: {}".format(motion_coord))
	if motion_coord[0] > 2:
		ard.write(bytes("0,80,-80,80,-80"))
	if motion_coord[0] < -2:
		ard.write(bytes("0,-80,80,-80,80"))
	if motion_coord[0] > -2 and motion_coord[0] < 2 and motion_coord[1] > 0.35:
		ard.write(bytes("0,-80,-80,-80,-80"))
	if motion_coord[1] <= 0.35:
		ard.write(bytes("0,0,0,0,0"))
```

> **note**: Подробный разбор кода для связи `Publisher and Subscriber` вы можете найти [здесь](publisher_and_subscriber.md).

Для запуска всех вышеперечисленных функций используется `main`.
``` python
def main():
	rospy.init_node('move_node')
	rospy.Subscriber("main_node_move", String, callback)
	rospy.spin()
```

Завершает программу стартовая инструкция `__name__ == '__main__'`
``` python
if __name__ == '__main__':
	ard = serial.Serial('/dev/ttyACM0', baudrate = 115200)
	main()
```

> **note**: Обьяснение строчки `ard = serial.Serial('/dev/ttyACM0', baudrate = 115200)` вы можете найти [здесь](arduino.md).

<p align="right">Next | <b><a href="hand_node.md">Hand node</a></b>
<br/>
Back | <b><a href="main_node.md">Main node</a></b></p>
