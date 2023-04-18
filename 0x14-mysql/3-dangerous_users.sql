-- unless we like to live dangerously, in which case we will ->
CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'hbtn89';
GRANT REPLICATION CLIENT, REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
