#   server
#   accept  ->  client socket   ->  read decode ->  buss service    ->  encode write
#   1)accept    2)client socket   ->  read decode   ->  encode write    3)buss service
#   server: 1)processPool;  2)sign process
#   2)sign process(1p)
#   1: use sign
#   1+2+3   all(1);         reactor;                                      but:1.cannot use mutil cpu;2.3 longtime.use in: cpu program
#   1+2-3   all(1+100):     rector+threadpool(normal)                   but thread cannot use mutil cpu.        use in: i/o program
#   1-2+3   all(1+100):     rector||normal+threadpool(normal)  but thread cannot use mutil cpu         use in: i/o program
#   1-2-3   all(1+4+100); rector||normal+threadpool(reactor)+threadpool(normal)
#   1:use pool
#

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