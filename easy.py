# webserver server react threadpool easy http  单例模式
# webserver tcpcon http  抽象工厂
# react                 工厂方法
# server react tcpcon； webserver server pool  外观模式
# tcpcon        状态模式
# tcpcon        模板模式
# http          策略模式

from server.core import *
from server.webServer import *
from time import *

# 入口类
class easy(Singleton):
    # 开始
    def start(self,servers):
        # 后台
        def backGround():
            return
        # 开始一种服务：如webserver，websocketserver
        def startOneServer(serv):
            globals()[serv[0]](serv[1]).start()

        backGround()
        list(map(startOneServer,servers.items()))
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
