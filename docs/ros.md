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


Далее перейдём в вашу папку, создадим новый проект командой `roscreate-pkg` и сразу соберём его:
``` bash
cd <Название вашей папки>
roscreate-pkg <Название вашего проекта> std_msgs rospy roscpp
rosmake
```

> **note:** После названия вашего проекта нужно указать пакеты, которые вы хотите добавить. Например, `std_msgs` - пакет, который содержит стандартные типы сообщений (Bool, Float64, Int64, String и другие); `rospy` - библиотека python для работы с ROS; `roscpp` - библиотека с++ для работы с ROS.

Поздравляю! Теперь у вас есть собранный проект и мы можем перейти к написанию программ.

# Publisher и subscriber
Приступим к написанию нод для связи Publisher и subscriber

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
> **note:** После каждого изменения структуры вашего проекта нужно заново его собирать.

Перейдём к коду.

Вот краткий обзор кода:
``` python
#!/usr/bin/env python
import roslib; roslib.load_manifest('Lesson1')
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

Для начала откройте файл `Publisher.py` в выбранном вами редакторе и добавьте последовательность shebang в самый верх файла, чтобы автоматически использовать интерпретатор Python и операторы `import`:
``` python
#!/usr/bin/env python
import roslib; roslib.load_manifest('<Название вашего проекта>')
import rospy
```
Команда `roslib.load_manifest('<Название вашего проекта>')` добавляет зависимости, указанные в манифесте вашего проекта.


Далее импортируем из пакета `std_msgs` тип данных `String`. Благодаря этому программа сможет получать и отправлять данные типа string.
``` python
from std_msgs.msg import String
```

Основой программы является функция `talker`:

``` python
def talker():
	pub = rospy.Publisher('chatter', String)
	rospy.init_node('talker1')
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

Завершает программу стартовая инструкция `__name__ == '__main__'` конструкция обработки исключений
``` python
if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException: pass
```
# Сервис и клиент
