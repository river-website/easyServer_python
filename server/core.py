class Singleton(object):
    _instance = None
    _oldInit = None
    _init = True
    def __new__(cls,*args,**kwd):
        if Singleton != cls:
            if not cls._instance:
                cls._oldInit = cls.__init__
                cls.__init__ = cls.__Singleton_Init__
                cls._instance = object.__new__(cls)
            return cls._instance

    def __Singleton_Init__(self, *args):
        if self._init:
            self._oldInit(*args)
            self._init = False

