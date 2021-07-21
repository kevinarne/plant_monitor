//#include "creds.h"
#include "HX711.h"
#include <WiFi.h>
#include <HTTPClient.h>
//#include <ESPAsyncWebServer.h>
#include <Preferences.h>

#define POLLING_INTERVAL 600000 // In milliseconds
#define DOUT 18
#define CLK 19

HX711 scale;

float calibration_factor = -7050;

// Use 0 for testing to make it easy to remove from the database
int sensor_id = 0;
int event_id = 0;

String serverName = "http://10.0.0.123/remotelight.php";
const char* eename;
const char* eepass;
Preferences prefs;

void setup() 
{
  Serial.begin(115200);
  prefs.begin("weight", false);
  // Check EEPROM for network ID and password
  if (prefs.getString("SSID").length()>0 && prefs.getString("PASS").length()>0)
  {
    eename = prefs.getString("SSID").c_str();
    Serial.println("Network name found"); 
    Serial.println(eename); 
    eepass = prefs.getString("PASS").c_str();
    Serial.println("Network password found");
    Serial.println(eepass);
  }
  else
  {
    eename = "null";
    eepass = "null";
    Serial.println("Network name not found");
    //prefs.putString("SSID", NETWORK);   
  }
  prefs.end();
    // If exists, attempt to connect
  
  WiFi.begin(eename, eepass);
  while(WiFi.status() != WL_CONNECTED)
  {
    Serial.println("Connecting...");
    delay(500);
  }
  Serial.println("Connected!");
  //setupSensor();
}

void loop() 
{
  if(WiFi.status() == WL_CONNECTED)
  {
    // Serve status webpage
    // Log values
    HTTPClient http;
    //uint16_t val = readSensor();
    uint16_t val = 100;
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
  else
  {
    // Serve login webpage
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
  Serial.println(scale.get_offset());
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

boolean isWifiConnected()
{
  for (int i = 0; i < 10; i++)
  {
    if (WiFi.status() == WL_CONNECTED)
    {
      return true;
    }  
    delay(250);
    Serial.print(".");
  }
  return false;
}

void serveLogin()
{

}

void serveStatus()
{
  
}
