#include "creds.h"
#include "HX711.h"
#include <WiFi.h>
#include <HTTPClient.h>

#define POLLING_INTERVAL 600000 // In milliseconds
#define DOUT 18
#define CLK 19

HX711 scale;

float calibration_factor = -7050;

// Use 0 for testing to make it easy to remove from the database
int sensor_id = 3;
int event_id = 8;

String serverName = "http://10.0.0.123/remotelight.php";

void setup() 
{
  Serial.begin(115200);
  
  WiFi.begin(NETWORK, PASS);
  while(WiFi.status() != WL_CONNECTED)
  {
    Serial.println("Connecting...");
    delay(500);
  }
  Serial.println("Connected!");
  setupSensor();
}

void loop() 
{
  if(WiFi.status() == WL_CONNECTED)
  {
    HTTPClient http;
    uint16_t val = readSensor();
    Serial.print("Value: ");
    Serial.println(val);
    String query = 
      serverName + 
      "?val=" + val + 
      "&sid=" + sensor_id + 
      "&eid=" + event_id;
    
    http.begin(query.c_str());
    int httpResponse = http.GET();

    http.end();
    delay(POLLING_INTERVAL);
  }
}

// Here is where you should place all of your sensor setup code
void setupSensor()
{
  scale.begin(DOUT, CLK);
  scale.set_scale();
  scale.tare();

  delay(1000);

  scale.tare();
}

// Place your sensor reading code here
uint16_t readSensor()
{
  scale.set_scale(calibration_factor);

  float rawRead = scale.get_units();
  float slope = (0.605605 + 0.60194) / 2.0;
  float adjRead = rawRead * slope;
  Serial.println(adjRead);
  
  return (uint16_t)(adjRead * 100);
}
