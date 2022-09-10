# Jetson-inference и ROS

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

Для начала запустите ядро ROS

```bash
roscore
```

Для начала проверим возможность трансляции видеопоток:

```bash
roslaunch ros_deep_learning video_viewer.ros1.launch input:=v4l2:///dev/video0 output:=display://0
```

### ImageNet

Следующая команда запустит `ImageNet`. Данная сеть обучена на базе данных из 1000 объектов, а её задача - определить объект, который находится на изображении.

```bash
roslaunch ros_deep_learning imagenet.ros1.launch input:=v4l2:///dev/video0 output:=display://0
```

### DetectNet

Следующая сеть может не только определять несколько объекто, но строить ограничивающие рамки и указывать их положение

```bash
roslaunch ros_deep_learning detectnet.ros1.launch input:=v4l2:///dev/video0 output:=display://0
```

### SegMet

Semantic Segmentation или cемантическая сегментация отличается от `DetectNet` тем, что классификация происходит на уровне пикселей, а не всего изображения.

```bash
roslaunch ros_deep_learning segnet.ros1.launch input:=v4l2:///dev/video0 output:=display://0
```
