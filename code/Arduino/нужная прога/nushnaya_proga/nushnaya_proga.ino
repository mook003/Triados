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
        motorL1.setSpeed(ints[1]);
        motorR1.setSpeed(ints[2]);  
        motorL2.setSpeed(ints[3]);
        motorR2.setSpeed(ints[4]); 
        digitalWrite(LED_BUILTIN, HIGH);   
        delay(200);                        
        digitalWrite(LED_BUILTIN, LOW);   
        delay(100);      
        break;
      Serial.println(ints[0]);
      }
  }
}
