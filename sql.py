from __future__ import print_function

from datetime import date, datetime, timedelta
import mysql.connector
import numpy as np

# cnx = mysql.connector.connect(user='test_user', password='redrock1234',
#                               host='127.0.0.1',
#                               database='test')
HOST = "192.168.1.100"
DATABASE = "test"
USER = "test_user"
PASSWORD = "redrock1234"

cnx = mysql.connector.connect(user=USER, password=PASSWORD,
                              host=HOST,
                              database=DATABASE)




cursor = cnx.cursor()

# imu_data = {
#     'accel_x': 1,
#     'accel_y': 2,
#     'accel_z': 3,
#     'time_entry': "2020-05-01 06:20:21.123"
# }

# imu_data = """INSERT INTO `test`.`imu_data` (`idimu_data`, `index`, `accel_x`, `time_entry`) VALUES ('2', '1', '1', '2020-03-05 20:20:20.200')"""
imu_data = """INSERT INTO `test`.`imu_data` (`index`, `accel_x`, `time_entry`) VALUES ('1', '1', '2020-03-05 20:20:20.200')"""

cursor.execute(imu_data)

cnx.commit()

cursor.close()
cnx.close()
