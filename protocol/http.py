from time import *
import re

class http(object):
    methods = ('GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS')
    def __del__(self):
        pass
    def decode(self,data):
        def decode(connect):
            (key, value) = self.listToArgs(connect.split(':', 1), 2)

        ret = httpData()
        (header,body) = self.listToArgs(data.split('\r\n\r\n',1),2)
        dd = header.split('\r\n')
        (ret.REQUEST_METHOD,ret.REQUEST_URI,ret.SERVER_PROTOCOL)=self.listToArgs(dd[0].split(' ',2),3)
        del(dd[0])
        list(map(decode,list(filter(lambda conent: conent!='',dd))))
        return ret
    def encode(self,content):
        header = 'HTTP/1.1 200 OK\r\n'
        header += 'Server: easy server\r\nContent-Length: '+ str(len(content)) +'\r\n\r\n'
        return  header+content

    def listToArgs(self,ary, num):
        lens = len(ary)
        f = lens - num
        if f > 0:
            for i in range(f):
                ary.pop(num + i)
        if f < 0:
            for i in range(-f):
                ary.append('')
        return ary if num > 1 else ary[0]
    def getInfo(self,con,data):
        (header) = self.listToArgs(data.split('\r\n\r\n',1),1)
        (METHOD) = self.listToArgs(header.split(' ', 1), 1)
        if METHOD in self.methods:
            return self.getSize(header,METHOD)
        else:
            con.send('HTTP/1.1 400 Bad Request\r\n\r\n')
            return 0
    def getSize(self,header,method):
        if method == 'GET' or method == 'HEAD' or method == 'OPTIONS':
            return len(header)+4
        p1 = r"(\r\nContent-Length: ?(\d+))"  # 这是我们写的正则表达式规则，你现在可以不理解啥意思
        pattern1 = re.compile(p1)  # 我们在编译这段正则表达式
        matcher1 = re.search(pattern1, header)  # 在源文本中搜索符合正则表达式的部分
        content_length = matcher1.group(0)  # 打印出来
        return content_length + len(header) + 4
class httpData(object):
    QUERY_STRING = ''
    REQUEST_METHOD = ''
    REQUEST_URI = ''
    SERVER_PROTOCOL = ''
    SERVER_SOFTWARE = 'easy server'
    SERVER_NAME = ''
    HTTP_HOST = ''
    HTTP_USER_AGENT = ''
    HTTP_ACCEPT = ''
    HTTP_ACCEPT_LANGUAGE = ''
    HTTP_ACCEPT_ENCODING = ''
    HTTP_COOKIE = ''
    HTTP_CONNECTION = ''
    REMOTE_ADDR = ''
    REMOTE_PORT = ''
    REQUEST_TIME = time()
