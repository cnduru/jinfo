from socket import *
import packet
s=socket(AF_INET, SOCK_DGRAM)
s.bind(('192.168.0.255',54545))

def generate_packet(packet):
    origin = packet.split(':')[3]
    payload = packet.split(':')[2]
    query = packet.split(':')[1]

    if query == 'master':
        print 'Resource Query \'%s\' with payload \'%s\' from %s' % (query, payload, origin)
        print 'Dispatchng reply \'#PACKET\''

def listen():
    print 'Listening for JINFO packets..'
    while True:
        m = s.recvfrom(1024)
        if 'RESQ' in m[0]:
            generate_packet(m[0])
        if 'RESR' in m[0]:
            origin = m[0].split(':')[2]
            query = m[0].split(':')[1]
            print 'Dispatching Resource Response \'%s\' to %s' % ('placeholder', 'placeholder')
            print 'Registering new host to record'
            write_record('master=%s' % origin)

def write_record(data):
    f = open('hosts.conf', 'w')
    f.write(data)
    f.close()

listen()
