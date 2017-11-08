

class ezWebServer(object):
    protocol = None
    data = None
    server = None
    def __init__(self):
        pass
    def setData(self,data):
        self.data = data
    def start(self):
        map(self.startOne(),dict(self.data).keys(),dict(self.data).values())
    def startOne(self,host,value):
        pass
    def onMessage(self):
        pass
