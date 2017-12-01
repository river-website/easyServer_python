from easy import *
if __name__ == '__main__':
    serverData = {}
    servers = {}
    host = '0.0.0.0'
    port = 88
    addr = (host,port)
    addrData = 'data'
    serverData[addr] = addrData
    servers['webServer'] = serverData
    easy().start(servers)
