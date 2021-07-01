#include "creds.h"
#include <WiFi.h>
#include <HTTPClient.h>

#define POLLING_INTERVAL 60000 // In milliseconds

#define CDS_PIN 34

// Use 0 for testing to make it easy to remove from the database
int sensor_id = 0;
int event_id = 0;

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
  Serial.println("Connection successful!");
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

uint16_t readSensor()
{
  return analogRead(CDS_PIN);
}
