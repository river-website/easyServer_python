#   python
#   多进程 单i/o线程  多业务线程
#   支持同一协议多端口
#   暂时同时仅支持单一服务如：web服务或websocket服务等等
from server.webServer import *
from time import *

# 入口类
class easy(object):
    # 开始
    def start(self,server,serverData):
        # 后台
        def backGround():
            return
        # 开始一种服务：如webserver，websocketserver
        def startOneServer(serverName,data):
            server = globals()[serverName](data)
            server.start()

        backGround()
        startOneServer(server,serverData)
        self.monitor()
    # 监视所有的server
    def monitor(self):
        sleep(1000)
    def getPids(self):
        pass
    def setPids(self):
        pass
    def getPid(self,pid):
        pass
    def getChild(self):
        pass
