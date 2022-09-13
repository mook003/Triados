# Triados
Добро пожаловать в наше учебное руководство по робототехнике и нейронным сетям

### Содержание

* [Привет мир](#привет-мир)
* [Видеоинструкции](#видеоинструкции)
* [Примеры кода](#примеры-кода)

### Привет мир

Данная инструкция предназначена для образовательного набора команды Triados. С ней вы научитесь использовать и обучать нейронные сети, писать программы для управления роботом, узнаете о разнообразных способах передачи информации в роботах и между ними и многое другое. 

#### Настройка системы
* [Установка операционной системы](docs/linux_installation.md)
* [Настройка Nvidia jetson](docs/setting_up_jetson_nano.md)
  * [ZED SDK](docs/setting_up_jetson_nano.md#zed-sdk)
  * [Ros](docs/setting_up_jetson_nano.md#ros)
    * [Zed-ros-wrapper](docs/setting_up_jetson_nano.md#zed-ros-wrapper)
    * [MoveIt](docs/setting_up_jetson_nano.md#moveit)
  * [Jetson-inference](docs/setting_up_jetson_nano.md#jetson-inference)

#### Разъёмы Nvidia jetson
* [40-контактный разъем расширения ](docs/40-pin_expansion_header.md)
  * [i2c](docs/40-pin_expansion_header.md#i2c)
  * [GPIO](docs/40-pin_expansion_header.md#gpio)
  * [UART](docs/40-pin_expansion_header.md#uart)
* [Разьёмы камеры MIPI CSI-2 ](docs/MIPI_CSI-2_camera_connectors.md)
* [12-контактный разъем](docs/12-pin_header.md)

#### Взаимодействие с Arduino
* [Что такое Arduino и для чего оно нужно в нашем роботе?](docs/arduino.md)
* [Начало работы с Arduino](https://github.com/mook003/Triados/blob/main/docs/4to_takoe_arduino.md)
* [Код для управления двигателями и сервоприводами](docs/servo_and_motors.md) 

#### Ros
* [Введение в Ros](docs/ros.md)
  * [Publisher and Subscriber](docs/ros.md#publisher-и-subscriber)
  * [Сервис и клиент](docs/ros.md#сервис-и-клиент)
  * [Типы файлов ROS](docs/ros_files.md)

#### Работа с zed
* [ROS](docs/zed.md#ros)
  * [Настройка камеры](docs/zed_param.md)
  * [Датчики](docs/sensors.md)
  * [Изображение](docs/camera.md)
  * [Глубина](docs/depth.md)
  * [Нейронные сети](docs/object_detection.md)
* [Jetson-inference и ROS](docs/jetson-inference&ros.md)

#### Манипулятор
* [Сборка манипулятора](docs/manipulator_manual.md) 
* [MoveIt](docs/moveit.md)

#### Робот
* [Сборка подвижной платформы](docs/platform.md)
* [Main node](docs/main_node.md)
* [Move node](docs/move_node.md)
* [Hand node](docs/hand_node.md)
