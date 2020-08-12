# MRU_python
Motion referenceing with the use of a 9-DOF IMU. Accelerometer, Gyro and Magnetometer


In order to build the Python module download [RTIMULib2](https://github.com/RTIMULib/RTIMULib2) and follow the instructions from RTIMULib2/Linux/python/README.md

Then install sql-connector-python with a pip install
    
    sudo apt install python3-pip  #  if pip is not installed 
    pip3 install mysql-connector-python

## Connecting to a LAN remote database
1. Enable other devices to connect to the database <br/>
    - This is done by editing the bind-address from 127.0.0.1 to 0.0.0.0 within the mysqld.cnf file, default located at:
    
            /etc/mysql/mysql.conf.d/my
              
2. Create a user with From host: %


## SQL cheat sheet:

##### Create table
    CREATE TABLE `imu_data`.`test_table` ( 
    `idtestTable2` INT NOT NULL, 
    `accel_x` INT NULL, 
    `accel_y` INT NULL,
    `time_entry` TIMESTAMP(3) NULL,
    PRIMARY KEY (`idtestTable2`));

##### Show users

    SELECT User, Host, authentication_string FROM mysql.user;
    
#### Show databases: 
    SHOW DATABASES;
    
#### Add user: 
    INSERT INTO mysql.user (User,Host,authentication_string,ssl_cipher,x509_issuer,x509_subject) VALUES('rrai','%',PASSWORD('redrock1234'),'','','');

#### Select database and show tables
    USE name_of_database;
    SHOW TABLES;
    
#### Show Password settings:
    SHOW VARIABLES LIKE 'validate_password%';
    
#### Change global values:
    SET GLOBAL validate_password_length = 6;
    SET GLOBAL validate_password_number_count = 0;
    
    
#### Grant basic user
    GRANT SELECT, INSERT, SHOW DATABASES ON imu_data.* TO user_name@'%';

#### Grant Super User ROLE/PRIVILEGES
    GRANT GRANT OPTION ON *.* TO user_name@'%';
    GRANT ALL PRIVILEGES ON *.* TO user_name@'%';
    # If the following lines are necessary tests them one at a time as listed
    GRANT SUPER ON *.* TO rrai@'%'; (Not sure if this one is neccesray)
    UPDATE mysql.user SET Super_Priv='Y' WHERE user='rrai' AND host='%'; (Not sure if this one is neccessary)

Indent with markdown:

    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    
## Sources:
 [python mysql insert](https://www.w3schools.com/python/python_mysql_insert.asp) <br/>
 [mySQL terminal command lines](https://support.rackspace.com/how-to/install-mysql-server-on-the-ubuntu-operating-system/) <br/> 
 [SQL role PRIVILEGES](https://mediatemple.net/community/products/dv/204404494/how-do-i-grant-privileges-in-mysql) <br/>
 [python matlibplot Plot with timestamp](https://stackoverflow.com/questions/1574088/plotting-time-in-python-with-matplotlib/16428019) <br/>