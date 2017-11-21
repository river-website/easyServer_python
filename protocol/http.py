from time import *

class http(object):
    methods = ('GET','')
    def __del__(self):
        pass
    def decode(self):
        pass
    def enocde(self):
        pass

    def listToArgs(self,ary, num):
        lens = len(ary)
        f = lens - num
        if f > 0:
            for i in range(f):
                ary.pop(num + i)
        if f < 0:
            for i in range(-f):
                ary.append('')
        return ary
    def getInfo(self,data):
        def decode():
            pass
        ret = httpData()
        (header,body) = self.listToArgs(data.split('\r\n\r\n',1),2)
        dd = header.split('\r\n')
        (ret.REQUEST_METHOD,ret.REQUEST_URI,ret.SERVER_PROTOCOL)=self.listToArgs(dd[0].split(' ',2),3)
        del(dd[0])
        list(map(decode,list(filter(lambda conent: conent!='',dd))))
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
    REMOTE_PORT = '0'
    REQUEST_TIME = time()
