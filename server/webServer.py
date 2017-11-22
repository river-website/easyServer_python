from protocol.http import *
from server.server import *
from pool.threadPool import *
from connect.tcpCon import *

class webServer(object):
    protocol = None
    server = None
    tpool = None
    webData = None
    def __init__(self,serverData):
        self.server = server(self.initData(serverData))
        self.server.onStart = self.onStart
    def initData(self,serverData):
        # return hosts
        self.webData = serverData
        return list(dict(serverData).keys())
    def onStart(self):
        self.protocol = http()
        self.server.protocol = self.protocol
        self.tpool = threadPool(100)
    def start(self):
        self.server.onMessage = self.onMessage
        self.server.start()
    def buss(self,arg):
        return 'hello world!'
    def work(self,arg):
        con = arg[0]
        ret = self.buss(arg[1])
        con.send(ret)
    def onMessage(self,con,data):
        self.tpool.run(self.work,(con,data))
