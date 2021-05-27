import argparse
from scapy.all import sr1, sniff, conf
from scapy.layers.inet import IP, ICMP
from IPy import IP as IPTEST

ttl_values = {}

#Abre una network interface, recibe paquetes, los checa para ver si el TTL de los mismos es el que debería

def checar_TTL(ipsrc, ttl):
    if IPTEST(ipsrc).iptype() == 'PRIVATE':
        return

    if ipsrc not in ttl_values:
        pkt = sr1(IP(dst=ipsrc) / ICMP(), retry=0, timeout=1, verbose=0)
        ttl_values[ipsrc] = pkt.ttl

    if abs(int(ttl) - int(ttl_values[ipsrc])) > THRESH:
        print(f'\n[!] Se detecto paquete posiblemente spoofed desde: {ipsrc}')
        print(f'[!] TTL: {ttl}, TTL Real: {str(ttl_values[ipsrc])}')


def probar_TTL(pkt):
    try:
        if pkt.haslayer(IP):
            ipsrc = pkt.getlayer(IP).src
            ttl = str(pkt.ttl)
            checar_TTL(ipsrc, ttl)
    except Exception as e:
        print(f'{"":>3}[-] Excepcion: {e.__class__.__name__}')
        pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage='python3 spoof_detect.py [-i INTERFACE] [-t THRESHOLD]')
    parser.add_argument('-i', type=str, metavar='INTERFACE', default='eth0',
                        help='specify the network interface')
    parser.add_argument('-t', type=int, metavar='THRESHOLD', default=5,
                        help='specify the threshold count')

    args = parser.parse_args()
    conf.iface = args.i
    THRESH = args.t

    sniff(prn=probar_TTL, store=0)
