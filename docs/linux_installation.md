# Настройка Nvidia Jetson nano

## Для начала немного теории.

Nvidia Jetson nano - одноплатный компьютер, разработанный компанией nvidia. 
Строение нашего компьютера:
<img src="https://github.com/mook003/Triados/blob/main/docs/images/jetson-nano-dev-kit.png" width="100%">

1 - слот для карты памяти. Т.к. у самого компьютера нет постоянной памяти, мы будем использовать карту памяти

2 - 40-контактный разъем расширения, более конкретное строение которого мы рассмотрим чуть позже

3 - разъем mini-usb

4 - ethernet разъем

5 - разъемы usb-a

6 - разъем HDMI

7 - разъем  display port 

8 - разъем питания на 5V 2A

9 - разъемы MIPI CSI-2 camera connectors

## А теперь давайте начнет работу

### Установка ОС:
1. Скачайте файл для установки [ОС Ubuntu](https://developer.nvidia.com/jetson-nano-sd-card-image).
#### Если если ОС на вашем компьютере Windows:
Отформатируйте SD-карту:
<img scr ="https://github.com/mook003/Triados/blob/main/docs/images/Jetson_Nano-Getting_Started-Windows-SD_Card_Formatter.png" width="100%">  
1. Скачайте, установите и запустите [файл](https://www.sdcard.org/downloads/formatter_4/eula_windows/).
2. Выберите SD-карту.
3. Выберите `Quick format`.
4. Не заполняйте `Volume label`.
5. Нажмите `Format`.
  
Используйте `Etcher` для создания образа (установочного файла) на SD-карте:
1. Скачайте, установите и запустите [Etcher](https://www.balena.io/etcher).
2. Нажмите `Select image` и укажите заархивированный обрвз, скачанный заранее.
3. Подключите SD-кариу, если она еще не подключена.
Если windows вам диалоговое окно по типу этого, согласно [этому объяснению](https://github.com/balena-io/etcher/issues/2024) нажмите `Cancel`.
<img scr ="https://github.com/mook003/Triados/blob/main/docs/images/Jetson_Nano-Getting_Started-Windows-Etcher_Cancel.png" width="100%">
4. Нажмите `Select drive` и выберите нужный диск.
5. Нажмите `Flash!` программе Etcher понадобится примерно 10 минут, если карта поключена через USB3, чтобы обработать и проверить образ.
6. Когда процесс закончится, Windows может сообщить вам, что не знает, как читать карту и предложить вам отформатировать ее. Просто нажите `cancel` и отключите SD-карту.


