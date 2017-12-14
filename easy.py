# webserver server react threadpool easy http  单例模式             ok
# webserver tcpcon http     抽象工厂                                no
# react connect protocol    工厂方法                                ok
# server react tcpcon； webserver server pool  外观模式             ok,ok
# tcpcon        状态模式                                            ok
# tcpcon        模板模式                                            no
# http          策略模式                                            ok

# 主线程：      实际操作，其他线程可提交事件：reactor.loop  accept read write decode encode  再循环中fd有变化可以等到通知
# reactor线程： reactor add or del     实际执行，其他可以提交
# 100业务线程： 只处理原始数据，return 原始数据

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
