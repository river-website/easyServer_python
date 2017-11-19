from threading import *
from time import *
k = Lock()

def a():
    global k
    print(k)
    k.acquire()
    print(k)
    print('get k1')
    sleep(5)
    print('get k2')
    k.release()
    print(k)
def b():
    global k
    print(k)
    k.release()
    print(k)
    k.release()
    print(k)
    k.acquire()
    print(k)
    print('put k1')
print('start')
t=Thread(target=a)
t.setDaemon(True)
t.start()
sleep(1)
b()
sleep(10)