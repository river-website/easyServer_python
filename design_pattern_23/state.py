class state(object):
    def connect(self,connect):
        pass
    def close(self,connect):
        pass
    def read(self,connect):
        pass

    def wirte(self, connect, str):
        pass
class connecting(state):
    def connect(self,connect):
        print("已经连接")
    def close(self,connect):
        connect.close()
    def read(self,connect):
        return connect.read()
    def wirte(self,connect,str):
        connect.wirte(str)
class closed(state):
    def connect(self,connect):
        connect.connect()
    def close(self,connect):
        print("已经关闭")
    def read(self,connect):
        print("已经关闭")
    def wirte(self, connect, str):
        print("已经关闭")
class tcp(object):
    buffer = ''
    def connect(self):
        print("tcp connecting")
    def close(self):
        print("tcp closed")
    def read(self):
        print(self.buffer)
    def wirte(self, str):
        self.buffer = str
class tcpCon(object):
    tcp = None
    state = None
    def __init__(self):
        self.tcp = tcp()
        self.state = closed()
    def connect(self):
        self.state.connect(self.tcp)
        self.state = connecting()

    def close(self):
        self.state.close(self.tcp)
        self.state = closed()


    def read(self,):
        return self.state.read(self.tcp)


    def wirte(self, str):
        self.state.wirte(self.tcp,str)

t = tcpCon()
t.connect()
t.wirte("111")
t.read()
t.close()
t.read()
