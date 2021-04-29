# Purpose
As I seek to both improve the lives of my plants and learn more about Python development, I've decided to add a light sensor by my plants to evaluate how well they're being fed by the sun and my grow lights.
I hope to use the data to improve growing conditions, particularly in the winter when there's less sunlight.

# Current Issues
The Rapberry Pi Zero W I'm using can read the 10 bit values (0-1023) of the voltage coming off a CdS light dependent resistor in a voltage divider (known resistor is 10k).
Those values need some light processing and storage in a database.

# Set up
Python 3 Libraries:
* pyserial
* pymysql

