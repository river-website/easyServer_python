from system.easy import *

# to easy
servers = dict()
# a server a server data
serverData = dict()
# 一个ip端口，一个数据
hostData = 'data'
hostIP = ('0.0.0.0',88)
# 一种协议服务，多个host数据
serverData[hostIP] = hostData

hostData = 'data'
hostIP = ('0.0.0.0',99)
serverData[hostIP] = hostData
servers['ezWebServer'] = serverData

# serverData = dict()
# hostData = 'data'
# hostIP = '0.0.0.0:82'
# serverData[hostIP] = hostData
# hostData = 'data'
# hostIP = '0.0.0.0:83'
# serverData[hostIP] = hostData
# servers['WebSocketServer'] = serverData

ez = easy(servers)
ez.start()