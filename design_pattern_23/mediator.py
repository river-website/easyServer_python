class mediator(object):
    def change(self,weight):
        pass
class concreteMediator(mediator):
    w1 = None
    w2 = None
    def change(self,weight):
        if isinstance(weight,weight1):
            self.w2.setName("name 2")
            weight.do1()

class colleague(object):
    def __init__(self,name,cm):
        self._name = name
        self.setMediator(cm)
    def setMediator(self,mediator):
        self._me = mediator
class weight1(colleague):
    def do1(self):
        print("do 1")
    def setName(self,name):
        self._name = name
        self._me.change(self)

class weight2(colleague):
    def do2(self):
        print("do 2")
    def setName(self,name):
        self._name = name

cm = concreteMediator()
w1= weight1("w1",cm)
w2 = weight2("w2",cm)
cm.w1 = w1
cm.w2 = w2
w1.setName("new w1")



