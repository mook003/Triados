# Разъем камеры MIPI CSI-2 

## Что такое MIPI

MIPI Alliance (Mobile Industry Processor Interface Alliance) - это ассоциация, в которой состоят почти все производители программного обеспечения и оборудования в индустрии мобильной связи и электроники для развлечений. Ее основная цель заключается в стандартизации всех важных интерфейсов, обеспечивающих взаимодействие между процессором мобильного устройства и периферийными компонентами (сенсоры, камеры, интерфейсы ввода, дисплеи и т.д.). Благодаря этому производителям периферии для мобильных устройств проще адаптировать свои компоненты к различным типам процессоров, а производителям процессоров доступен более широкий ассортимент потенциально совместимых периферийных устройств. Таким образом, обе стороны получают выгоду за счет экономии на процессах разработки и производства.

<img src="https://github.com/mook003/Triados/blob/main/docs/images/mipi_csi2.jpg" width="100%">

## Преймущества данного разъема:
* Компактен блягодаря плоскому гибкому кабелю 
* Данные изображения могут передаваться непосредственно от модуля камеры или сенсора на процессор
* Низкое ресурсопотребление 
* Высокая пропускная способность
* Дешевизна

## Ограничения данного разъема
* Длина кабеля до 20-30см. Для таких устройств как смартфоны это не принципиально, однако может стать проблемой для промышленных систем.
* Нет стандартного разъема, из-за чего обычно требуется адаптация аппаратного обеспечения, например с помощью адаптерной платы
* В стандарте MIPI CSI-2 не определены ни стек драйверов, ни программный стек. Как правило, разработчику необходимо специально адаптировать сенсор или модуль камеры для использования с драйвером CSI-2 или выбранной однокристальной системой (SoC). При выборе сенсора (модуля) камеры, разработанного под SoC, следует убедиться в наличии соответствующих драйверов. Это сужает выбор сенсоров и однокристальных систем
* Большинство драйверов CSI-2 поддерживают только лишь несколько форматов изображения
* Все функции камеры расскрываются только блягодаря стандарту камеры API

## Итог
Интерфейс MIPI CSI-2 идеально подходит для встраиваемых систем машинного зрения, для которых важными факторами выступают низкое ресурсопотребление и доступная стоимость. 

<p align="right">Дальше | <b><a href="12-pin_header.md">12-контактный разъём</a></b>
<br/>
Назад | <b><a href="setting_up_jetson_nano.md#moveit.md">40-контактный разъём расширения</a></b></p>
<p align="center"><sup>2021-2023 TRIADOS | </sup><a href="../README.md#содержание"><sup>Содержание</sup></a></p>
