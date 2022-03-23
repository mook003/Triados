# I2C

I2C - последовательная асимметричная шина для связи между интегральными схемами. Для передачи информации используются две двунаправленные линии связи (SDA и SCL). 

На Nvidia Jetson это реализовано на пинах 3, 5 и 27, 28. 

Для примера разберём подключение драйвера 12-битного драйвера PWM/Servo PCA9685.

Для её работы потребуется библиотека Adafruit ServoKit.

```bash
git clone https://github.com/JetsonHacksNano/ServoKit
cd ServoKit
./installServoKit.sh
```

Теперь соедините
```
Pin 3 (SDA) -> PCA9685 SDA
J41 Pin 5 (SCL) -> PCA9685 SCL
J41 Pin 1 (3.3V) -> PCA9685 VCC
J41 Pin 6 (GND) -> PCA9685 GND
```

<p align="right">Next | <b><a href="UART.md">UART</a></b>
<br/>
Back | <b><a href="40-pin_expansion_header.md">40-контактный разъем расширения</a></b></p>
<p align="center"><sup>2021-2022 TRIADOS | </sup><a href="../README.md#содержание"><sup>Содержание</sup></a></p>
