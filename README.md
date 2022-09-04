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
  * :x: [Jetson-inference](docs/setting_up_jetson_nano.md#jetson-inference)

#### Разъёмы Nvidia jetson
* [40-контактный разъем расширения](docs/40-pin_expansion_header.md)
  * [i2c](docs/i2c.md)
  * [UART](docs/UART.md)
  * [PWM](docs/PWM.md)
  * [GPIO](docs/GPIO.md)
* [Разьёмы камеры MIPI CSI-2](docs/MIPI_CSI.md)
* [12-контактный разъем кнопок](docs/12-pin_button_header.md)

#### Взаимодействие с Arduino
* [Что такое Arduino и для чего оно нужно в нашем роботе?](docs/arduino.md)
  * [Начало работы с Arduino](https://github.com/mook003/Triados/blob/main/docs/4to_takoe_arduino.md)
  * [Програмное обеспечение для взаимодействия с Arduino](https://github.com/mook003/Triados/blob/main/docs/the%20first%20arduino%20program.md)
* [Прорамма для управления двигателями и сервоприводами](docs/servo_and_motors.md) 
  * [Управление электродвигателем постоянного тока](docs/dc_motor.md)
  * [Управление серводвигателем](docs/servomotor.md)

#### Ros
* [Введение в Ros](docs/ros.md)
  * [Publisher and Subscriber](docs/ros.md#publisher-и-subscriber)
  * [Сервис и клиент](docs/ros.md#сервис-и-клиент)
  * [Файлы ROS](docs/ros_files.md)

#### Работа с zed
* [ROS](docs/zed.md#ros)
  * [Настройка камеры](docs/zed_param.md)
  * [Датчики](docs/sensors.md)
  * [Изображение](docs/camera.md)
  * [Глубина](docs/depth.md)
  * [Нейронные сети](docs/object_detection.md)
* [Pyzed](docs/zed.md#pyzed) (к защите готово НЕ будет)

#### Манипулятор
* [Сборка манипулятора](docs/manipulator_manual.md) (в начале в коробке будет сидеть маленький Ярослав, который всё соберёт) нет
* [MoveIt](docs/moveit.md)

#### Робот
* [Сборка подвижной платформы](docs/platform.md)
* [Main node](docs/main_node.md)
* [Move node](docs/move_node.md)
* [Hand node](docs/hand_node.md)
