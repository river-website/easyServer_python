from server.core import *
class connection(object):
    _rBuffer = ''
    _wBuffer = ''
    _socket = None
    _state = None
    _curLen = 0
    _protocol = None
    onMessage = None

    def __init__(self,socket,protocol):
        self._socket = socket
        self._protocol = protocol
    def read(self):
        pass
    def write(self):
        pass
    def send(self,data):
        pass
    def close(self,data = None):
        pass
    def getSocket(self):
        return self._socket
    def getState(self):
        return self._state
    def setState(self,state):
        self._state = state

class tcpCon(connection):
    def read(self):
        buffer = self._state.read(self)
        if buffer:
            buffer = bytes.decode(buffer)
            if self._protocol:
                if self._curLen:
                    self._curLen = self._protocol.getInfo(self, buffer)
                self._rBuffer += buffer
                if len(self._rBuffer) < self._curLen:
                    return
                else:
                    dData = self._protocol.decode(self._rBuffer)
                    self.onMessage(self, dData)
            else:
                self.onMessage(self, buffer)
    def wirte(self):
        l = self._state.write(self,self._wBuffer)
        if l < len(self._wBuffer):
            self._wBuffer = self._wBuffer[l:]
    def send(self,data=None):
        if not data:
            self._wBuffer += data
        self.wirte()
    def close(self):
        if self._wBuffer:
            self.send()
class tcpState(Singleton):
    def read(self,connect):
        pass
    def write(self,connect,data):
        pass
    def close(self,socket):
        pass
class connecting(tcpState):
    def read(self,connect):
        socket = connect.getSocket()
        try:
            buffer = socket.recv(65536)
        except ConnectionError as e:
            print('read error:' + str(socket) + e.strerror)
            connect.close()
            return None
        if not buffer:
            print('read None:' + str(socket))
            connect.close()
            return None
        return buffer
    def write(self,connect,data):
        socket = connect.getSocket()
        return socket.send(data)

    def close(self,connect):
        socket = connect.getSocket()
        socket.close()
        connect.setState(closeing())
class closeing(tcpState):
    pass

