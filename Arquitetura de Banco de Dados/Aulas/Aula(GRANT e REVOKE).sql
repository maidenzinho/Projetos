CREATE DATABASE Teste;

USE Teste;

CREATE USER 'estudantes'@'localhost';

ALTER USER 'estudates'@'localhost';
		WITH MAX_QUERIES_PER_HOUR 100
	MAX_UPDATES_PER_HOUR 100
    MAX_CONNECTIONS_PER_HOUR 4
    MAX_USER_CONNECTIONS 2;
    
SHOW PROCESSLIST;

KILL id;

CREATE ROLE IF NOT EXISTS 'administrator', 'client', 'employee', 'manager', 'waiter';

DROP ROLE IF EXISTS 'estudantes';

GRANT ALL PRIVILEGES ON *.* TO 'administrator' WITH GRANT OPTION;

GRANT SELECT ON database_name.* TO 'client';

GRANT SELECT, INSERT ON database_name.* TO 'employee';

GRANT SELECT, UPDATE ON database_name.* TO 'manager';

GRANT SELECT, INSERT, UPDATE ON databese_name.orders TO 'waiter';

GRANT 'administrator' TO 'user_name'@'host';

GRANT 'client' TO 'user_name'@'host';

REVOKE SELECT, INSERT, UPDATE ON database_name.orders FROM 'estudantes';

REVOKE 'administrator' FROM 'user_name'@'host';

CREATE USER ''@'localhost';

GRANT UPDATE, INSERT ON database_name.* TO ''@'localhost';

SET DEFAULT ROLE "admin" TO "jose"@"%";

SET ROLE ALL;

FLUSH PRIVILEGES;

DELETE FROM mysql.user WHERE user="clientes" AND host="localhost";

