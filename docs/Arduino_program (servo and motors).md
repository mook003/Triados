``` c++

#define pin_SW_SDA A2             
#define pin_SW_SCL A3   
#include <iarduino_MultiServo.h>        
iarduino_MultiServo MSS;
#include "GParser.h"
#include "GyverMotor.h" 
GMotor motorR1(DRIVER2WIRE, 2, 3, HIGH); 
GMotor motorL1(DRIVER2WIRE, 4, 5, HIGH);
GMotor motorR2(DRIVER2WIRE, 7, 6, HIGH); 
GMotor motorL2(DRIVER2WIRE, 8, 9, HIGH);

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(5);
  motorL1.setMode(AUTO); 
  motorR1.setMode(AUTO);
  motorL2.setMode(AUTO); 
  motorR2.setMode(AUTO);
  MSS.servoSet(0, SERVO_MG996R);  
  MSS.servoSet(1, SERVO_MG996R); 
  MSS.servoSet(2, SERVO_MG996R);  
  MSS.servoSet(3, SERVO_MG996R);  
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
        digitalWrite(LED_BUILTIN, HIGH);   
        delay(200);                        
        digitalWrite(LED_BUILTIN, LOW);   
        delay(100);      
        break;
      case 1:
        MSS.servoWrite(0, ints[1]); // угол поворота 1 сервопривода
        MSS.servoWrite(1, ints[2]); // угол поворота 2 сервопривода
        MSS.servoWrite(2, ints[3]); // угол поворота 3 сервопривода
        MSS.servoWrite(3, ints[4]); // угол поворота 4 сервопривода
        Serial.println((MSS.analogRead(0)-130)/2.13888);
        Serial.println((MSS.analogRead(1)-130)/2.13888);
        Serial.println((MSS.analogRead(2)-130)/2.13888);
        Serial.println((MSS.analogRead(3)-130)/2.13888);
        break;
      }
  }
}

```
