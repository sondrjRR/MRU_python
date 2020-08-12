from __future__ import print_function
import mysql.connector  # https://www.w3schools.com/python/python_mysql_insert.asp
# https://support.rackspace.com/how-to/install-mysql-server-on-the-ubuntu-operating-system/ # command line mySQL
# https://mediatemple.net/community/products/dv/204404494/how-do-i-grant-privileges-in-mysql # PRIVILEGES


# CREATE TABLE `imu_data`.`test_table` (
#   `idtestTable2` INT NOT NULL,
#   `accel_x` INT NULL,
#   `accel_y` INT NULL,
#   `time_entry` TIMESTAMP(3) NULL,
#   PRIMARY KEY (`idtestTable2`));

    #  Show users : SELECT User, Host, authentication_string FROM mysql.user;
    # Show databases: SHOW DATABASES;
    # Add user: INSERT INTO mysql.user (User,Host,authentication_string,ssl_cipher,x509_issuer,x509_subject) VALUES('rrai','%',PASSWORD('redrock1234'),'','','');
    # Show Password settings: SHOW VARIABLES LIKE 'validate_password%';
    # Set values: SET GLOBAL validate_password_length = 6;
    #             SET GLOBAL validate_password_number_count = 0;
    # Grant basic user: GRANT SELECT, INSERT, SHOW DATABASES ON imu_data.* TO rrai@%;
import sys
import getopt
# # sys.path.append('.')
import RTIMU
import os.path
import time
import math
from AHRS import madgwick
from AHRS import quaternions
import numpy as np
from datetime import date, datetime, timedelta
###########################################################################################################
# HOST = "127.0.0.1"
HOST = "192.168.1.100"
PORT = 3306
DATABASE = "test"
USER = "test_user"
PASSWORD = "redrock1234"
print("Hello, world!")
try:
    cnx = mysql.connector.connect(user=USER, password=PASSWORD, host=HOST, database=DATABASE, port=PORT)
except Exception as e:
    print(e)


timeRead = datetime.utcnow()
print("Time read is: ", timeRead)
cursor = cnx.cursor()


testAccel = 1
imu_data = "INSERT INTO `test`.`imu_data` (`index`, `accel_x`, `time_entry`) VALUES (%s, %s, %s)"
val = (testAccel, testAccel, timeRead)

cursor.execute(imu_data, val)

cnx.commit()

cursor.close()
cnx.close()


cnx.close()
###########################################################################################################
    # cnx = mysql.connector.connect(user=USER, password=PASSWORD,
    #                               host=HOST,
    #                               database=DATABASE)


# SETTINGS_FILE = "IMU_config"
#
# print("Using settings file " + SETTINGS_FILE + ".ini")
# if not os.path.exists(SETTINGS_FILE + ".ini"):
#     print("Settings file does not exist, will be created")
#
# s = RTIMU.Settings(SETTINGS_FILE)
# imu = RTIMU.RTIMU(s)
#
# print("IMU Name: " + imu.IMUName())
#
# if not imu.IMUInit():
#     print("IMU Init Failed")
#     sys.exit(1)
# else:
#     print("IMU Init Succeeded")
#
# # this is a good time to set any fusion parameters
#
# # imu.setSlerpPower(0.02)
# imu.setGyroEnable(True)
# imu.setAccelEnable(True)
# imu.setCompassEnable(True)
#
# poll_interval = imu.IMUGetPollInterval()
# print("Recommended Poll Interval: %dmS\n" % poll_interval)
#
# AHRS = madgwick.MadgwickAHRS()
# #
# # while True:
# #     if imu.IMURead():
# #
# #         # accelData = imu.getAccel()
# #         aX = round(imu.getAccel()[0], 4)  # accelData[0]
# #         aY = round(imu.getAccel()[1], 4)  # accelData[1]
# #         aZ = round(imu.getAccel()[2], 4)  # accelData[2]
# #         # print("aX: %f aY: %f aZ: %f" % (aX, aY, aZ))
# #
# #         # gyroData = imu.getGyro()
# #         gX = round(imu.getGyro()[0], 4)
# #         gY = round(imu.getGyro()[1], 4)
# #         gZ = round(imu.getGyro()[2], 4)
# #         # print("gX: %f gY: %f gZ: %f" % (gX, gY, gZ))
# #
# #         # magData = imu.getCompass()
# #         mX = round(imu.getCompass()[0], 4)
# #         mY = round(imu.getCompass()[1], 4)
# #         mZ = round(imu.getCompass()[2], 4)
# #         # print("mX: %f mY: %f mZ: %f" % (mX, mY, mZ))
# #
# #         # print("(aX: %f aY: %f aZ: %f) : (gX: %f gY: %f gZ: %f) : (mX: %f mY: %f mZ: %f) " % (aX, aY, aZ, gX, gY, gZ,
# #         #                                                                                          mX, mY, mZ))
# #
# #         a_array = np.array([aX, aY, aZ])
# #         g_array = np.array([gX, gY, gZ])
# #         m_array = np.array([mX, mY, mZ])
# #         AHRS.update(g_array, a_array, m_array)
# #         print(AHRS)
# #         time.sleep(poll_interval * 1.0 / 1000.0)
# #
#
#
# imu.IMURead()
#
# # accelData = imu.getAccel()
# aX = round(imu.getAccel()[0], 4)  # accelData[0]
# aY = round(imu.getAccel()[1], 4)  # accelData[1]
# aZ = round(imu.getAccel()[2], 4)  # accelData[2]
# # print("aX: %f aY: %f aZ: %f" % (aX, aY, aZ))
#
# # gyroData = imu.getGyro()
# gX = round(imu.getGyro()[0], 4)
# gY = round(imu.getGyro()[1], 4)
# gZ = round(imu.getGyro()[2], 4)
# # print("gX: %f gY: %f gZ: %f" % (gX, gY, gZ))
#
# # magData = imu.getCompass()
# mX = round(imu.getCompass()[0], 4)
# mY = round(imu.getCompass()[1], 4)
# mZ = round(imu.getCompass()[2], 4)
# # print("mX: %f mY: %f mZ: %f" % (mX, mY, mZ))
#
# # print("(aX: %f aY: %f aZ: %f) : (gX: %f gY: %f gZ: %f) : (mX: %f mY: %f mZ: %f) " % (aX, aY, aZ, gX, gY, gZ,
# #                                                                                          mX, mY, mZ))
#
# a_array = np.array([aX, aY, aZ])
# g_array = np.array([gX, gY, gZ])
# m_array = np.array([mX, mY, mZ])
# AHRS.update(g_array, a_array, m_array)
# print(AHRS)
# time.sleep(poll_interval * 1.0 / 1000.0)

###########################################################################################################
# timeRead = datetime.utcnow()
# print("Time read is: ", timeRead)
# cursor = cnx.cursor()
#
#
# testAccel = 1
# imu_data = "INSERT INTO `test`.`imu_data` (`index`, `accel_x`, `time_entry`) VALUES (%s, %s, %s)"
# val = (testAccel, testAccel, timeRead)
#
# cursor.execute(imu_data, val)
#
# cnx.commit()
#
# cursor.close()
# cnx.close()
###########################################################################################################
    # madgwick.MadgwickAHRS.update(imu.getAccel(), imu.getGyro(), imu.getCompass())


# sudo systemctl set-default multi-user.target
# sudo systemctl set-default graphical.target


