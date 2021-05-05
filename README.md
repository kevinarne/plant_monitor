# Purpose
As I seek to both improve the lives of my plants and learn more about Python development, I've decided to add a light sensor by my plants to evaluate how well they're being fed by the sun and my grow lights.
I hope to use the data to improve growing conditions, particularly in the winter when there's less sunlight.

# Current State
The script can read sensor values in response to prompting from the menu and deposit that value in the light_vals table of the lights database.
I'd like it to be able to automatically read from the sensor at regular intervals.
Arduino code and schematic for the light sensor need to be added to the repo.


# Set up
Python 3 Libraries:
* pyserial
* pymysql
See /setup/README.md for more details on setting up this project, including database setup.

