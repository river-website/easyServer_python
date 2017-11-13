

class ezTCP(object):
    socket = None
    readBuffer = None
    writeBuffer = None
    onMessage = None

    def __init__(self,socket):
        self.socket = socket
    def onRead(self):
        pass
    def onWrite(self):
        pass
    def send(self):
        pass
    def close(self):
        pass
    def __del__(self):
        pass
