# Глубина

Для получения данных о расстоянии запустите следующую программу:

```python
import roslib; roslib.load_manifest('<Название вашего проекта>')
import rospy

from sensor_msgs.msg import Image

def callback(msg):
  print()

def listener():
	rospy.init_node('listenerBoss')
	rospy.Subscriber("/zed2/zed_node/depth/depth_registered", Imu, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
```

<p align="right">Дальше | <b><a href="object_detection.md">Нейронные сети</a></b>
<br/>
Назад | <b><a href="camera.md">Изображение</a></b></p>
<p align="center"><sup>2021-2023 TRIADOS | </sup><a href="../README.md#содержание"><sup>Содержание</sup></a></p>
