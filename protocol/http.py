from time import *
import re
from urllib.parse import *
from server.core import *

import cgi
# http解析类
class http(Singleton):
    # 可接受的方式
    methods = ('GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS')
    # 解码函数
    def decode(self,data):
        def decode(content):
            (key, value) = self.listToArgs(content.split(':', 1), 2)
            key='HTTP_'+key.replace('-','_').upper()
            value = value.strip()
            setattr(ret, key, value)
            if key == 'HTTP_HOST':
                tmp = value.split(':')
                ret.SERVER_NAME = tmp[0]
                if tmp[1]:
                    ret.SERVER_PORT = tmp[1]
            elif key == 'HTTP_COOKIE':
                ret.COOKIE =  parse_qs(value.replace(':','&'))
            elif key == 'HTTP_CONTENT_TYPE':
                p1 = r"(boundary='?(\S+)'?)"  # 这是我们写的正则表达式规则，你现在可以不理解啥意思
                pattern1 = re.compile(p1)  # 我们在编译这段正则表达式
                match = re.search(pattern1, value)  # 在源文本中搜索符合正则表达式的部分
                if not match:
                    pos = value.strpos(';')
                    if pos:
                        ret.CONTENT_TYPE = value.substr(0,pos)
                    else:
                        ret.CONTENT_TYPE = value
                else:
                    ret.CONTENT_TYPE = 'multipart/form-data'
                    http_post_boundary = '--'+match.group(0)
            elif key == 'HTTP_CONTENT_LENGTH':
                ret.CONTENT_LENGTH = value
        # 返回的类
        ret = httpData()
        http_post_boundary = ''
        (http_header,http_body) = self.listToArgs(data.split('\r\n\r\n',1),2)
        header_data = http_header.split('\r\n')
        (ret.REQUEST_METHOD,ret.REQUEST_URI,ret.SERVER_PROTOCOL)=self.listToArgs(header_data[0].split(' ',2),3)
        del(header_data[0])
        list(map(decode,list(filter(lambda conent: conent!='',header_data))))
         # Parse POST.
        if ret.REQUEST_METHOD == 'POST':
            if ret.CONTENT_TYPE:
                if ret.CONTENT_TYPE == 'multipart/form-data':
                    self.parseUploadFiles(http_body, http_post_boundary)
                elif ret.CONTENT_TYPE == 'application/x-www-form-urlencoded':
                    ret.POST =  parse_qs(http_body)
                else:
                    ret.HTTP_RAW_REQUEST_DATA = ret.HTTP_RAW_POST_DATA = http_body
            else:
                ret.HTTP_RAW_REQUEST_DATA = ret.HTTP_RAW_POST_DATA = http_body
        if ret.REQUEST_METHOD == 'PUT':
            ret.HTTP_RAW_REQUEST_DATA = http_body
        if ret.REQUEST_METHOD == 'DELETE':
            ret.HTTP_RAW_REQUEST_DATA = http_body
        ret.QUERY_STRING = urlparse(ret.REQUEST_URI)
        if ret.QUERY_STRING:
            ret.GET = parse_qs(ret.QUERY_STRING.params)
        else:
            ret.QUERY_STRING = ''
        ret.REQUEST = dict(ret.GET, **ret.POST)
        ret.REMOTE_ADDR = '1.1.1.1'
        ret.REMOTE_PORT = 80
        return ret
    # 加密函数
    def encode(self,content):
        header = 'HTTP/1.1 200 OK\r\n'
        header += 'Server: easy server\r\nContent-Length: '+ str(len(content)) +'\r\n\r\n'
        return  header+content
    # 参数转化
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
    # 获取报文基础信息，size
    def getInfo(self,con,data):
        (header) = self.listToArgs(data.split('\r\n\r\n',1),1)
        (METHOD) = self.listToArgs(header.split(' ', 1), 1)
        if METHOD in self.methods:
            return self.getSize(header,METHOD)
        else:
            con.send('HTTP/1.1 400 Bad Request\r\n\r\n')
            return 0
    # 获取size
    def getSize(self,header,method):
        if method == 'GET' or method == 'HEAD' or method == 'OPTIONS':
            return len(header)+4
        p1 = r"(\r\nContent-Length: ?(\d+))"  # 这是我们写的正则表达式规则，你现在可以不理解啥意思
        pattern1 = re.compile(p1)  # 我们在编译这段正则表达式
        matcher1 = re.search(pattern1, header)  # 在源文本中搜索符合正则表达式的部分
        content_length = matcher1.group(0)  # 打印出来
        return content_length + len(header) + 4
# 解码后的类
class httpData(object):
    GET = {}                          # get 请求参数
    POST = {}                         # post 请求参数
    REQUEST = {}                      # 请求参数
    COOKIE = {}                        # cookie
    CONTENT_TYPE = None                 # 内容类型
    QUERY_STRING = None                 # 未解析的原始请求字符串
    REQUEST_METHOD = None               # 请求方式
    REQUEST_URI = None                  # 当前URL的 路径地址
    SERVER_PROTOCOL = None              # 请求页面时通信协议的名称和版本
    SERVER_SOFTWARE = 'easy server'   # 服务器标识的字串
    SERVER_NAME = None                  # 服务器主机的名称
    HTTP_HOST = None                    # 当前请求的 Host: 头部的内容
    HTTP_USER_AGENT = None              # 当前请求的 User_Agent: 头部的内容
    HTTP_ACCEPT = None                  # 当前请求的 Accept: 头部的内容
    HTTP_ACCEPT_LANGUAGE = None         # 浏览器语言
    HTTP_ACCEPT_ENCODING = None         # 当前请求的 Accept-Encoding: 头部的内容
    HTTP_COOKIE = None                  # cookie
    HTTP_CONNECTION = None              # 当前请求的 Connection: 头部的内容。例如：“Keep-Alive”
    REMOTE_ADDR = None                  # 当前用户 IP
    REMOTE_HOST = None                  # 当前用户主机名
    REMOTE_PORT = None                  # 端口
    REQUEST_TIME = time()
