class component(object):
    def do(self):
        pass
class nomarlComponent(component):
    def do(self):
        print("nomarlComponent")
class decoretor(component):
    _comp = None
    def __init__(self,comp):
        self._comp = comp
class hook1(decoretor):
    def do(self):
        print("hook1")
        self._comp.do()
class hook2(decoretor):
    def do(self):
        print("hook2")
        self._comp.do()
nomarlComponent().do()
hook1(nomarlComponent()).do()
hook2(hook1(nomarlComponent())).do()