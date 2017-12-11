class globalMap(object):
    __instance = None
    map = {}
    conf = {
        'threadCount': 0,
        'eventLock': False,
        'maxEventLock': False,
        'maxEvent': 500
    }
    def __new__(cls, *args, **kwd):
        if globalMap.__instance is None:
            globalMap.__instance = object.__new__(cls, *args, **kwd)
        return globalMap.__instance
    def get(self,key):
        try:
            return self.map[key]
        except KeyError:
            return None
    def set(self,key,value):
        self.map[key] = value
    def getConf(self):
        return self.conf