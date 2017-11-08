import os
import ezWebServer

class easy(object):
    server = []

    def __init__(self):
        pass
    def addServer(self,server,serverData):
        self.server.append({'server':server,'data':serverData})
    def start(self):
        self.back()
        map(self.startOneServer(),self.server)
        self.monitor()
    def startOneServer(self,server):
        serv = server['server']()
        serv.setData(server['data'])
        serv.start()
    def back(self):
        if os.fork() > 0:
            exit()
    def monitor(self):
        pass
    def getPids(self):
        pass
    def setPids(self):
        pass
    def getPid(self,pid):
        pass
    def getChild(self):
        pass
