from protocol.ezHTTP import *
from system.ezServer import *

class ezWebServer(object):
    protocol = None
    server = None
    webData = dict()
    def __init__(self,serverData):
        self.webData = serverData
        self.server = ezServer(dict(serverData).keys())
        self.protocol = ezHTTP()
    def start(self):
        self.server.start()
    def onMessage(self):
        pass
