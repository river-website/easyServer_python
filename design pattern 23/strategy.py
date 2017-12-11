class context(object):
    def __init__(self,strategy):
        self.__strategy = strategy
    def interface(self,x,y):
       return self.__strategy.do(x,y)

class strategy(object):
    def do(self,x,y):
        pass
class min(strategy):
    def do(self,x,y):
        if x<y:
            return x
        else:return y
class max(strategy):
    def do(self,x,y):
        if x>y:
            return x
        else:return y
c=context(min())
print(c.interface(1,2))