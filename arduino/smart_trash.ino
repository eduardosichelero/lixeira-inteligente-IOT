#include <Servo.h>

const int botaoPin = 2;
const int servoPin = 6;

Servo servo;
bool aberta = false;

void setup() {
  pinMode(botaoPin, INPUT_PULLUP);
  servo.attach(servoPin);
  servo.write(0);
  Serial.begin(9600);
}

void loop() {
  if(digitalRead(botaoPin) == HIGH) {
    Serial.println("Botão pressionado");
    toggleTampa();
    delay(500); 
  }
}

void toggleTampa() {
  if(aberta) {
    servo.write(0);
    Serial.println("Tampa fechada");
  } else {
    servo.write(90);
    Serial.println("Abrindo tampa");
    delay(3000);
    Serial.println("Tampa aberta");
  }
  aberta = !aberta;
}
