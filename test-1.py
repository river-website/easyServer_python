from threading import *
from time import *
import datetime

sum = 500000000
threadCount = 1
time= 0

def test():
    print(datetime.datetime.now()-time)
    c = int(sum/threadCount)
    for i in range(c):
        f = i*9+4-4
    print(datetime.datetime.now()-time)
    print(f)

time = datetime.datetime.now()
print('start')
if threadCount>1:
    for i in range(threadCount):
        a = Thread(target=test)
        a.start()
else:
    test()