import time
count = 0
i = 0
x = [None]*5
while count < 50:
    count = count + 1
    if i == 5:
        i = 0
        print(x)
    x[i] = count
    print("The value of i: ", i)
    i = i + 1
    time.sleep(1)
