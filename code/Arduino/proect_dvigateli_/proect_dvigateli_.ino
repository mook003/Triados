#include "GyverMotor.h" //библиотека для простого взаимодействия с двигателями
GMotor motorR(DRIVER2WIRE, 2, 3, HIGH); //определение пинов для двигателя R
GMotor motorL(DRIVER2WIRE, 4, 5, HIGH); //определение пинов для двигателя L
char key = "0"; //чтение ардуиной ключа
 int val = 0;




void setup() {
  Serial.begin(115200); //частота работы с SerialPort
  Serial.setTimeout(5); //задержка перед вводом я началом работы двигателя(вроде)
  motorR.setMode(AUTO); //если захочешь поменять направление вращения колес, меняй "AUTO" на "REVERSE"
  motorL.setMode(AUTO);
}
void loop() {
if (Serial.available() > 1) {  //не совсем понял, что это значит
  key = Serial.read(); //чтение ардуиной ключа
  val = Serial.parseInt(); //ввод какого-либо числа после ключа и дальнейшая обработка     
  Serial.println(Serial.read());    //(вывод введенных значений в serialport)
  Serial.println(val);
  
  if (key=='r'){ 
      motorR.setSpeed(val);   // команда, позволяющая подать на движок шим сигнал = val
      Serial.println(key);    //(вывод введенных значений в serialport)
      Serial.println(val);   
      digitalWrite(LED_BUILTIN, HIGH);   //
      delay(200);                         // светодиодная индикация
      digitalWrite(LED_BUILTIN, LOW);   //
      delay(100);                                 
 }
  else if (key=='l'){ 
      motorL.setSpeed(val); 
      Serial.println(key);     //(вывод введенных значений в serialport)
      Serial.println(val);  
      digitalWrite(LED_BUILTIN, HIGH);   //
      delay(200);                         // светодиодная индикация
      digitalWrite(LED_BUILTIN, LOW);   //
      delay(100); 
 }
  else if (key=='lr'){ 
      motorL.setSpeed(val); 
      Serial.println(key);     //(вывод введенных значений в serialport)
      Serial.println(val);  
      digitalWrite(LED_BUILTIN, HIGH);   //
      delay(200);                         // светодиодная индикация
      digitalWrite(LED_BUILTIN, LOW);   //
      delay(100);                                               
  }
  key = ' ';
  val = 0;

}
}
/*пример: r255 ("r" - ключ, благодаря которому 
 ардуино понимает, что на правый движок необходимо подать шим "255") */




    
