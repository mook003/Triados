# Настройка Nvidia jetson

Теперь, когда операционная система настроена, мы можем перейти к установке необходимых библиотек и SDK.

## ZED SDK
Для работы с камерой нам понадобится комплект для разработки программного обеспечения ZED (software development kit - SDK). Установите [этот файл](https://download.stereolabs.com/zedsdk/3.7/jp46/jetsons).

Откройте терминал, перейдите в папку к скачанному файлу и сделайте его исполняемым.

> **note:** Терминал можно найти на рабочем столе или вызвать комбинацией `Ctrl+ALT+T`

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

Скачайте и инициилизируйте `rosdep`. Он позволяет устанавливать системные зависимости в командной строке.

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

Теперь обновите ваш `.bashrc` файл с информацией о новом рабочем пространстве.

```bash
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc 
source ~/.bashrc
```

Ваше рабочее пространстве готово для сборки пакетов.

Мы установили ROS melodic и ряд других пакетов для дальнейшей работы.

### Zed ros wrapper

Перейдите в папку `src` вашего рабочего пространства `catkin`.

```bash
cd ~/catkin_ws/src
```

Клонируйте репозиторий ZED ROS wrapper.

```bash
cd ~/catkin_ws
rosdep install --from-paths src --ignore-src -r -y
```

Проверьте зависимости:

```bash
cd ~/catkin_ws
rosdep install --from-paths src --ignore-src -r -y
```

Команда `rosdep` проверит все элементы в папке `src` и установит недостоющие зависимости.

Теперь скомпилируйте `ZED ROS wrapper`:

```bash
catkin_make -DCMAKE_BUILD_TYPE=Release
```

### MoveIt

Для начала проверьте наличие последних обновлений всех пакетов.

```bash
rosdep update
sudo apt-get update
sudo apt-get dist-upgrade
```

Установите MoveIt

```bash
sudo apt install ros-melodic-moveit
```

Перейдите в `catkin_ws/src` и установите зависимости.

```bash
cd ~/catkin_ws/src
rosdep install -y --from-paths . --ignore-src --rosdistro melodic
```

Теперь настройте и собирите ваше рабочее пространсво.

```bash
cd ~/catkin_ws
rosdep install -y --from-paths . --ignore-src --rosdistro melodic
catkin config --extend /opt/ros/${ROS_DISTRO} --cmake-args -DCMAKE_BUILD_TYPE=Release
catkin build
```

Добавьте в ваш `.bashrc` код информацию об обновлённом пространстве?

```bash
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc 
source ~/.bashrc
```

Теперь всё готово для работы с `MoveIt`.

## Jetpack Setup

Для начала обновите все необходимые инструменты

```bash
sudo apt-get update
sudo apt-get install git cmake
```

Клонируйте репозиторий jetson-inference:

```bash
$ git clone https://github.com/dusty-nv/jetson-inference
$ cd jetson-inference
$ git submodule update --init
```

Для работы с Python 3.6 установите следующие пакеты:

```bash
$ sudo apt-get install libpython3-dev python3-numpy
```

Создайте директорию проекта и соберите её.

```bash
cd jetson-inference    # omit if working directory is already jetson-inference/ from above
mkdir build
cd build
cmake ../
```

После загрузки откроется окно установщика моделей нейронных сетей.

:x:

В нём вы можете выбрать интересующие сети или даже все. Выбранные сети отмечаются * (значение можно изменить пробелом). В конце нажмите Enter.

Для запуска загрузчика заново введите это:
```bash
cd jetson-inference/tools
./download-models.sh
```

Теперь соберите весь проект
```bash
cd jetson-inference/build
$ make
$ sudo make install
$ sudo ldconfig
```

Поздравляю! Вы подготовили вашего робота к использованию.

<p align="right">Дальше | <b><a href="40-pin_expansion_header.md">40-контактный разъём расширения</a></b>
<br/>
Назад | <b><a href="setting_up_jetson_nano.md">Настройка Nvidia jetson</a></b></p>
<p align="center"><sup>2021-2022 TRIADOS | </sup><a href="../README.md#содержание"><sup>Содержание</sup></a></p>
