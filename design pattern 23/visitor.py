class element(object):
    def accept(self,v):
        pass
class man(element):
    def accept(self,v):
        v.visitMan(self)
    def doMan(self):
        print("man do something")
class woman(element):
    def accept(self,v):
        v.visitWoman(self)
    def doWoman(self):
        print("woman do something")
class visit(object):
    def visitMan(self,el):
        pass
    def visitWoman(self,el):
        pass
class A(visit):
    def visitMan(self,el):
        print("A visit")
        el.doMan()
    def visitWoman(self,el):
        print("A not visit")
class B(visit):
    def visitWoman(self,el):
        print("B visit")
        el.doWoman()
    def visitMan(self,el):
        print("B not")

class objectStruct(object):
    _list = []
    def add(self,obj):
        self._list.append(obj)
    def remove(self,obj):
        self._list.remove(obj)
    def showAll(self,visitor):
        for o in self._list:
            o.accept(visitor)
l = objectStruct()
l.add(man())
l.add(woman())
l.add(woman())
l.add(man())
l.showAll(A())