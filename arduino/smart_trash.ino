#include <Servo.h>

Servo servo;
const int servoPin = 6; 

void setup() {
  Serial.begin(9600);
  servo.attach(servoPin);
  servo.write(0); 
}

void loop() {
  if (Serial.available() > 0) {
    String comando = Serial.readStringUntil('\n');
    comando.trim();
    
    if (comando == "abrir") {
      servo.write(90); 
      Serial.println("Tampa aberta!");
    } 
    else if (comando == "fechar") {
      servo.write(0); 
      Serial.println("Tampa fechada!");
    }
  }
}
