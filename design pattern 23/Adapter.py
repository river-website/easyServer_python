class target(object):
    def pay(self):
        pass
class nomal1Target(target):
    def pay(self):
        print("normal 1")
class nomal2Target(target):
    def pay(self):
        print("normal 2")
class adaptee(object):
    def pay_other(self):
        print("other pay")

class adapter(target):
    def __init__(self):
        self.__adpetee = adaptee()
    def pay(self):
        self.__adpetee.pay_other()
nomal1Target().pay()
nomal2Target().pay()
adapter().pay()