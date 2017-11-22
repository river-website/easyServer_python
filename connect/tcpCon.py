from react.react import *

class tcpCon(object):
    socket = None
    readBuffer = ''
    writeBuffer = ''
    onMessage = None
    protocol = None
    len = 0
    server = None
    def __init__(self,socket):
        self.socket = socket
    def onRead(self,s,args=None):
        buffer = self.socket.recv(8192)
        if buffer:
            buffer = bytes.decode(buffer)
            if self.protocol:
                if self.len:
                    self.len = self.protocol.getInfo(self,buffer)
                self.readBuffer += buffer
                if len(self.readBuffer) < self.len:
                    return
                else:
                    dData = self.protocol.decode(self.readBuffer)
                    self.onMessage(self, dData)
            else:
                self.onMessage(self,buffer)
        else:
            self.close()
    def onWrite(self):
        pass
    def send(self,data):
        if self.protocol:
            data = self.protocol.encode(data)
        self.socket.send(bytearray(data,'utf-8'))
        self.close()
    def close(self):
        self.server.react.delEvent(self.socket, EVENT_READ)
        self.socket.close()
    def __del__(self):
        pass
