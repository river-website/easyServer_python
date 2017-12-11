class observer(object):
    def update(self,subject):
        pass
class ob1(observer):
    def __init__(self,subject):
        self._sub = subject
    def update(self,subject):
        print("ob1 get state change")
        print(self._sub.get())
class ob2(observer):
    def __init__(self,subject):
        self._sub = subject
    def update(self,subject):
        print("ob2 get statechange")
        print(self._sub.get())

class subject(object):
    _list = []
    def attach(self,ob):
        self._list.append(ob)
    def detach(self,ob):
        self._list.remove(ob)
    def notify(self):
        for ob in self._list:
            ob.update(self)
class concreteSub(subject):
    __state = 0
    def set(self,s):
        self.__state = s
        self.notify()
    def get(self):
        return self.__state

sub = concreteSub()
ob1 = ob1(sub)
sub.attach(ob1)
ob2 = ob2(sub)
sub.attach(ob2)
sub.set(1)
