from __future__ import print_function
import mysql.connector
import sys
import getopt
# sys.path.append('.')
import RTIMU
import os.path
import time
import math
from AHRS import madgwick
from AHRS import quaternions
import numpy as np
from datetime import date, datetime, timedelta
import threading


def queryBufferList(sql_string, data):

    try:
        time_start = time.time()
        cursor.executemany(sql_string, data)
        cnx.commit()
        time_ms = (time.time() - time_start) * 1000
        print(" - Query completed \n - Time for query was: ", time_ms, "\n")

    except mysql.connector.errors.OperationalError as e:
        print("Error code:", e.errno)  # error number
        print("SQLSTATE value:", e.sqlstate)  # SQLSTATE value
        print("Error message:", e.msg)  # error message
        print ("Error:", e)  # errno, sqlstate, msg values
        s = str(e)
        print("Error:", s)  # errno, sqlstate, msg values

    # sqlThread.join()


#################################################################################################################
# SQL connection # ##############################################################################################
HOST = "127.0.0.1"
# HOST = "192.168.1.130"
PORT = 3306
DATABASE = "test"
USER = "test_user"
PASSWORD = "redrock1234"
print("Hello, world!")
cnx = mysql.connector.connect(user=USER, password=PASSWORD, host=HOST, database=DATABASE, port=PORT)
cursor = cnx.cursor()
#################################################################################################################
#################################################################################################################

#################################################################################################################
# IMU setup # ###################################################################################################
# SETTINGS_FILE = "IMU_config"
#
# print("Using settings file " + SETTINGS_FILE + ".ini")
# if not os.path.exists(SETTINGS_FILE + ".ini"):
#     print("Settings file does not exist, will be created")
# s = RTIMU.Settings(SETTINGS_FILE)
# imu = RTIMU.RTIMU(s)
# print("IMU Name: " + imu.IMUName())
# if not imu.IMUInit():
#     print("IMU Init Failed")
#     sys.exit(1)
# else:
#     print("IMU Init Succeeded")
# # this is a good time to set any fusion parameters
# # imu.setSlerpPower(0.02)
# imu.setGyroEnable(True)
# imu.setAccelEnable(True)
# imu.setCompassEnable(True)
# poll_interval = imu.IMUGetPollInterval()
# print("Recommended Poll Interval: %dmS\n" % poll_interval)
# AHRS = madgwick.MadgwickAHRS()
#################################################################################################################
#################################################################################################################

aX = 0.1
aY = 0.2
aZ = 0.3

gX = 0.4
gY = 0.5
gZ = 0.6

mX = 0.7
mY = 0.8
mZ = 0.9


imu_data = "INSERT INTO `test`.`imu_data` (`time_entry`, `accel_x`, `accel_y`, `accel_z`, `gyro_x`, `gyro_y`, `gyro_z`, `mag_x`, `mag_y`, `mag_z`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

listSize = 50
# listSize = 150
xList = [None]*listSize  # Pre-allocating memory
count = 0
i = 0
thCount = 0
sqlThread = threading.Thread()
sqlThreadBackup = threading.Thread()
BackUp = False

while count <= 100000:
    timeRead = datetime.utcnow()
    count = count + 1
    if i == listSize:
        i = 0
    xList[i] = (timeRead, aX, aY, aZ, gX, gY, gZ, mX, mY, mZ)
    if count % listSize == 0 and count != 0:
        print("Active threads are: ", threading.active_count())
        # if threading.active_count() >= 1 and sqlThread.is_alive():
        #     sqlThreadBackup = threading.Thread(target=queryBufferList, args=(imu_data, xList,), daemon=True)
        #     sqlThreadBackup.start()
        if sqlThread.is_alive():
            sqlThread.join()
        sqlThread = threading.Thread(target=queryBufferList, args=(imu_data, xList,), daemon=True)
        sqlThread.start()

    i = i + 1
    # time.sleep(0.004)
    # time.sleep(0.0005)


cursor.close()
cnx.close()
