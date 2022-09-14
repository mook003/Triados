# Датчики

Для получения информации с датчиков нужно использовать стандартную программу [`Subscriber`](/docs/ros.md#publisher-и-subscriber).

### IMU

IMU (инерциальный измерительный блок) - совокупность акселерометра, гироскопа и магнитометра. Может сообщать линейное ускорение, угловую скорость, ориентацию (кватернион).

```python
import roslib; roslib.load_manifest('<Название вашего проекта>')
import rospy

from sensor_msgs.msg import Imu

def callback(msg):
  print(msg.linear_acceleration.x, msg.linear_acceleration.y, msg.linear_acceleration.z, msg.angular_velocity.x, msg.angular_velocity.y, msg.angular_velocity.z, msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w)

def listener():
	rospy.init_node('listenerBoss')
	rospy.Subscriber("/zed2/zed_node/imu/data", Imu, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
```

### Температура

Данные о температуре можно получать сразу с 3 датчиков.

```python
import roslib; roslib.load_manifest('<Название вашего проекта>')
import rospy

from sensor_msgs.msg import Temperature

def callback(msg):
  print(msg.temperature)
  
def leftcallback(msg):
  print(msg.temperature)

def rightcallback(msg):
  print(msg.temperature)

def listener():
	rospy.init_node('listenerBoss')
	rospy.Subscriber("/zed2/zed_node/imu/temperature", Temperature, callback)
  rospy.Subscriber("/zed2/zed_node/imu/temperature/left", Temperature, leftcallback)
  rospy.Subscriber("/zed2/zed_node/imu/temperature/right", Temperature, rightcallback)
	rospy.spin()

if __name__ == '__main__':
	listener()
```

### Давление

```python
import roslib; roslib.load_manifest('<Название вашего проекта>')
import rospy

from sensor_msgs.msg import FluidPressure

def callback(msg):
  print(msg.fluid_pressure * 100)

def listener():
	rospy.init_node('listenerBoss')
	rospy.Subscriber("/zed2/zed_node/atm_press", FluidPressure, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
```

### Данные магнитометра

```python
import roslib; roslib.load_manifest('<Название вашего проекта>')
import rospy

from sensor_msgs.msg import MagneticField

def callback(msg):
  print(msg.magnetic_field.x*10^-6, msg.magnetic_field.y*10^-6, msg.magnetic_field.z*10^-6)

def listener():
	rospy.init_node('listenerBoss')
	rospy.Subscriber("/zed2/zed_node/imu/mag", MagneticField, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
```

<p align="right">Дальше | <b><a href="camera.md">Изображение</a></b>
<br/>
Назад | <b><a href="zed_param.md">Настройка камеры</a></b></p>
<p align="center"><sup>2021-2022 TRIADOS | </sup><a href="../README.md#содержание"><sup>Содержание</sup></a></p>
