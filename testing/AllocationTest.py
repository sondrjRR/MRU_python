import time

def doAppend( size=10000 ):
    result = []
    for i in range(size):
        message= "some unique object %d" % ( i, )
        result.append(message)
    return result

def doAllocate( size=10000 ):
    result=size*[None]
    for i in range(size):
        message= "some unique object %d" % ( i, )
        result[i]= message
    return result


start_time = time.time()
doAppend()
append_time = (time.time() - start_time)*1000
print("Append time was:", append_time)



start_time = time.time()
doAllocate()
append_time = (time.time() - start_time)*1000
print("Allocate time was:", append_time)
