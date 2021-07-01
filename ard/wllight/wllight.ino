#include "creds.h"
#include <WiFi.h>
#include <HTTPClient.h>

#define CDS_PIN 34

String serverName = "http://10.0.0.123/remotelight.php";

void setup() 
{
  Serial.begin(115200);
  //pinMode(CDS_PIN, INPUT);
  
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
    uint16_t val = analogRead(CDS_PIN);
    Serial.print("Value: ");
    Serial.println(val);
    String query = serverName + "?val="+val+"&sid=1&eid=0";
    
    http.begin(query.c_str());
    int httpResponse = http.GET();
    //Serial.println(httpResponse);
    http.end();
    delay(60000);
  }
}

uint16_t readSensor()
{
  return analogRead(CDS_PIN);
}
