# Required libraries
* mariadb
* pymysql
* datetime

# Initializing the database
Start by updating your pi:
* sudo apt update
* sudo apt upgrade

Install the server software
* sudo apt install mariadb-server

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

or for a remote user:
* GRANT ALL PRIVILEGES on <dbname>.* TO '<username>'@'%';
* FLUSH PRIVILEGES;

# Add your credentials to a .env file in your root directory
While in the util folder:
* nano .env
* HOST_NAME=yourhostname
* USER_NAME=yourusername
* PASSWORD=yourpassword
* Replace the right side of each of the above 3 lines with whatever your values are.

# Initialize the tables
Run util/setup.py from the util folder.

You're all set.
