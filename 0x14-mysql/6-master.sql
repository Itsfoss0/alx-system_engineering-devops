-- lets change the slave to be synchronized with the server
CHANGE MASTER TO
MASTER_HOST='54.146.84.110',
MASTER_USER='replica_user',
MASTER_PASSWORD='hbtn89',
MASTER_LOG_FILE='mysql-bin.000001',
MASTER_LOG_POS=727;

START SLAVE;