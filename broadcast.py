from socket import *
cs = socket(AF_INET, SOCK_DGRAM)
cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
cs.sendto('RESQ:master:192.168.0.12:192.168.0.12', ('192.168.0.255', 54545))
#cs.sendto('RESR:master:192.168.0.12:192.168.0.12', ('192.168.0.255', 54545))
print 'sent UDP packet'
