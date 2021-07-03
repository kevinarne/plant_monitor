#include "creds.h"
#include <WiFi.h>
#include <HTTPClient.h>

#define POLLING_INTERVAL 600000 // In milliseconds

// Use 0 for testing to make it easy to remove from the database
int sensor_id = 0;
int event_id = 0;

String serverName = "localhost";

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

}

// Place your sensor reading code here
uint16_t readSensor()
{
  return 1;
}
