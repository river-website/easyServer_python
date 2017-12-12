class abstractClass(object):
    def first(self):
        pass
    def second(self):
        pass
    def last(self):
        pass
    def do(self):
        self.first()
        self.second()
        self.last()
class concreteClass(abstractClass):
    def first(self):
        print("第一步")
    def second(self):
        print("dierbu")
    def last(self):
        print("zuih")
c = concreteClass()
c.do()