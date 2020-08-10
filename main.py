import sys
import getopt
from AHRS import madgwick
from AHRS import quaternions
# sys.path.append('.')


import RTIMU
import os.path
import time
import math

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

while True:
    if imu.IMURead():

        # accelData = imu.getAccel()
        aX = round(imu.getAccel()[0], 4)  # accelData[0]
        aY = round(imu.getAccel()[1], 4)  # accelData[1]
        aZ = round(imu.getAccel()[2], 4)  # accelData[2]
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

        print("(aX: %f aY: %f aZ: %f) : (gX: %f gY: %f gZ: %f) : (mX: %f mY: %f mZ: %f) " % (aX, aY, aZ, gX, gY, gZ,
                                                                                             mX, mY, mZ))

        time.sleep(poll_interval * 1.0 / 1000.0)

    madgwick.MadgwickAHRS.update(imu.getAccel(), imu.getGyro(), imu.getCompass())

#
# sudo systemctl set-default multi-user.target
# sudo systemctl set-default graphical.target