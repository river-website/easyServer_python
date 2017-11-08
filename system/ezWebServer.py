

class ezWebServer(object):
    protocol = None
    data = None
    server = None
    def __init__(self):
        pass
    def setData(self,data):
        self.data = data
    def start(self):
        map(self.startOne(),self.data)
    def startOne(self,data):
        data['host']
    def onMessage(self):
        pass
