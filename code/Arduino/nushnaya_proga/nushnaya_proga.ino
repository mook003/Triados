#include "GParser.h"
#include "GyverMotor.h" 
GMotor motorR(DRIVER2WIRE, 2, 3, HIGH); 
GMotor motorL(DRIVER2WIRE, 4, 5, HIGH);

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(5);
  motorL.setMode(AUTO); 
  motorR.setMode(AUTO);
}


void loop() {
  if (Serial.available()) {
    char str[30];
    int amount = Serial.readBytesUntil(';', str, 30);
    Serial.println("dwdwdwd");
    /*digitalWrite(LED_BUILTIN, HIGH);   
    delay(200);                        
    digitalWrite(LED_BUILTIN, LOW);   
    delay(100);
    digitalWrite(LED_BUILTIN, HIGH);   
    delay(200);                        
    digitalWrite(LED_BUILTIN, LOW);   
    delay(100);*/
    str[amount] = NULL;
    GParser data(str, ',');
    int ints[5];
    int am = data.parseInts(ints);
  
    switch (ints[0]) {  // ключ
      case 0:
        motorL.setSpeed(ints[1]);
        motorR.setSpeed(ints[2]);   
        digitalWrite(LED_BUILTIN, HIGH);   
        delay(200);                        
        digitalWrite(LED_BUILTIN, LOW);   
        delay(100);      
        break;
      Serial.println(ints[0]);
      }
  }
}
