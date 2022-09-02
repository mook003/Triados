# ROS :wolf:

Начнём с краткого обзора `zed-ros-wrapper`, пакета для работы с камерами ZED в среде ROS. Он позволяет выводить левые и правые изображения камеры, карту глубины, облако точек, информацию о позе и поддерживает использование нескольких камер ZED.

Он содержит ряд пакетов для обработки данных, получаемых от камеры:
+ nav_msgs
+ tf2_geometry_msgs
+ message_runtime
+ catkin
+ roscpp
+ stereo_msgs
+ rosconsole
+ robot_state_publisher
+ urdf
+ sensor_msgs
+ image_transport
+ roslint
+ diagnostic_updater
+ dynamic_reconfigure
+ tf2_ros
+ message_generation
+ nodelet

В дальнейшем мы разберём эти пакеты на конкретных примерах.

### Запуск

Для запуска оболочки ZED введите в терминале следующую команду:

```bash
roslaunch zed_wrapper zed2.launch
```

Или эту, для запуска по серийному номеру конкретной камеры:

```bash
roslaunch zed_wrapper zed.launch serial_number:=<серийный номер>
```

### Rviz и Zed

Теперь давайте попробуем визуализировать данные с камеры. Запустите `zed-ros-wrapper`:

```bash
roslaunch zed_wrapper zed2.launch
```

Откройте ещё одно окно терминала и введите эту команду:

```bash
rosrun rviz rviz
```

У вас откроется Rviz - трехмерный визуализатор, используемый для визуализации роботов, среды, в которой они работают, и данных датчиков. 

Для добавления нового топика нажмите кнопку `Add`:

<img src="https://github.com/mook003/Triados/blob/main/docs/images/rviz_add.png" width="90%">

В открывшемся окне выберите `By topic` > `/point_cloud` > `/cloud_registered` > `PointCloud` и нажмите `OK`.

<img src="https://github.com/mook003/Triados/blob/main/docs/images/rviz_point_cloud.png" width="40%">

В левой панели Rviz появился новый элемент, `PointCloud`, который вы можете развернуть и узнать информацию о нём. На сцене появилось облако точек. Его можно рассматреть с помощью мыши. 

<img src="https://github.com/mook003/Triados/blob/main/docs/images/rviz_viz_point_cloud.png" width="100%">

Вы также можете добавить и другие топики вышеописанным методом. Например, изображение - `/left_row` или траекторию движения - `/odom`.

# Pyzed

:x::x::x:

<p align="right">Next | <b><a href="zed_param.md">Настройки камеры</a></b>
<br/>
Back | <b><a href="ros.md">Введение в ROS</a></b></p>
<p align="center"><sup>2021-2022 TRIADOS | </sup><a href="../README.md#содержание"><sup>Содержание</sup></a></p>
