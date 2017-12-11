class component(object):
    _compositeList = []
    def __init__(self,name):
        self._name = name
    def name(self):
        print(self._name)
        self.type()
        self.suffix()
    def type(self):
        pass
    def suffix(self):
        pass
    def add(self,comp):
        pass
    def remove(self,comp):
        pass
class txtComponent(component):
    def type(self):
        print("file")
    def suffix(self):
        print(".txt")

class pdfComponent(component):
    def type(self):
        print("file")
    def suffix(self):
        print(".pdf")
class composite(component):
    def type(self):
        print("dir")
    def suffix(self):
        print("null")
    def add(self, comp):
        self._compositeList.append(comp)
    def remove(self, comp):
        self._compositeList.remove(comp)
    def name(self):
        print(self._name)
        self.type()
        self.suffix()
        for comp in self._compositeList:
            comp.name()
t1 = txtComponent("txt1")
com = composite("dir1")
com.add(pdfComponent("pdf1"))
com.add(txtComponent("txt2"))
t1.name()
com.name()