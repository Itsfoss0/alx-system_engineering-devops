-- create a Database tyrell_corp and assign 'holberton_user'@'localhost' SELECT privs
CREATE DATABASE IF NOT EXISTS `tyrell_corp`;
USE `tyrell_corp`;
CREATE TABLE IF NOT EXISTS nexus6 (`int` INT, `name` VARCHAR(30));
INSERT INTO `nexus6` VALUES (1, 'John Doe');
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;