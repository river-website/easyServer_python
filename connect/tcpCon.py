from react.react import *

# tcp连接类
class tcpCon(object):
    # 客户端socket
    clientSocket = None
    # 读数据缓存
    readBuffer = ''
    # 写数据缓存
    writeBuffer = ''
    # 数据读完，回调函数
    onMessage = None
    # 解密加密类
    protocol = None
    # 当前报文长度
    currentLen = 0
    # 服务类
    server = None
    def __init__(self,clientSocket):
        self.clientSocket = clientSocket
    # 数据到达
    def onRead(self,s,args=None):
        buffer = self.clientSocket.recv(8192)
        if buffer:
            buffer = bytes.decode(buffer)
            if self.protocol:
                if self.currentLen:
                    self.currentLen = self.protocol.getInfo(self,buffer)
                self.readBuffer += buffer
                if len(self.readBuffer) < self.currentLen:
                    return
                else:
                    dData = self.protocol.decode(self.readBuffer)
                    self.onMessage(self, dData)
            else:
                self.onMessage(self,buffer)
        else:
            self.close()
    # 写准备好
    def onWrite(self):
        pass
    # 发送数据
    def send(self,data):
        if self.protocol:
            data = self.protocol.encode(data)
        self.clientSocket.send(bytearray(data,'utf-8'))
        # self.close()
    # 关闭
    def close(self):
        self.server.react.delEvent(self.clientSocket, EVENT_READ)
        self.clientSocket.close()
