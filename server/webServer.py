from protocol.http import *
from server.server import *
from pool.threadPool import *
from connect.tcpCon import *
from globals.globalMap import *
from server.core import *

class serverAF(Singleton):
    def createProtocol(self):
        pass
    def createConect(self):
        pass
class webServer(serverAF):
    def createConect(self):
        return "tcp"
    def createProtocol(self):
        return http()


# web服务
class webServer1(Singleton):
    # 协议如：http
    protocol = None
    # server实体
    server = None
    # 线程池
    tPools = None
    # web数据
    webData = None
    # 线程数
    threadCount=0
    # 设置web数据，创建server
    def __init__(self,serverData):
        self.server = server(self.initData(serverData))
        self.server.onStart = self.onStart
    # 初始化数据
    def initData(self,serverData):
        # return hosts
        self.webData = serverData
        return list(serverData.keys())
    # 进程启动时运行
    def onStart(self):
        conf = globalMap().getConf()
        self.threadCount = conf['threadCount']
        self.protocol = http()
        self.server.protocol = self.protocol
        if self.threadCount:
            self.tPools = threadPool(self.threadCount)
    # web启动
    def start(self):
        self.server.onMessage = self.onMessage
        self.server.start()
    # 业务逻辑
    def buss(self,arg):
        # # i/o 小
        # time.sleep(0.01)
        # # i/o 大
        # time.sleep(1)
        # # cpu 小
        # for i in range(1000):
        #     a = (i * 4 - 9) / 3
        # # cpu 大
        # for i in range(100000):
        #     a = (i * 4 - 9) / 3
        return "Hello, world"
    # 线程函数
    def work(self,arg):
        con = arg[0]
        ret = self.buss(arg[1])
        if arg[1].HTTP_CONNECTION.lower() == 'Keep-Alive'.lower():
            con.send(ret)
        else:
            con.close(ret)
    # tcp收到数据回调
    def onMessage(self,con,data):
        if self.threadCount:
            self.tPools.addEvent(self.work,(con,data))
        else:
            self.work((con,data))