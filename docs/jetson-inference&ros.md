# Jetson-inference и ROS

## Подготовка

В данном разделе мы разберём как запускать нейронные сети глубокого обучения в нодах ROS

Для начала установите необходимые зависимости
```bash
sudo apt-get install ros-melodic-image-transport ros-melodic-vision-msgs
```

Перейдите в `catkin_ws/src` и клонируйте `ros_deep_learning`:

```bash
cd ~/catkin_ws/src
git clone https://github.com/dusty-nv/ros_deep_learning
```

Соберите и подготовте рабочее пространство

```bash
cd ~/catkin_ws/
catkin_make
source devel/setup.bash
```

## Запуск

Для начала запустите ядро ROS

```bash
roscore
```

Проверим возможность трансляции видеопотока:

```bash
roslaunch ros_deep_learning video_viewer.ros1.launch input:=v4l2:///dev/video0 output:=display://0
```

Вы должны увидеть окно с изображением, полученным от камеры 

### ImageNet

Следующая команда запустит `ImageNet`. Данная сеть обучена на базе данных из 1000 объектов, а её задача - определить объекты, которые находится на изображении.

```bash
roslaunch ros_deep_learning imagenet.ros1.launch input:=v4l2:///dev/video0 output:=display://0
```

В открывшемся окне вы можете также увидеть изображение с камеры, но теперь в левом верхнем углу находится строка с объектам. Первое значение - наибольшее значение уверенности среди всех найденных объектов; остальные - наименования классов объектов.

Также в терминале вы можете увидить информацию о всех объектах.

### DetectNet

Следующая сеть может не только определять объекты на изображении, но и строить ограничивающие рамки и указывать их положение

```bash
roslaunch ros_deep_learning detectnet.ros1.launch input:=v4l2:///dev/video0 output:=display://0
```

В новом окне все обнаруженные объекты будут выделяться ограничивающими рамками с указанием уверенности в определении объекта. В терминале Вы можете увидеть данные об объекте и его ограничивающей рамке.

### SegMet

Semantic Segmentation или cемантическая сегментация отличается от `DetectNet` тем, что классификация происходит на уровне пикселей, а не всего изображения.

```bash
roslaunch ros_deep_learning segnet.ros1.launch input:=v4l2:///dev/video0 output:=display://0
```

В последнем окне Вы можете увидеть, как нейронная сеть выделяет обнаруженные объекты цветами. Например, `SegMet` отдельно выделяет ноги, руки и голову человека. 

## Топики и параметры

Ниже приведены топики сообщений и параметры, которыми опирирует каждый узел.

### ImageNet Node

Топики

| Название топика | I/O | Тип сообщения | Описание |  
|-------------------|--------------|--------------|--------------|
|`image_i`|Ввод|[`sensor_msgs/Image`](http://docs.ros.org/en/melodic/api/sensor_msgs/html/msg/Image.html)|Необработанное входное изображение|
|`classification`|Вывод|[`vision_msgs/Classification2D`](http://docs.ros.org/en/melodic/api/vision_msgs/html/msg/Classification2D.html)|Результаты классификации (идентификатор класса + уверенность)|
|`vision_info`|Вывод|[`vision_msgs/VisionInfo`](http://docs.ros.org/en/melodic/api/vision_msgs/html/msg/VisionInfo.html)|Метаданные видения (название списка параметров меток классов)|
|`overlay`|Вывод|[`sensor_msgs/Image`](http://docs.ros.org/en/melodic/api/sensor_msgs/html/msg/Image.html)|Входное изображение c наложенными результатами классификации|

Параметры

| Название параметра | Тип | Значение по умолчанию | Описание | 
|`model_name`|`string`|`googlenet`|Имя встроенной модели (допустимые значения см. Здесь)|
|`model_path`|`string`|`""`|Путь к пользовательской модели `caffe` или `ONNX`|
|`prototxt_path`|`string`|`""`|Путь к пользовательскому файлу `caffe prototxt`|
|`input_blob`|`string`|`data`|Имя входного слоя `DNN`|
|`output_blob`|`string`|`prob`|Имя выходного слоя `DNN`|
|`class_labels_path`|`string`|`""`|Путь к файлу пользовательских меток классов|
|`class_labels_HASH`|`vector<string>`|class names|Список меток классов, где `HASH` зависит от модели (фактическое имя параметра можно найти в топике `vision_info`)|

### DetectMet Node

Топики

| Название топика | I/O | Тип сообщения | Описание |  
|-------------------|--------------|--------------|--------------|
|`image_i`|Ввод|[`sensor_msgs/Image`](http://docs.ros.org/en/melodic/api/sensor_msgs/html/msg/Image.html)|Необработанное входное изображение|
|`classification`|Вывод|[`vision_msgs/Classification2D`](http://docs.ros.org/en/melodic/api/vision_msgs/html/msg/Classification2D.html)|Результаты классификации (идентификатор класса + уверенность)|
|`vision_info`|Вывод|[`vision_msgs/VisionInfo`](http://docs.ros.org/en/melodic/api/vision_msgs/html/msg/VisionInfo.html)|Метаданные видения (название списка параметров меток классов)|
|`overlay`|Вывод|[`sensor_msgs/Image`](http://docs.ros.org/en/melodic/api/sensor_msgs/html/msg/Image.html)|Входное изображение c наложенными результатами классификации|

Параметры

| Название параметра | Тип | Значение по умолчанию | Описание | 
|||||
|||||
|||||
|||||
|||||
|||||
|||||

### SegMet Node

Топики

| Название топика | I/O | Тип сообщения | Описание |  
|-------------------|--------------|--------------|--------------|
|`image_i`|Ввод|[`sensor_msgs/Image`](http://docs.ros.org/en/melodic/api/sensor_msgs/html/msg/Image.html)|Необработанное входное изображение|
|`classification`|Вывод|[`vision_msgs/Classification2D`](http://docs.ros.org/en/melodic/api/vision_msgs/html/msg/Classification2D.html)|Результаты классификации (идентификатор класса + уверенность)|
|`vision_info`|Вывод|[`vision_msgs/VisionInfo`](http://docs.ros.org/en/melodic/api/vision_msgs/html/msg/VisionInfo.html)|Метаданные видения (название списка параметров меток классов)|
|`overlay`|Вывод|[`sensor_msgs/Image`](http://docs.ros.org/en/melodic/api/sensor_msgs/html/msg/Image.html)|Входное изображение c наложенными результатами классификации|

Параметры

| Название параметра | Тип | Значение по умолчанию | Описание | 
|||||
|||||
|||||
|||||
|||||
|||||
|||||

### video_source Node

Топики

| Название топика | I/O | Тип сообщения | Описание |  
|-------------------|--------------|--------------|--------------|
|`image_i`|Ввод|[`sensor_msgs/Image`](http://docs.ros.org/en/melodic/api/sensor_msgs/html/msg/Image.html)|Необработанное входное изображение|
|`classification`|Вывод|[`vision_msgs/Classification2D`](http://docs.ros.org/en/melodic/api/vision_msgs/html/msg/Classification2D.html)|Результаты классификации (идентификатор класса + уверенность)|
|`vision_info`|Вывод|[`vision_msgs/VisionInfo`](http://docs.ros.org/en/melodic/api/vision_msgs/html/msg/VisionInfo.html)|Метаданные видения (название списка параметров меток классов)|
|`overlay`|Вывод|[`sensor_msgs/Image`](http://docs.ros.org/en/melodic/api/sensor_msgs/html/msg/Image.html)|Входное изображение c наложенными результатами классификации|

Параметры

| Название параметра | Тип | Значение по умолчанию | Описание | 
|||||
|||||
|||||
|||||
|||||
|||||
|||||

### video_output Node

Топики

| Название топика | I/O | Тип сообщения | Описание |  
|-------------------|--------------|--------------|--------------|
|`image_i`|Ввод|[`sensor_msgs/Image`](http://docs.ros.org/en/melodic/api/sensor_msgs/html/msg/Image.html)|Необработанное входное изображение|
|`classification`|Вывод|[`vision_msgs/Classification2D`](http://docs.ros.org/en/melodic/api/vision_msgs/html/msg/Classification2D.html)|Результаты классификации (идентификатор класса + уверенность)|
|`vision_info`|Вывод|[`vision_msgs/VisionInfo`](http://docs.ros.org/en/melodic/api/vision_msgs/html/msg/VisionInfo.html)|Метаданные видения (название списка параметров меток классов)|
|`overlay`|Вывод|[`sensor_msgs/Image`](http://docs.ros.org/en/melodic/api/sensor_msgs/html/msg/Image.html)|Входное изображение c наложенными результатами классификации|

Параметры

| Название параметра | Тип | Значение по умолчанию | Описание | 
|||||
|||||
|||||
|||||
|||||
|||||
|||||

Ниже приведены темы сообщений и параметры, которые реализует каждый узел.
