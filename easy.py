# webserver tcpcon http  抽象工厂
# react                 工厂方法
# webserver server react threadpool easy http  单例模式
# server react tcpcon； webserver server pool  外观模式
# tcpcon        状态模式
# tcpcon        模板模式
# http          策略模式



#   python
#   多进程 单i/o线程  多业务线程
#   支持同一协议多端口
#   暂时同时仅支持单一服务如：web服务或websocket服务等等

#   测试用例
#   1.并发高1800，每个请求io小
#   2.并发高1800，每个请求io大
#   3.并发一般100，每个请求io小
#   4.并发一般100，每个请求io大

#   1.并发高1800，每个请求cpu小
#   2.并发高1800，每个请求cpu大
#   3.并发一般100，每个请求cpu小
#   4.并发一般100，每个请求cpu大

from server.webServer import *
from time import *

# 入口类
class easy(object):
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
