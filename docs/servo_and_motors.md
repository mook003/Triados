# Код для управления двигателями и сервоприводами

Для начала нужно установить все необходимы библиотеки для передачи данных с компьютера на Arduino и управления сервопроводами с двигателями.
1. Перейдите в `Скетч` > `Подключить библиотеку` > `Управлять библиотеками...` 

<img src=https://github.com/mook003/Triados/blob/main/docs/images/Скриншот%2004-09-2022%20235912.png>

2. После чего в поиске найдите и установите следующие библиотеки:

  a. `iarduino_MultiServo.h`
 
  b. `GParser.h`
  
  c. `GyverMotor.h`
  
3. Скопируйте и вставьте код, приведенный ниже, в Arduino IDE

``` C++
#define pin_SW_SDA A2  // задаем аналоговый порт A2, как линию данных (интерфейс I2C)            
#define pin_SW_SCL A3  // задаем аналоговый порт A3, как линию тактирования (интерфейс I2C)
#include <iarduino_MultiServo.h> // задаем библиотеку для управления сервоприводами        
iarduino_MultiServo MSS;
#include "GParser.h" // задаем библиотеку для передачи данных черех Serial.port
#include "GyverMotor.h" // задаем библиотеку для управления двигателями
GMotor motorR1(DRIVER2WIRE, 2, 3, HIGH); // обозначение пинов, через которые будут подаваться сигналы на двигатели 
GMotor motorL1(DRIVER2WIRE, 4, 5, HIGH); // -||-
GMotor motorR2(DRIVER2WIRE, 7, 6, HIGH); // -||-
GMotor motorL2(DRIVER2WIRE, 8, 9, HIGH); // -||-

void setup() {
  Serial.begin(115200); // задаем частоту передачи данных с Arduino в Serial.port и наоборот
  Serial.setTimeout(5); // задержка в передаче данных
  motorL1.setMode(AUTO); //
  motorR1.setMode(AUTO); // -||-
  motorL2.setMode(AUTO); // -||-
  motorR2.setMode(AUTO); // -||-
  MSS.servoSet(0, SERVO_MG996R); // задаем расположение серовопривода на ШИМ-контроллере и его наименвоание  
  MSS.servoSet(1, SERVO_MG996R); // -||-
  MSS.servoSet(2, SERVO_MG996R); // -||-
  MSS.servoSet(3, SERVO_MG996R); // -||-
  MSS.begin();
}
void loop() {
  if (Serial.available()) {
    char str[30];
    int amount = Serial.readBytesUntil(';', str, 30);
    str[amount] = NULL;
    GParser data(str, ',');
    int ints[5];
    int am = data.parseInts(ints);
  
    switch (ints[0]) {  // ключ
      case 0:
        motorL1.setSpeed(-ints[1]); // скорость 1 мотора
        motorR1.setSpeed(-ints[2]); // скорость 2 мотора
        motorL2.setSpeed(ints[3]); // скорость 3 мотора
        motorR2.setSpeed(-ints[4]); // скорость 4 мотора 
        break;
      case 1:
        MSS.servoWrite(0, ints[1]); // угол поворота 1 сервопривода
        MSS.servoWrite(1, ints[2]); // угол поворота 2 сервопривода
        MSS.servoWrite(2, ints[3]); // угол поворота 3 сервопривода
        MSS.servoWrite(3, ints[4]); // угол поворота 4 сервопривода
        Serial.println((MSS.analogRead(0)-130)/2.13888); // отображение в порте угла поворота сервоприводов
        Serial.println((MSS.analogRead(1)-130)/2.13888); // -||-
        Serial.println((MSS.analogRead(2)-130)/2.13888); // -||-
        Serial.println((MSS.analogRead(3)-130)/2.13888); // -||-
        break;
      }
  }
}
```

4. Как загружать код в Arduino, Вы уже знаете. Так что загружаем и кайфуем)

<p align="right">Дальше | <b><a href="https://github.com/mook003/Triados/blob/main/docs/ros.md">Введение в Ros</a></b>
<br/>
Назад | <b><a href="https://github.com/mook003/Triados/blob/main/docs/4to_takoe_arduino.md">Начало работы с Arduino</a></b></p>
<p align="center"><sup>2021-2023 TRIADOS | </sup><a href="../README.md#содержание"><sup>Содержание</sup></a></p>



```C++
#include <AFMotor.h>
AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor4(4);
#include "GParser.h" // задаем библиотеку для передачи данных черех Serial.port
void setup() {
  Serial.begin(115200); // задаем частоту передачи данных с Arduino в Serial.port и наоборот
  Serial.setTimeout(5); // задержка в передаче данных
  motor1.setSpeed(255);
  motor1.run(RELEASE);
  motor2.setSpeed(255);
  motor2.run(RELEASE);
  motor3.setSpeed(255);
  motor3.run(RELEASE);
  motor4.setSpeed(255);
  motor4.run(RELEASE);
}
void loop() {
  if (Serial.available()) {
    char str[30];
    int amount = Serial.readBytesUntil(';', str, 30);
    str[amount] = NULL;
    GParser data(str, ',');
    int ints[10];
    int am = data.parseInts(ints);
  
    switch (ints[0]) {  // ключ
      case 0:
        motor1.run(ints[1]);               // FORWARD
        motor1.setSpeed(ints[2]);          // RELEASE
        motor2.run(ints[3]);               // BACKWARD
        motor2.setSpeed(ints[4]); 
        motor3.run(ints[5]);
        motor3.setSpeed(ints[6]); 
        motor4.run(ints[7]);
        motor4.setSpeed(ints[8]); 
        break;
      }
  }
}
```
