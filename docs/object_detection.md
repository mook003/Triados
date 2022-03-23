# Обнаружения объектов

Для начала нужно активировать обнаружение объектов в [настройках](/docs/zed_param.md#параметры-с-префиксом-object_detection) камеры.

Теперь мы можем перейти рассмотрению кода:

```python
import roslib; roslib.load_manifest('<Название вашего проекта>')
import rospy

from zed_interfaces.msg import Object
from zed_interfaces.msg import ObjectsStamped

def callback(msg):
  for i in msg.objects:
    print(i.lable)

def listener():
	rospy.init_node('listenerBoss')
	rospy.Subscriber("/zed2/zed_node/obj_det/objects", ObjectsStamped, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
```

<p align="right">Next | <b><a href="manipulator_manual.md">Сборка манипулятора</a></b>
<br/>
Back | <b><a href="depth.md">Глубина</a></b></p>
<p align="center"><sup>2021-2022 TRIADOS | </sup><a href="../README.md#содержание"><sup>Содержание</sup></a></p>
