#include "creds.h"
#include <WiFi.h>
#include <HTTPClient.h>

#define CDS_PIN 2

String serverName = "http://10.0.0.123/remotelight.php";

void setup() 
{
  Serial.begin(115200);
  pinMode(CDS_PIN, INPUT);
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
    
    String query = serverName + "?val=198&sid=2&eid=1";
    
    http.begin(query.c_str());
    int httpResponse = http.GET();
    Serial.println(httpResponse);
    http.end();
    delay(2000);
  }
}
