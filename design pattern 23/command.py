class command(object):
    def excute(self):
        pass
    def __init__(self,recv):
        self._recv = recv

class zhujiaofang(command):
    def excute(self):
        self._recv.cook("猪脚饭")
class yabo(command):
    def excute(self):
        self._recv.cook("鸭脖")
class recv(object):
    def cook(self,req):
        print("cook req"+ req)
class invoker(object):
    _clist = []
    def add(self,comd):
        self._clist.append(comd)
    def excute(self):
        for i in self._clist:
            i.excute()
inv = invoker()
inv.add(yabo(recv()))
inv.excute()
