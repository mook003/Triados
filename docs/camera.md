# Изображение

Для получения изображения с любой из 2 камер нужно использовать следующую программу:

```python
import roslib; roslib.load_manifest('<Название вашего проекта>')
import rospy

from sensor_msgs.msg import Image

def leftcallback(msg):
  print(msg.width, msg.height)

def rightcallback(msg):
  print(msg.width, msg.height)

def listener():
	rospy.init_node('listenerBoss')
	rospy.Subscriber("/zed2/zed_node/right/image_rect_color", Image, leftcallback)
	rospy.Subscriber("/zed2/zed_node/left/image_rect_color", Image, rightcallback)
	rospy.spin()

if __name__ == '__main__':
	listener()
```

<p align="right">Дальше | <b><a href="depth.md">Глубина</a></b>
<br/>
Назад | <b><a href="sensors.md">Датчики</a></b></p>
<p align="center"><sup>2021-2023 TRIADOS | </sup><a href="../README.md#содержание"><sup>Содержание</sup></a></p>
