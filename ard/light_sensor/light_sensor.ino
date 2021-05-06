#define CDS_PIN A0
void setup() {
  pinMode(A0, INPUT);
  Serial.begin(9600);
}

void loop() {
  uint16_t sensor_read = analogRead(A0);
  Serial.println(sensor_read);
}
