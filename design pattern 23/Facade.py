class cpuSubsystem(object):
    def work(self):
        print("cpu sys work")
class diskSubsystem(object):
    def read(self):
        print("read disk")
class facade(object):
    __cpu = None
    __disk = None
    def __init__(self):
        self.__cpu = cpuSubsystem()
        self.__disk = diskSubsystem()
    def read(self):
        self.__disk.read()
    def work(self):
        self.__cpu.work()
f = facade()
f.work()
f.read()