# Введение в Ros

Операционная система робота (ROS) - это набор программных библиотек и инструментов, которые помогают создавать приложения для роботов. Главной особенностью данной системы является то, что все процессы выполняются параллельно в отдельных нодах или связи клиент-сервер.

<img src="https://github.com/mook003/Triados/blob/main/docs/images/topic.png" width="100%">

# Создание первого проекта

Для начала откройте терминал и выполните эту команду, чтобы создать папку для ваших проектов:

``` bash
mkdir <Название вашей папки>
```


Следующей командой вы добавтие папку в bash файл, для того, чтобы ROS мог находить её и запускать проекты.

``` bash
export ROS_PACKAGE_PATH=-/<Название вашей папки>:$ROS_PACKAGE_PATH
```
> **note:** Также перед каждым запуском программы ROS в новом терминале нужно выполнять эту команду.

Далее перейдём в вашу папку, создадим новый проект командой `roscreate-pkg` и сразу соберём его:
``` bash
cd <Название вашей папки>
roscreate-pkg <Название вашего проекта> std_msgs rospy roscpp
rosmake
```

> **note:** После названия вашего проекта нужно указать пакеты, которые вы хотите добавить. Например, `std_msgs` - пакет, который содержит стандартные типы сообщений (Bool, Float64, Int64, String и другие); `rospy` - библиотека python для работы с ROS; `roscpp` - библиотека с++ для работы с ROS.
> **note:** Также перед каждым запуском программы ROS в новом терминале нужно выполнять команду `export ROS_PACKAGE_PATH=-/<Название вашей папки>:$ROS_PACKAGE_PATH`

Поздравляю! Теперь у вас есть собранный проект и мы можем перейти к написанию программ.

# Publisher и subscriber
Приступим к написанию нод для связи Publisher и Subscriber.

Для начала перейдите в папку проекта командой `roscd`, создайте папку для нод и два текстовых документа. 

``` bash
roscd <Название вашего проекта>
mkdir nodes
touch nodes/Publisher.py
touch nodes/Subscriber.py
chmod +x nodes/Publisher.py
chmod +x nodes/Subscriber.py
make
```
Для запуска программ через ROS нужно сделать их исполняемыми командой `chmod +x`. 
> **note:** После каждого изменения структуры вашего проекта нужно заново его собирать командой `make`.

Перейдём к коду.

Вот краткий обзор кода для Publisher:
``` python
#!/usr/bin/env python
import roslib; roslib.load_manifest('<Название вашего проекта>')
import rospy

from std_msgs.msg import String

def talker():
	pub = rospy.Publisher('chatter', String)
	rospy.init_node('talker1')
	while not rospy.is_shutdown():
		str  = 'Hello world %s' %rospy.get_time
		rospy.loginfo(str)
		pub.publish(String(str))

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException: pass
```

Для начала откройте файл `Publisher.py` в выбранном вами редакторе и добавьте последовательность `shebang` в самый верх файла, чтобы автоматически использовать интерпретатор Python и операторы `import`:
``` python
#!/usr/bin/env python
import roslib; roslib.load_manifest('<Название вашего проекта>')
import rospy
```
Команда `roslib.load_manifest('<Название вашего проекта>')` добавляет зависимости, указанные в манифесте вашего проекта.


Далее импортируем из пакета `std_msgs` тип данных `String`. Благодаря этому программа сможет получать и отправлять данные типа `String` или же текст.
``` python
from std_msgs.msg import String
```

Основой программы является функция `talker`:

``` python
def talker():
	pub = rospy.Publisher('chatter', String)
	rospy.init_node('talker')
	while not rospy.is_shutdown():
		str  = 'Hello world %s' %rospy.get_time
		rospy.loginfo(str)
		pub.publish(String(str))
```

Командой `pub = rospy.Publisher('chatter', String)` мы обьявляем узел `pub`, который будет публиковать данные в топик `chatter` в формате `String`. 
Следующая строчка, `rospy.init_node('talker')`, сообщает ROS, что название ноды - `talker`.
`rospy.is_shutdown()` возвращает `false` когда ROS работает.
`rospy.loginfo(str)` выводит в терминал сообщение с указанием времени и уровня.
`pub.publish(String(str))` публикует сообщение `str` в формате `String`.

Завершает программу стартовая инструкция `__name__ == '__main__'` и конструкция обработки исключений
``` python
if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException: pass
```

Вот краткий обзор кода для Subscriber:
``` python
#!/usr/bin/env python
import roslib; roslib.load_manifest('<Название вашего проекта>')
import rospy
from std_msgs.msg import String
def callback(data):
	rospy.loginfo(rospy.get_name()+"$s I heard %s", data.data)

def listener():
	rospy.init_node('listener')
	rospy.Subscriber("chatter", String, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
```

Начало аналогично коду Publisher. Отличия начинаются с функции `callback`:
``` python
def callback(data):
	rospy.loginfo(rospy.get_name()+"$s I heard %s", data.data)
```
Эта функция выводит название своей ноды командой `rospy.get_name()` и данные от Publisher.

Далее идёт функция `listener`, которая называет данную ноду `listener` и получает типданных `String` от узла `chatter`, передавая их в функцию `callback`.
```python
def listener():
	rospy.init_node('listener')
	rospy.Subscriber("chatter", String, callback)
	rospy.spin()
```
`rospy.spin()` повторяет данную функцию, пока ROS работает.

Завершает программу также стартовая инструкция `__name__ == '__main__'`:
``` python
if __name__ == '__main__':
	listener()
```

# Сервис и клиент

Приступим к написанию нод для связи Сервис и клиент.

Для начала создайте ещё один проект, следуя [данной](#создание-первого-проекта) инструкции.

Теперь перейдите в папку проекта командой `roscd` и создайте папку для нод и сообщений. Также нужно создать файл для хранения типов сообщений.
``` bash
roscd <Название вашего проекта>
mkdir nodes
mkdir msg
mkdir srv
touch "int64 sum" > msg/Num.msg
touch srv/Messages.srv
```

Откройте файл Messages.srv в текстовом редакторе и добавьте следующие строки:
```
int64 x
int64 y
float64 angle
string Status
---
float64 Sum
string Status_out
```
Переменные, идущие до `---`, отправляются клиентом, а те, которые идут после, принимаются в качестве ответа.

int64 может содержать 64-битные целые числа (от $-2^{63}$ до $2^{63}-1$)

float64 может представлять числа, для которых соблюдается условие: дистанция от X до следующего по величине представимого числа с плавающей запятой равно $2^{E-52}$, E ≈ 2,7182818284


Теперь откройте файл `CMakeList.txt` в вашем проекте и раскоментирйте строчку `#rosbuild_genmsg()` и `#rosbuild_gensrv()`.

Создайте файлы для нод:
``` bash
touch nodes/service.py
touch nodes/client.py
chmod +x nodes/service.py
chmod +x nodes/client.py
make
```
Вот краткий обзор кода для сервиса:

```python
#!/usr/bin/env python
import roslib
roslib.load_manifest('<Название вашего проекта>')
import rospy

from <Название вашего проекта>.srv import *

def callback(req):
	X = req.x
	Y = req.y
	print(req.angle)
	STATUS = req.Status
	return MessagesResponse(X+Y, STATUS)


def add_three_server():
	rospy.init_node('add_two_ints_server')
	s = rospy.Service('add_three', Messages, handle_add_three_ints)
	print("Ready to add coord and Status")
	rospy.spin()

if __name__ == '__main__':
	add_three_server()
```

Начало в обеих программах аналогично предыдущим.

Следующей строчкой мы импортируем переменные и их типы данных:

``` python
from <Название вашего проекта>.srv import *
```

Функция `callback` обрабатывает полученные данные и отправляет ответ командой `MessagesResponse()`.

``` python
def callback(req):
	X = req.x
	Y = req.y
	print(req.angle)
	STATUS = req.Status
	return MessagesResponse(X+Y, STATUS)
```

> **note:** `MessagesResponse()` должен содержать столько переменных, сколько указано в файле `Messages.srv`.

В данной функции новой является команда `s = rospy.Service('add_three', Messages, callback)`. Она задаёт сервис с названием `'add_three`, который передаёт данные в функцию `callback`.

``` python
def add_three_server():
	rospy.init_node('add_two_ints_server')
	s = rospy.Service('add_three', Messages, handle_add_three_ints)
	print("Ready to add coord and Status")
	rospy.spin()
```

Вот краткий обзор кода для клиента:

```python
#!/usr/bin/env python
import roslib
roslib.load_manifest('<Название вашего проекта>')
import sys
import rospy
from <Название вашего проекта>.srv import *


def add_three_client(x, y, angle, Status):
	rospy.wait_for_service('add_three')
	try:
		add_two_ints = rospy.ServiceProxy('add_three', Messages)
		resp1 = add_two_ints(x, y, angle, Status)
		return resp1.Sum, resp1.Status_out
	except rospy.ServiceException as e:
		print("Service call failed: %s" % e)

if __name__ == '__main__':
	if len(sys.argv) == 5:
		x = int(sys.argv[1])
		y = int(sys.argv[2])
		angle = float(sys.argv[3])
		Status = str(sys.argv[4])
	else:
		sys.exit(1)
	print("Requesting %s+%s+%s" % (x, y, angle))
	print("Status:", Status)
	print(add_three_client(x, y, angle, Status))
```

Функция `add_three_client` связывается с сервисом.
``` python
def add_three_client(x, y, angle, Status):
	rospy.wait_for_service('add_three')
	try:
		add_two_ints = rospy.ServiceProxy('add_three', Messages)
		resp1 = add_two_ints(x, y, angle, Status)
		return resp1.Sum, resp1.Status_out
	except rospy.ServiceException as e:
		print("Service call failed: %s" % e)
```
`rospy.wait_for_service('add_three')` останавливает работу программы, пока не будет установленно соединение с сервисом.

`add_two_ints = rospy.ServiceProxy('add_three', Messages)` создаёт дескриптор, в который далее передаются данные.

Переменная `resp1` содержит полученный ответ. 

Благодаря `try` и `except` реализуеся обработка исключений: пока не получена ошибка, выполняется код в `try:`

<p align="right">Next | <b><a href="zed.md">Работа с ZED</a></b>
<br/>
Back | <b><a href="servomotor.md">Управление сервоприводом</a></b></p>
<p align="center"><sup>2021-2022 TRIADOS | </sup><a href="../README.md#содержание"><sup>Содержание</sup></a></p>
