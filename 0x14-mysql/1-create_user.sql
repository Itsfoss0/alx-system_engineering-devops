-- lets create a user on the database servers
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT, REPLICATION SLAVE ON *.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
