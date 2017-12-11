
class globals(object):
    __instance = None
    map = {}
    conf = {
        'threadConut': 0,
        'eventLock': False,
        'maxEventLock': False,
        'maxEvent': 500
    }
    def __new__(cls, *args, **kwd):
        if globals.__instance is None:
            globals.__instance = object.__new__(cls, *args, **kwd)
        return globals.__instance
    def get(self,key):
        try:
            return self.map[key]
        except KeyError:
            return None
    def set(self,key,value):
        self.map[key] = value
    def getConf(self,key):
        try:
            return self.conf[key]
        except KeyError:
            return None