# Triados
Добро пожаловать в наше учебное руководство по робототехнике и нейронным сетям

### Содержание

* [Привет мир](#привет-мир) (надо будет изменить)
* [Видеоинструкции](#видеоинструкции) (к защите готово НЕ будет)
* [Примеры кода](#примеры-кода)

### Привет мир

Здесь вы обучитесь...

#### Настройка системы
* [Установка операционной системы](docs/linux_installation.md)
* [Настройка Nvidia jetson](docs/setting_up_jetson_nano.md)

#### Разъёмы Nvidia jetson
* [Основные разьёмы](docs/ports.md)
* [40-контактный разъем расширения](docs/40-pin_expansion_header.md)
  * [i2c](docs/i2c.md)
  * [UART](docs/UART.md)
  * [PWM](docs/PWM.md)
  * [GPIO](docs/GPIO.md)
* [Разьёмы камеры MIPI CSI-2](docs/MIPI_CSI.md)
* [Пины у сд карты и у 40-контактный разъем расширения](docs/hz.md)

#### Взаимодействие с Arduino
* [Начало работы с Arduino](docs/arduino.md)
  * [Програмное обеспечение для взаимодействия с Arduino](https://github.com/mook003/Triados/blob/main/docs/images/Arduino%20software.md)
  * [Первая программа!](https://github.com/mook003/Triados/blob/main/docs/the%20first%20arduino%20program.md)
* [Прорамма для управления двигателями и сервоприводами](docs/servo_and_motors.md) 
  * [Управление электродвигателем постоянного тока](docs/dc_motor.md)
  * [Управление серводвигателем](docs/servomotor.md)

#### Ros
* [Введение в Ros](docs/ros.md)
  * [Publisher and Subscriber](docs/ros.md#publisher-и-subscriber)
  * [Сервис и клиент](docs/ros.md#сервис-и-клиент)

#### Работа с zed
* [ROS](docs/zed.md#ros)
  * [Датчики](docs/sensors.md)
  * [Изображение](docs/camera.md)
  * [Глубина](docs/depth.md)
  * [Нейронные сети](docs/object_detection.md)
* [Pyzed](docs/zed.md#pyzed) (к защите готово НЕ будет)

#### Манипулятор
* [Сборка манипулятора](docs/manipulator_manual.md) (в начале в коробке будет сидеть маленький Ярослав, который всё соберёт)
* [MoveIt](docs/moveit.md)

#### Робот
* [Сборка подвижной платформы](docs/platform.md)
* [Main node](docs/main_node.md)
* [Move node](docs/move_node.md)
* [Hand node](docs/hand_node.md)
