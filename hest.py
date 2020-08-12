import threading
import time
# https://realpython.com/intro-to-python-threading/

def slowQuery(data):
    print(data)
    time.sleep(2)
    print("done", data)



count = 0
while(count < 100):
    if (count % 10 == 0):
        x = threading.Thread(target=slowQuery, args=(count,)).start()

    count = count +1
