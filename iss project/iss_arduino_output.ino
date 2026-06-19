// ISS Compass LED pins
int northLED = 2;
int eastLED  = 3;
int southLED = 4;
int westLED  = 5;


// Setup runs once when Arduino starts
void setup() {

  pinMode(northLED, OUTPUT);
  pinMode(eastLED, OUTPUT);
  pinMode(southLED, OUTPUT);
  pinMode(westLED, OUTPUT);

  Serial.begin(9600);
}


// Turn every LED off
void allOff() {

  digitalWrite(northLED, HIGH);
  digitalWrite(eastLED, HIGH);
  digitalWrite(southLED, HIGH);
  digitalWrite(westLED, HIGH);
}


void loop() {

  if (Serial.available() > 0) {

    // Read direction sent by Python
    String direction = Serial.readStringUntil('\n');

    // Remove spaces/new line problems
    direction.trim();

    // Turn everything off before showing new direction
    allOff();


    // North
    if (direction == "N") {
      digitalWrite(northLED, LOW);
    }

    // East
    else if (direction == "E") {
      digitalWrite(eastLED, LOW);
    }

    // South
    else if (direction == "S") {
      digitalWrite(southLED, LOW);
    }

    // West
    else if (direction == "W") {
      digitalWrite(westLED, LOW);
    }


    // North-East
    else if (direction == "NE") {
      digitalWrite(northLED, LOW);
      digitalWrite(eastLED, LOW);
    }


    // North-West
    else if (direction == "NW") {
      digitalWrite(northLED, LOW);
      digitalWrite(westLED, LOW);
    }


    // South-East
    else if (direction == "SE") {
      digitalWrite(southLED, LOW);
      digitalWrite(eastLED, LOW);
    }


    // South-West
    else if (direction == "SW") {
      digitalWrite(southLED, LOW);
      digitalWrite(westLED, LOW);
    }


    // Send received direction back for testing
    Serial.println(direction);
  }
}
