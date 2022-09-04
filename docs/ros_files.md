# Типы файлов ROS

В ROS существует множество файлов. В данном разделе мы опишем некоторые из них, объясним как их создавать и как ими пользоваться.

## Launch файл

Важной частью ROS являются топики, но запускать кадый из них отедльно неудобно. Для этого существует файлы формата `launch`. Они основаны на расширяемом языке разметки XML. 

Для начала давайте создадим простой файл запуска. Перейдите в ранее созданный проект для `Publisher и Subscriber` командой `roscd` и создайте файл.

```bash
touch nodes/test.launch
```

Откройте новый файл и вставьте следующий код

```xml
<launch>
  <node pkg="test_package" type="topic_publisher.py" name="topic_publisher1"/>
  <node pkg="test_package" type="topic_subscriber" name="topic_subscriber1"/>
  <node pkg="test_package" type="topic_publisher.py" name="topic_publisher2"/>
  <node pkg="test_package" type="topic_subscriber" name="topic_subscriber2"/>
</launch>
```

<p align="right">Next | <b><a href="zed.md">Работа с ZED</a></b>
<br/>
Back | <b><a href="ros.md">Введение в ROS</a></b></p>
<p align="center"><sup>2021-2022 TRIADOS | </sup><a href="../README.md#содержание"><sup>Содержание</sup></a></p>
