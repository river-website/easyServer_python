class Singleton(object):
    _instance=None
    def __new__(cls,*args,**kwd):
        if Singleton != cls:
            if not cls._instance:
                cls._instance = object.__new__(cls)
                cls._instance.__Singleton_Init__()
            return cls._instance

    def __Singleton_Init__(self):
        print("__Singleton_Init__")

class BB(Singleton):
    def __init__(self,name):
        print("init")
        self.name =name

class CC(Singleton):
    pass


c = BB("b")
print(c.name)
k = BB("v")
print(c.name)


