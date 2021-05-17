# Purpose
As I seek to both improve the lives of my plants and learn more about Python development, I've decided to add a light sensor by my plants to evaluate how well they're being fed by the sun and my grow lights.
I hope to use the data to improve growing conditions, particularly in the winter when there's less sunlight.

# Current State
The script reads from the light sensor every 10 minutes and stores that value in the database. Next step is to record some data for a while and look for patterns. Another potential next step is to add more tables to the database to track other pieces of information that I record, such as the daily weight. I'd also like to capture events like watering, repotting, pruning, and so on.

# Set Up
Python 3 Libraries:
* pyserial
* pymysql
See /setup/README.md for more details on setting up this project, including database setup.

