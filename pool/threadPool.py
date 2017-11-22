from threading import *

class que(object):
    queue = []
    mutex = None
    empty = None
    def __init__(self,mutex=False):
        if mutex:
            self.mutex = Lock()
            self.empty = Lock()
            self.setEmpty()
    def acquire(self):
        if self.mutex != None:
            if self.mutex.acquire():
                return
    def notEmpty(self):
        if self.empty != None:
            self.empty.acquire()
    def setEmpty(self):
        if self.empty != None:
            self.empty.acquire()
    def setNotEmpty(self):
        if self.empty != None:
            self.empty.release()

    def release(self):
        if self.mutex != None:
            self.mutex.release()
    def pop(self):
        self.notEmpty()
        self.acquire()
        ret = self.queue.pop()
        if self.queue.__len__():
            self.setNotEmpty()
        self.release()
        return ret
    def push(self,item):
        self.acquire()
        if not self.queue.__len__():
            self.setNotEmpty()
        self.queue.append(item)
        self.release()
class threadPool(object):
    # 线程池
    pools = []
    task = 1
    maxSize = 0
    free = 0
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.task = que(True)
    def createThread(self):
        t = Thread(target=self.pool)
        t.setDaemon(True)
        t.start()
        self.pools.append(t)
    def run(self,func,args=None):
        self.task.push((func,args))
        if self.pools.__len__()<self.maxSize:
            self.createThread()

    def pool(self):
        while True:
            task = self.task.pop()
            if task:
                func = task[0]
                args = task[1]
                func(args)

