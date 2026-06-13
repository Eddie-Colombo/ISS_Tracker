int northLED = 2;
int eastLED  = 3;
int southLED = 4;
int westLED  = 5;

void setup() {
  pinMode(northLED, OUTPUT);
  pinMode(eastLED, OUTPUT);
  pinMode(southLED, OUTPUT);
  pinMode(westLED, OUTPUT);
}

void loop() {
  digitalWrite(northLED, LOW);
  delay(1000);
  digitalWrite(northLED, HIGH);
  digitalWrite(eastLED, LOW);
  delay(1000);
  digitalWrite(eastLED, HIGH);
  digitalWrite(southLED, LOW);
  delay(1000);
  digitalWrite(southLED, HIGH);
  digitalWrite(westLED, LOW);
  delay(1000);
  digitalWrite(westLED, HIGH);
}