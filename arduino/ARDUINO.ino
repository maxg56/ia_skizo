// Définition des broches pour le module ultrason
#define TRIG_PIN 4
#define ECHO_PIN 5


// Variables pour mesurer la distance
long duration;
int distance;

void setup() {

  Serial.begin(9600);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

void loop() {
  digitalWrite(TRIG_PIN, LOW);  
  delayMicroseconds(2);  
  digitalWrite(TRIG_PIN, HIGH);  
  delayMicroseconds(10);  
  digitalWrite(TRIG_PIN, LOW);  
  duration = pulseIn(ECHO_PIN, HIGH);

  distance = duration * 0.0344 / 2;
  Serial.print(distance);
   Serial.print('\n');
  delay(100);
}