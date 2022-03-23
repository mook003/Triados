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

В [настройках](/docs/zed_param.md#параметры-с-префиксом-object_detection) вы можете выбрать одну из 5 обученных нейронных сетей: 

`0`: MULTI_CLASS_BOX (предназначен для нахождения людей, транспорта, животных, электронных устройств, фруктов, овощей и сумки на низкопроизводительных графических картах) 

`1`: MULTI_CLASS_BOX_ACCURATE (предназначен для нахождения людей, транспорта, животных, электронных устройств, фруктов, овощей и сумки на высокопроизводительных графических картах)

`2`: HUMAN_BODY_FAST 

`3`: HUMAN_BODY_ACCURATE 

`4`: MULTI_CLASS_BOX_MEDIUM (предназначен для нахождения людей, транспорта, животных, электронных устройств, фруктов, овощей и сумки на среднепроизводительных графических картах)

`5`: HUMAN_BODY_MEDIUM

<p align="right">Next | <b><a href="manipulator_manual.md">Сборка манипулятора</a></b>
<br/>
Back | <b><a href="depth.md">Глубина</a></b></p>
<p align="center"><sup>2021-2022 TRIADOS | </sup><a href="../README.md#содержание"><sup>Содержание</sup></a></p>
