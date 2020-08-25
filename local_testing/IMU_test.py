# from __future__ import print_function
import mysql.connector
import sys
import getopt
# sys.path.append('.')
import RTIMU
import os.path
import time
import math
# from AHRS import madgwick
# from AHRS import quaternions
import numpy as np
from datetime import date, datetime, timedelta
import threading




#################################################################################################################
#################################################################################################################

#################################################################################################################
# IMU setup # ###################################################################################################
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
# AHRS = madgwick.MadgwickAHRS()
#################################################################################################################
#################################################################################################################
start = time.time()
while True:


    imu.IMURead()

    #
    end = time.time()
    # print(end-start)
    if (end-start) > 1:
        start = time.time()
        print(imu.getAccel())

    # duration = end - start
    # if duration < poll_interval:
    #     time.sleep(poll_interval - duration)
