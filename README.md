# Purpose
As I seek to both improve the lives of my plants and learn more about Python development, I've decided to add a light sensor by my plants to evaluate how well they're being fed by the sun and my grow lights.
I hope to use the data to improve growing conditions, particularly in the winter when there's less sunlight.

# Current State
The script reads from the light sensor every 10 minutes and stores that value in the database. Another potential next step is to add more tables to the database to track other pieces of information that I record, such as the daily weight. I'd also like to capture events like watering, repotting, pruning, and so on.

# Potential Next Steps
* Visualize the collected light sensor data
* Migrate light values to plant_events table
* Wire the strain gage for measuring weight
* Create interface for adding new plants
* Create database backup

# Current Tables
* light_vals - Tracks the values coming off the CdS light sensor wired to an Arduino Nano. Will eventually be deprecated by plant_events.
* plant_events - Eventually will track all values recorded by various sensors, their associated plants, and things like watering, repotting, pruning, weighing, and even light.
* plants - Dictionary relating ids used in plant_events and actual plants.
* event_codes - Dictionary correlating events with unique ids.

# Set Up
Python 3 Libraries:
* pyserial
* pymysql
See /setup/README.md for more details on setting up this project, including database setup.
