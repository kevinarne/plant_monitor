# Required libraries
* mariadb


# Initializing the database
Start by updating your pi:
sudo apt update
sudo apt upgrade
Install the server software
sudo apt install mariadb-server

Install the Python module:
pip3 install mariadb

Run secure installation (set up root password):
sudo mysql_secure_installation
* set a password
* remove anonymous users
* disallow root login remotely
* remove the test database
* reload privileges

Create new user:
sudo mysql -uroot -p
CREATE DATABASE <dbname>;
CREATE USER '<username>'@'localhost' IDENTIFIED BY '<password>';
GRANT ALL PRIVILEGES ON <dbname>.* TO '<username>'@'localhost';
FLUSH PRIVILEGES;

Create a credentials file
nano credentials
Format with username on the first line and password on the second line. Save and exit (ctrl-s and ctrl-x)

Initialize the table in the database
run lightdbhandler.py

You're all set.
