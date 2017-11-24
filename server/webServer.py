from protocol.http import *
from server.server import *
from pool.threadPool import *
from connect.tcpCon import *

# web服务
class webServer(object):
    # 协议如：http
    protocol = None
    # server实体
    server = None
    # 线程池
    tPools = None
    # web数据
    webData = None
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
        self.protocol = http()
        self.server.protocol = self.protocol
        self.tPools = threadPool(100)
    # web启动
    def start(self):
        self.server.onMessage = self.onMessage
        self.server.start()
    # 业务逻辑
    def buss(self,arg):
        return 'hello world!'
    # 线程函数
    def work(self,arg):
        con = arg[0]
        ret = self.buss(arg[1])
        con.send(ret)
    # tcp收到数据回调
    def onMessage(self,con,data):
        self.tPools.addEvent(self.work,(con,data))
