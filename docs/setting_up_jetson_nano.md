# Настройка Nvidia jetson

Теперь, когда операционная система настроена, мы можем перейти к установке необходимых библиотек и SDK.

## ZED SDK
Для работы с камерой нам понадобится комплект для разработки программного обеспечения ZED (software development kit - SDK). Установите [этот файл](https://download.stereolabs.com/zedsdk/3.7/jp46/jetsons).

Откройте терминал, перейдите в папку к скачанному файлу и сделайте его исполняемым.

```bash
cd path/to/download/folder
chmod +x <Название файла>.run
```

Запустите установщих ZED SDK:
```bash
./<Название файла>.run
```
> **note:** Для принятия лицензионного соглашения нажмите `q`. Во время установки вам нужно будет отвечать на вопросы для установки зависимостей. Введите `y` для ответа да и `n` для нет и нажмите `Enter`.

## Ros

Настройте Jetson на получение програмного обеспечения. 

```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

Добавьте новый apt ключ.

```bash
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
```

> **note:** Вы можете столкнуться с ошибкой `надо найти`. Для её решения нужно...

Обновите индексы пакетов Debian.

```bash
sudo apt update
```

Установите пакет Ros Desktop, включая поддержку `rqt`, `rviz` и других пакетов для робототехники.

Рекомендуется автоматически загружать переменные среды ROS при запуске нового терминала.

```bash
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc 
source ~/.bashrc
```

Скачайте и инициилизируйте rosdep. Он позволяет устанавливать системные зависимости в командной строке.

```bash
sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
sudo rosdep init 
rosdep update
```

Для установки сторонних пакетов, например ZED ROS wrapper, и запуска собственных вам потребуется создать и настроить рабочее пространство `catkin`.

Установите необходимые зависимости:

```bash
sudo apt-get install cmake python-catkin
```

Создайте папку `src` и укажите её права.
```bash
mkdir -p ~/catkin_ws/src 
cd ~/catkin_ws/
```

Выполните команду для первоначальной пустой сборки рабочего пространства.

```bash
catkin_make
```

Теперь обновите ваш .bashrc

Мы установили ROS melodic и ряд других пакетов для дальнейшей работы.

### Zed ros wrapper



### MoveIt
## Jetson-inference
