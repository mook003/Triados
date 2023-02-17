# Настройка Nvidia Jetson nano

## Для начала немного теории.

Nvidia Jetson nano - одноплатный компьютер, разработанный компанией nvidia. 
Строение нашего компьютера:

<img src="https://github.com/mook003/Triados/blob/main/docs/images/jetson-nano-dev-kit.png" width="100%">

1 - слот для карты памяти. Т.к. у самого компьютера нет постоянной памяти, мы будем использовать карту памяти

2 - 40-контактный разъем расширения, более конкретное строение которого мы рассмотрим чуть позже

3 - разъем mini-usb (5V)

4 - Gigabit Ethernet разъем

5 - разъемы USB 3.0

6 - разъем HDMI

7 - разъем  DisplayPort 

8 - разъем DC Barrel для питания на 5V 2A

9 - разъемы MIPI CSI-2 camera connectors

> **note:** Разьём mini-usb можно использовать для питания или для подключения к другому компьютеру, если питание подаётся на DC Barrel.

## А теперь давайте начнём работу

### Создание образа(установочного файла) на microSD карте:
1. Скачайте образ для установки [ОС Ubuntu](https://developer.nvidia.com/jetson-nano-sd-card-image).
2. Затем, в зависимости от того, какая ОС установлена на ваш компьютер, создайте образ на microSD карте:
   - [Инструкции для Windows](#если-на-вашем-компьютере-стоит-windows)
   - [Инструкции для Mac](#если-на-вашем-компьютере-стоит-macos)
   - [Инструкции для Linux](#инструкции-для-linux)
#### Для компьютеров на базе Windows:
Отформатируйте SD-карту:

<img src="https://github.com/mook003/Triados/blob/main/docs/images/imageWINDOWS/Card_Formatter.png" width="50%">

1. Скачайте, установите и запустите [прогурамму дя форматирования microSD карты](https://www.sdcard.org/downloads/formatter_4/eula_windows/).
2. Выберите microSD карту.
3. Выберите `Quick format`.
4. Не заполняйте `Volume label`.
5. Нажмите `Format`.
  
Используйте `Etcher` для создания образа на microSD карте:
1. Скачайте, установите и запустите [Etcher](https://www.balena.io/etcher). 

<img src="https://github.com/mook003/Triados/blob/main/docs/images/imageWINDOWS/Windows-Etcher.png" width="50%">

2. Нажмите `Select image` и укажите заархивированный образ, скачанный заранее.
3. Подключите microSD карту, если она еще не подключена.
Если windows выведет вам диалоговое окно по типу этого, согласно [этому объяснению](https://github.com/balena-io/etcher/issues/2024) нажмите `Cancel`.

<img src="https://github.com/mook003/Triados/blob/main/docs/images/imageWINDOWS/Etcher_Cancel.png" width="50%">

4. Нажмите `Select drive` и выберите нужный диск.

<img src="https://github.com/mook003/Triados/blob/main/docs/images/imageWINDOWS/Etcher_Select_Drive.png" width="50%">

5. Нажмите `Flash!` программе Etcher понадобится примерно 10 минут, если карта поключена через USB3, чтобы обработать и проверить образ.
6. Когда процесс закончится, Windows может сообщить вам, что не знает, как читать карту и предложить вам отформатировать ее. Просто нажите `Cancel` и отключите microSD карту.

<img src="https://github.com/mook003/Triados/blob/main/docs/images/imageWINDOWS/Etcher_Cancel.png" width="50%">

После того как microSD карта готова, можно перейти к [настройке ос на Nvidia Jetson Nano](#настройка-и-первый-запуск)


#### Для компьютеров на базе MACOS:

Вы можете записать образ с помощью графической программы по типу [Etcher](#%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%86%D0%B8%D0%B8-%D0%B4%D0%BB%D1%8F-etcher) или с [помощью командной строки](#иструкции-для-командной-строки)
###### Инструкции для Etcher
1. Скачайте, установите и запустите [Etcher](https://www.balena.io/etcher).

<img src="https://github.com/mook003/Triados/blob/main/docs/images/imageMACOS/Mac-Etcher.png" width="50%">

2. Нажмите `Select image` и укажите заархивированный обрaз, скачанный заранее.
3. Вставьте вашу microSD карту и нажмите `Ignore`, если появится это окно:

<img src="https://github.com/mook003/Triados/blob/main/docs/images/imageMACOS/Mac-Disk_readable.png" width="50%">

4. Если у Вас не подключено других внешних носителей, то Etcher автоматически выберет microSD карту. В противном случае нажмите `Select drive` и выберите нужный диск.
5. Нажмите `Flash!`. Ваш Mac может запросить ваш ник и пароль прежде чем позволит программе продолжить.

<img src="https://github.com/mook003/Triados/blob/main/docs/images/imageMACOS/Mac-Etcher_permission.png" width="50%">
Программе понадобится примерно 10 минут, если карта поключена через USB3, чтобы обработать и проверить образ.

6. Когда процесс закончится, Мас может сообщить вам, что не знает, как читать карту и предложить вам отформатировать ее. Просто нажите `Eject` и отключите SD-карту.

<img src="https://github.com/mook003/Triados/blob/main/docs/images/imageMACOS/Mac-Disk_readable.png" width="50%">

После того как SD-карта готова, можно перейти к [настройке ос на Nvidia Jetson Nano](#настройка-и-первый-запуск)


##### Иструкции для командной строки

1. Откройте терминал

<img src="https://github.com/mook003/Triados/blob/main/docs/images/imageMACOS/Mac-Terminal_app.png" width="50%">

2. Введите эту команду, чтобы увидеть список всех внешних носителей 
```bash
diskutil list external | fgrep '/dev/disk'
```
Например, если к вашему компьютеру уже подключен USB накопитель, то результат будет примерно таким:

<img src="https://github.com/mook003/Triados/blob/main/docs/images/imageMACOS/Mac-Terminal_disk_already_attached.png" width="50%">

3. Вставьте вашу microSD карту. Нажмите `Ignore`, если ваш Mac покажет вам это окно

<img src="https://github.com/mook003/Triados/blob/main/docs/images/imageMACOS/Mac-Disk_readable.png" width="50%">

4. Используйте команду, что и до этого, чтобы вывести список. В списке будет новое устройство - microSD карта в данном примере: `/dev/disk2`

<img src="https://github.com/mook003/Triados/blob/main/docs/images/imageMACOS/Mac-Terminal_list_disks.png" width="50%">

5. Используйте следующую команду, чтобы форматировать microSD карту.
> **note:** Форматирование дтска - процесс разметки области хранения данных электронных носителей информации, в результате которого хранилище будет полностью очищенным. Будьте осторожны! Указав неправильный носитель, вы можете потерять свои данные
```bash
sudo diskutil partitionDisk /dev/disk<n> 1 GPT "Free Space" "%noformat%" 100%
```
Например:

<img src='https://github.com/mook003/Triados/blob/main/docs/images/imageMACOS/Mac-Terminal_partitions.png' width='50%'>

6. Используйте эту команду чтобы записать заархивированный образ на microSD карту. Используйте `/dev/rdisk` вместо `/dev/disk`.
```bash
/usr/bin/unzip -p ~/Downloads/jetson_nano_devkit_sd_card.zip | sudo /bin/dd of=/dev/rdisk<n> bs=1m
```
<img src='https://github.com/mook003/Triados/blob/main/docs/images/imageMACOS/Mac-Terminal_write_zipped_SD_card.png' width='50%'>

7. Индикации процесса не будет (только если вы не нажмете CTRL+t). Когда процесс завершится ваш устройство выведет предупреждение, что не может прочитать microSD карту. Просто нажмите `Eject`

<img src="https://github.com/mook003/Triados/blob/main/docs/images/imageMACOS/Mac-Disk_readable.png" width="50%">

После того как SD-карта готова, можно перейти к [настройке ос на Nvidia Jetson Nano](#настройка-и-первый-запуск)

#### Для компьютеров на базе LINUX:

Вы можете записать образ с помощью графической программы по типу [Etcher](#%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%86%D0%B8%D0%B8-%D0%B4%D0%BB%D1%8F-etcher) или с [помощью командной строки](#инструкции-для-командной-строки)

##### Инструкции для Etcher
1. Скачайте, установите и запустите [Etcher](https://www.balena.io/etcher). 

<img src="https://github.com/mook003/Triados/blob/main/docs/images/imageLINUX/Linux-Etcher.png" width="50%">

2. Нажмите `Select image` и укажите заархивированный образ, скачанный заранее.
3. Подключите SD-карту, если она еще не подключена. Если у вас не подключены другие внешние носители, то Etcher автоматически выберет microSD карту. В противном случае нажмите `Change` и выберите microSD карту.

<img src="https://github.com/mook003/Triados/blob/main/docs/images/imageLINUX/Linux-Etcher_Select_Drive.png" width="50%">

4. Нажмите `Flash!`. Ваш ОС может запросить ваше имя пользователя и пароль прежде чем позволит программе продолжить.

<img src="https://github.com/mook003/Triados/blob/main/docs/images/imageLINUX/Linux-Etcher_Password.png" width="50%">

Программе понадобится примерно 10-15 минут, если карта поключена через USB3, чтобы обработать и проверить образ.
5. Когда Etcher закончит, извлеките microSD карту с помощью проводника. 

<img src="https://github.com/mook003/Triados/blob/main/docs/images/imageLINUX/Linux-Files_App.png" width="50%">

6. Вытащите карту из компьютера

После того как SD-карта готова, можно перейти к [настройке ос на Nvidia Jetson Nano](#настройка-и-первый-запуск)

##### Инструкции для командной строки 

1. Откройте терминал с помощью комбинации клавиш `Ctrl+Alt+t`
2. Вставьте microSD карту. Затем введите эту команду что увидеть, как она назначена компьютером.
```bash
dmesg | tail | awk '$3 == "sd" {print}'
```
В этом примере мы видим, что 16гб microSD карта была назначена как `/dev/sda`:

<img src="https://github.com/mook003/Triados/blob/main/docs/images/imageLINUX/Jetson_Nano-Getting_Started-Linux-Terminal_Disk_Assign.png" width="50%">

3. Введите эту команду, чтобы записать заархивированный на microSD карту.
```bash
/usr/bin/unzip -p ~/Downloads/jetson_nano_devkit_sd_card.zip | sudo /bin/dd of=/dev/sd<x> bs=1M status=progress
```
Пример:

<img src="https://github.com/mook003/Triados/blob/main/docs/images/imageLINUX/Linux-Terminal_Disk_Write.png" width="50%">

4. Когда процесс завершится, извлеките microSD карту командой
```bash
sudo eject /dev/sd<x>
```
После того как SD-карта готова, можно перейти к [настройке ос на Nvidia Jetson Nano](#настройка-и-первый-запуск)


### Настройка и первый запуск

Есть 2 способа взаимодкйствия с nvidia jetson nano:
1. [Как с обычным компьютером, спомощью клавиатуры, компьютерной мыши и монитора]()
2. [И с помощью дополнительного компьютера]()

| | НАТСРОЙКА С МОНИТОРОМ | НАСТРОЙКА С ПОМОЩЬЮ ДОП. КОМПЬЮТЕРА |
|-----------------|:-----------:|:------------:|
| Клавиатура, мышь и монитор | Нужны | Не нужны |
| Дополнительный компьютер | Не нужен | Нужен |
| Питание | разъем питания на 5V 2A или micro-USB разъем | Только разъем питания на 5V 2A |

#### Настройка с подключенным монитором 

<img src="https://github.com/mook003/Triados/blob/main/docs/images/1setupWITHMONITOR/Jetbot_animation_500x282_2.gif" width="50%">

##### Порядок установки:
1. Распакуйте бумажную подскавку и поместите ее в коробку 
2. Вставьте microSD карту с предустановленным на нее образом linux в слот, находящийся в задней части модуля

<img src="https://github.com/mook003/Triados/blob/main/docs/images/1setupWITHMONITOR/Insert_microSD-B01.png" width="50%">

3. Расположите компьютер на бумажной подставке
4. Включите монитор и подключите его
5. Подключите клавиатуру и мышь через USB
6. Подключите питание через разъем micro-USB (или посмотрите [Jetson Nano Developer Kit User Guide](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#) для получения более подробной информации об использовании цилиндрического разъема питания). Модуль включится и загрузится автоматически.

##### Первый запуск

Как только Jetson nano ыключится, рядом с разъемом micro-USB загорится зеленый светодиод. При первом запуске вам нужно будет пройти некоторые начальный настройки, в том числе:
* лицензионное соглашение
* выбор языка, раскладки клавиатуры и часового пояса
* создание имени пользователя, пароля и псевдонима
* выбор размера ярлыков приложений, рекомендуется выбрать максимальный из предлагаемых

##### После входа в систему

Вы увидите такой экран. Поздравляем!

<img src="https://github.com/mook003/Triados/blob/main/docs/images/1setupWITHMONITOR/desktop.png" width="50%">

<p align="right">Дальше | <b><a href="setting_up_jetson_nano.md">Настройка Nvidia jetson</a></b>
<br/>
</p>
<p align="center"><sup>2021-2023 TRIADOS | </sup><a href="../README.md#содержание"><sup>Содержание</sup></a></p>
