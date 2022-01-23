# Purpose
As I seek to both improve the lives of my plants and learn more about Python development, I've decided to start instrumenting my plants with some sensors like light and weight sensors.

# Current State
There are three kinds of sensors currently supported: CdS light sensor hooked up to an Arduino (directly connected to Pi via serial), CdS light sensor hooked up to an ESP32 (wireless), and load cell hooked up to an ESP32 (wireless). Each of these connects to a Raspberry Pi-hosted MySQL database on my local network.

The wireless sensors add data to the database via an HTTP request handled by a PHP script on the local server. The wired sensor is polled via serial regularly by a python script scheduled with crontab.

# Current Event Types
* 10-bit CdS light sensor (wired Arduino Nano)
* 12-bit CdS light sensor (wireless ESP32)
* Manual weighing
* Load cell weighing (wireless ESP32)
* Wiring (for shaping trees)
* Removed wire
* Root pruning
* Plant status (out of 5 stars)

# Potential Next Steps
* Visualize the collected light sensor data
* Create more ESP32-powered sensors
* Migrate from serial light sensor to ESP32 light sensor
* Add a user id column to the plant_events, sensors, and plants tables
* Convert to Flask
* Add web page to store wireless connections to ESP32 sketches
* Store tare value in EEPROM on ESP32

# Flask Conversion Next Steps
* Create routes.py
* Migrate database to an sqlite database
* Create user database
* Create web interface for adding weight
* Create plant status page
* 

# Current Tables
* plant_events - Tracks values recorded by various sensors, their associated plants, and things like watering, repotting, pruning, weighing, and even light. Currently it only tracks light.
* plants - Dictionary relating ids used in plant_events and actual plants.
* event_codes - Dictionary correlating events with unique ids.
* sensors - Details of the sensors.


# Set Up
Python 3 Libraries:
* datetime
* itertools
* python-decouple
* pyserial
* pymysql
* matplotlib
* numpy
* smtplib

See /setup/README.md for more details on setting up this project, including database setup.
