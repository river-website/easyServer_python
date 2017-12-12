class CarAbstraction(object):
    _imp =  None
    def __init__(self,imp):
        self._imp = imp
    def run(self):
        pass

class car(CarAbstraction):
    def run(self):
        print("car")
        self._imp.run()
class bus(CarAbstraction):
    def run(self):
        print("bus")
        self._imp.run()

class roadAb(object):
    def run(self):
        pass
class high(roadAb):
    def run(self):
        print("high")
class nomal(roadAb):
    def run(self):
        print("nomal")


p = car(high())
p.run()