# Сбор собственных наборов данных для классификации изображений

Для захвата и маркировки изображений на вашем Jetson из видео в реальном времени мы будем использовать инструмент `camera-capture`

Данный инструмент создаёт организационную структуру, ожидаемую сценарием обучения PyTorch

```
‣ train/
	• class-A/
	• class-B/
	• ...
‣ val/
	• class-A/
	• class-B/
	• ...
‣ test/
	• class-A/
	• class-B/
	• ...
```

В представленном примере `class-A`, `class-B` и т.д. являются подкаталогами, содержащими данные для каждого класса объектов, который Вы определили в файле меток классов. Имена этих подкаталогов классов будут соответствовать именам меток классов, которые мы создадим ниже. Эти подкаталоги будут автоматически заполнены инструментом для наборов `train`, `val` и `test` из классов, перечисленных в файле метки, и в каждом из них будет сохранена последовательность изображений JPEG.

## Создание файла меток

В разделе `jetson-inference/python/training/classification/data` создайте пустой каталог для хранения вашего набора данных и текстового файла (обычно называемого `labels.txt`), который будет определять метки классов. Файл меток содержит по одной метке класса в строке, которые расположены в алфавитном порядке (это важно, чтобы порядок классов в файле меток соответствовал порядку соответствующих подкаталогов на диске). Как упоминалось выше, `camera-capture` автоматически заполнит необходимые подкаталоги для каждого класса из этого файла ярлыка.

Вот пример `labels.txt` файла с 5 классами:

```
background
fox
tree
computer_mouse
keyboard
```

И вот соответствующая структура каталогов, которую создаст инструмент:

```
‣ train/
	• background/
	• fox/
	• tree/
	• computer_mouse/
	• keyboard/
‣ val/
	• background/
	• fox/
	• tree/
	• computer_mouse/
	• keyboard/
‣ test/
	• background/
	• fox/
	• tree/
	• computer_mouse/
	• keyboard/
```

## Сбор данных

Для начала запустите инструмент `camera-capture`:

```bash
camera-capture /dev/video0
```

Ниже Вы можете увидеть окно `Data Capture Control`, которое позволяет вам выбрать желаемый путь к набору данных и загрузить файл меток, который Вы создали выше, а затем предоставляет опции для выбора текущего класса объекта и набора `train`/`val`/`test`, для которого вы в данный момент собираете данные:



<p align="right">Дальше | <b><a href="detection_datasets.md">Сбор собственных наборов данных для обнаружения объектов</a></b>
<br/>
Назад | <b><a href="transfer_learning_with_pytorch.md">Трансферное обучение нейронных сетей с PyTorch</a></b></p>
<p align="center"><sup>2021-2023 TRIADOS | </sup><a href="../README.md#содержание"><sup>Содержание</sup></a></p>
