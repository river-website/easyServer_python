class subject(object):
    def func1(self):
        pass
    def func2(self):
        pass
class realSubject(subject):
    def func1(self):
        print("real 1")
    def func2(self):
        print("real 2")
class proxy(subject):
    __real = None
    def __init__(self,real):
        self.__real = real
    def func1(self):
        if False:
            self.__real.func1()
    def func2(self):
        self.__real.func2()
vpn = proxy(realSubject())
vpn.func1()
vpn.func2()