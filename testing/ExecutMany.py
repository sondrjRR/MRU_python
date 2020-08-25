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

HOST = "127.0.0.1"
DATABASE = "test"
USER = "test_user"
PASSWORD = "redrock1234"
print("Hello, world!")

cnx = mysql.connector.connect(user=USER, password=PASSWORD, host=HOST, database=DATABASE, port=PORT)

timeRead = datetime.utcnow()
print("Time read is: ", timeRead)
cursor = cnx.cursor()

SETTINGS_FILE = "IMU_config"

print("Using settings file " + SETTINGS_FILE + ".ini")
if not os.path.exists(SETTINGS_FILE + ".ini"):
    print("Settings file does not exist, will be created")

s = RTIMU.Settings(SETTINGS_FILE)
imu = RTIMU.RTIMU(s)

print("IMU Name: " + imu.IMUName())

if not imu.IMUInit():
    print("IMU Init Failed")
    sys.exit(1)
else:
    print("IMU Init Succeeded")

# this is a good time to set any fusion parameters
# imu.setSlerpPower(0.02)
imu.setGyroEnable(True)
imu.setAccelEnable(True)
imu.setCompassEnable(True)

poll_interval = imu.IMUGetPollInterval()
print("Recommended Poll Interval: %dmS\n" % poll_interval)

AHRS = madgwick.MadgwickAHRS()
x = []
t = [None]*10
for step in range(10):
    timeRead = datetime.utcnow()
    t[step] = timeRead
    imu.IMURead()

    # accelData = imu.getAccel()
    aX = round(imu.getAccel()[0], 4)  # accelData[0]
    aY = round(imu.getAccel()[1], 4)  # accelData[1]
    aZ = round(imu.getAccel()[2], 4)  # accelData[2]
    x.append(aX)
    # print("aX: %f aY: %f aZ: %f" % (aX, aY, aZ))

    # gyroData = imu.getGyro()
    gX = round(imu.getGyro()[0], 4)
    gY = round(imu.getGyro()[1], 4)
    gZ = round(imu.getGyro()[2], 4)
    # print("gX: %f gY: %f gZ: %f" % (gX, gY, gZ))

    # magData = imu.getCompass()
    mX = round(imu.getCompass()[0], 4)
    mY = round(imu.getCompass()[1], 4)
    mZ = round(imu.getCompass()[2], 4)
    # print("mX: %f mY: %f mZ: %f" % (mX, mY, mZ))

    # print("(aX: %f aY: %f aZ: %f) : (gX: %f gY: %f gZ: %f) : (mX: %f mY: %f mZ: %f) - at TIME: %s " % (aX, aY, aZ, gX, gY, gZ,
    #                                                                                                    mX, mY, mZ, timeRead))


    time.sleep((poll_interval) * 1.0 / 1000.0)
    # time.sleep(100/1000)
    # a_array = np.array([aX, aY, aZ])
    # g_array = np.array([gX, gY, gZ])
    # m_array = np.array([mX, mY, mZ])
    # AHRS.update(g_array, a_array, m_array)
    # print(AHRS)
for i in t:
    imu_data = "INSERT INTO `data_db`.`imu_data` (`time_entry`, `accel_x`, `accel_y`, `accel_z`, `gyro_x`, `gyro_y`, `gyro_z`, `mag_x`, `mag_y`, `mag_z`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    mellom = i
    val = (i, aX, aY, aZ, gX, gY, gZ, mX, mY, mZ)
    start_time = time.time()
    # print(i)
    cursor.execute(imu_data, val)
    cnx.commit()
    # ms_time = round((time.time() - start_time) * 1000, 4)
    # print("--- %s[ms] mySQL exectuion time---" % ms_time)

    # time.sleep(poll_interval * 1.0 / 1000.0)
    # madgwick.MadgwickAHRS.update(imu.getAccel(), imu.getGyro(), imu.getCompass())

cursor.close()
cnx.close()
count = 0
start_time = time.time()
while (count < 100):
    imu.IMURead()
    count = count + 1

ms_time = round((time.time() - start_time) * 10, 4)
print("--- %s[ms]  time avg---" % ms_time)

# sudo systemctl set-default multi-user.target
# sudo systemctl set-default graphical.target


# while True:
#     if imu.IMURead():
#
#         # accelData = imu.getAccel()
#         aX = round(imu.getAccel()[0], 4)  # accelData[0]
#         aY = round(imu.getAccel()[1], 4)  # accelData[1]
#         aZ = round(imu.getAccel()[2], 4)  # accelData[2]
#         # print("aX: %f aY: %f aZ: %f" % (aX, aY, aZ))
#
#         # gyroData = imu.getGyro()
#         gX = round(imu.getGyro()[0], 4)
#         gY = round(imu.getGyro()[1], 4)
#         gZ = round(imu.getGyro()[2], 4)
#         # print("gX: %f gY: %f gZ: %f" % (gX, gY, gZ))
#
#         # magData = imu.getCompass()
#         mX = round(imu.getCompass()[0], 4)
#         mY = round(imu.getCompass()[1], 4)
#         mZ = round(imu.getCompass()[2], 4)
#         # print("mX: %f mY: %f mZ: %f" % (mX, mY, mZ))
#
#         # print("(aX: %f aY: %f aZ: %f) : (gX: %f gY: %f gZ: %f) : (mX: %f mY: %f mZ: %f) " % (aX, aY, aZ, gX, gY, gZ,
#         #                                                                                          mX, mY, mZ))
#
#         a_array = np.array([aX, aY, aZ])
#         g_array = np.array([gX, gY, gZ])
#         m_array = np.array([mX, mY, mZ])
#         AHRS.update(g_array, a_array, m_array)
#         print(AHRS)
#         time.sleep(poll_interval * 1.0 / 1000.0)
#
