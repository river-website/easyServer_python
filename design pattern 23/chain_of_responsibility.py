class handle(object):
    def oprator(self,request):
        pass
    def setNext(self,hand):
        self._h = hand
class h1(handle):
    def oprator(self,request):
        if request == 'h1':
            print("h1 do")
            return True
        elif self._h:
            return self._h.oprator(request)
class h2(handle):
    def oprator(self,request):
        if request == 'h2':
            print("h2 do")
            return True
        elif self._h:
            return self._h.oprator(request)

a = h1()
b = h2()
a.setNext(b)
a.oprator('h1')
a.oprator('h2')