import threading
import time
import mysql.connector
# https://realpython.com/intro-to-python-threading/
# https://stackoverflow.com/questions/311775/python-create-a-list-with-initial-capacity - pre-allocation is going to affect due to using multiple threads
def queryBufferList(sql_string, data):
    # time_start = time.time()
    cursor.executemany(sql_string, data)
    cnx.commit()
    # time_ms = (time.time()-time_start) * 1000
    # print(" - Query completed \n - Time for query was: ", time_ms, "\n")


HOST = "127.0.0.1"
PORT = 3306
DATABASE = "test"
USER = "test_user"
PASSWORD = "redrock1234"
print("Hello, world!")
cnx = mysql.connector.connect(user=USER, password=PASSWORD, host=HOST, database=DATABASE, port=PORT)
cursor = cnx.cursor()


imu_data = """INSERT INTO test.t_test (a_val, b_str) VALUES (%s, %s)"""
xList = [None]*100  # Pre-allocating memory
y = "Hest"
count = 0
i = 0
while count <= 10000:

    count = count + 1
    if i == 100:
        i = 0
    xList[i] = (count, y)
    if count % 100 == 0 and count != 0:
        sqlThread = threading.Thread(target=queryBufferList, args=(imu_data, xList,)).start()
    i = i + 1
    time.sleep(0.002)

cursor.close()
cnx.close()
