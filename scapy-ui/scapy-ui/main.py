import bottle
from bottle import request
from scapy.all import *

app = bottle.Bottle()

def get_nic_list():
    nic_list = []
    nic_ignore_list = ['lo', 'docker0', 'virbr0']
    with open('/proc/net/dev') as f:
        line = f.readline()
        while line is not None and line != '':
            if ':' not in line:
                line = f.readline()
                continue

            nic = line.split(':')[0].strip()

            if nic not in nic_ignore_list:
                nic_list.append(nic)

            line = f.readline()

    nic_list.sort()
    return nic_list

@app.route('/')
def index():
    return bottle.template('index', nic_list=get_nic_list())

@app.route('/sendpacket', method='POST')
def sendpacket():
    iface = request.forms.get('iface')
    src_mac = request.forms.get('src_mac')
    dst_mac = request.forms.get('dst_mac')
    src_ip = request.forms.get('src_ip')
    dst_ip = request.forms.get('dst_ip')
    protocol = request.forms.get('protocol')
    length = int(request.forms.get('length'))

    if protocol == 'TCP':
        flags = request.forms.get('flags')
        if flags == 'syn':
            packet = Ether(src=src_mac, dst=dst_mac)/IP(src=src_ip, dst=dst_ip)/TCP(sport=RandShort(), dport=80, flags='S', seq=12345)
        elif flags == 'ack':
            packet = Ether(src=src_mac, dst=dst_mac)/IP(src=src_ip, dst=dst_ip)/TCP(sport=RandShort(), dport=80, flags='A', ack=12346)
        elif flags == 'push':
            packet = Ether(src=src_mac, dst=dst_mac)/IP(src=src_ip, dst=dst_ip)/TCP(sport=RandShort(), dport=80, flags='P', seq=12345)/Raw(RandString(size=length))
        else:
            packet = None
    elif protocol == 'UDP':
        packet = Ether(src=src_mac, dst=dst_mac)/IP(src=src_ip, dst=dst_ip)/UDP(sport=RandShort(), dport=80)/Raw(RandString(size=length))
    elif protocol == 'ICMP':
        if len(src_mac) == 0:
            src_mac = None
        if len(dst_mac) == 0:
            dst_mac = None
        packet = Ether(src=src_mac, dst=dst_mac)/IP(src=src_ip, dst=dst_ip)/ICMP()/Raw(RandString(size=length))
    else:
        packet = None

    if packet is not None:
        sendp(packet, iface=iface)

    return bottle.template('result', packet=packet.summary())

if __name__ == '__main__':
    bottle.run(app, host='0.0.0.0', port=80)

