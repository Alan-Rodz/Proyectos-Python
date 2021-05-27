import dpkt
import argparse
import socket

#Este programa recibe archivos .pcap y nos dice si en los mismos hay presentes:
#Una evidencia de descarga de LOIC
#Una evidencia de ataque usando LOIC
#Una evidencia de uso de Hivemind con LOIC

def encontrar_descarga(pcap):
    for ts, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            tcp = ip.data
            http = dpkt.http.Request(tcp.data)

            if http.method == 'GET':
                uri = http.uri.lower()
                if '.zip' in uri and 'loic' in uri:
                    print(f'[!] {src} descargo LOIC.')

        except Exception as e:
            print(f'[-] Excepcion: {e.__class__.__name__}')
            pass


def encontrar_hivemind(pcap):
    for ts, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            tcp = ip.data
            dport = tcp.dport
            sport = tcp.sport

            if dport == 6667 and b'!lazor' in tcp.data.lower():
                print(f'[!] DDoS Hivemind issued by: {src}')
                print(f'{"":>3}[+] Objetivo CMD: {tcp.data.decode("utf-8")}')

            if sport == 6667 and b'!lazor' in tcp.data.lower():
                print(f'[!] DDoS Hivemind issued to: {dst}')
                print(f'{"":>3}[+] Objetivo CMD: {tcp.data.decode("utf-8")}')

        except Exception as e:
            print(f'{"":>3}[-] Excepcion: {e.__class__.__name__}')
            pass


def encontrar_ataque(pcap):
    pkt_count = {}

    for ts, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            tcp = ip.data
            dport = tcp.dport

            if dport == 80:
                stream = f'{src}:{dst}'
                if stream in pkt_count:
                    pkt_count[stream] = pkt_count[stream] + 1
                else:
                    pkt_count[stream] = 1

        except Exception as e:
            print(f'{"":>3}[-] Excepcion: {e.__class__.__name__}')
            pass

    for stream in pkt_count:
        pkts_sent = pkt_count[stream]
        if pkts_sent > THRESH:
            src = stream.split(':')[0]
            dst = stream.split(':')[1]
            print(f'[+] {src} ataco a {dst} con {str(pkts_sent)} paquetes.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage='python3 find_ddos.py PCAP_FILE [-t THRESH]')
    parser.add_argument('pcap_file', type=str, metavar='PCAP_FILE',
                        help='specify the name of the pcap file')
    parser.add_argument('-t', type=int, metavar='THRESH', default=1000,
                        help='specify threshold count ')

    args = parser.parse_args()
    pcap_file = args.pcap_file
    THRESH = args.t

    with open(pcap_file, 'rb') as file:
        _pcap = dpkt.pcap.Reader(file)
        encontrar_descarga(_pcap)
        encontrar_hivemind(_pcap)
        encontrar_ataque(_pcap)
