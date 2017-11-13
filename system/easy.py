import os
import time

from system.ezWebServer import *

class easy(object):
    servers = dict()

    def __init__(self,servers):
        self.servers = servers
    def start(self):
        def back():
            return
            if os.fork() > 0:
                exit()
        def startOneServer(data):
            serverName = data[0]
            serverData = data[1]
            server = globals()[serverName](serverData)
            server.start()

        back()

        list(map(startOneServer, self.servers.items()))
        self.monitor()
    def monitor(self):
        while(True):
            print('main')
            time.sleep(10)
        pass
    def getPids(self):
        print('cc')
        pass
    def setPids(self):
        pass
    def getPid(self,pid):
        pass
    def getChild(self):
        pass
