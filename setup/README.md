# Required libraries
* mariadb
* pymysql
* datetime
* pyserial

# Initializing the database
Start by updating your pi:
sudo apt update
sudo apt upgrade
Install the server software
sudo apt install mariadb-server

# Install the Python module:
pip3 install mariadb

# Run secure installation (set up root password)
sudo mysql_secure_installation
* set a password
* remove anonymous users
* disallow root login remotely
* remove the test database
* reload privileges

# Create new user
* sudo mysql -uroot -p
* CREATE DATABASE <dbname>;
* CREATE USER '<username>'@'localhost' IDENTIFIED BY '<password>';
* GRANT ALL PRIVILEGES ON <dbname>.* TO '<username>'@'localhost';
* FLUSH PRIVILEGES;

# Create a credentials file in the util folder
While in the util folder:
* nano credentials
* Format with username on the first line, password on the second line, and host name on the third line. Save and exit (ctrl-s and ctrl-x)

# Initialize the tables
Run util/sqlmanager.py from the util folder.
* python3 sqlmanager.py

You're all set.

# Setting up the cron job
* Open the cron table using the command: crontab -e
** If you haven't used the cron table before, you'll be prompted to choose an editor. I recommend nano.
* Type the following in */10 * * * * python3 "your path"
** "your path" should be replaced with the complete path to readlight.py (don't include quotation marks).
* Exit using ctrl-s.
