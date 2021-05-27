from scapy.all import rdpcap
from scapy.layers.inet import UDP
from scapy.layers.dns import DNS, DNSQR

#Este programa recibe como argumento un archivo .pcap de trafico de una maquina infectada por conficker
#Como conficker usaba un domain_flux attack, esta herramienta nos permite distinguir dominios que no se resuelven con DNS

def dns_QR_test(pkt):
    if pkt.getlayer(UDP).sport == 53:
        rcode = pkt.getlayer(DNS).rcode
        qname = pkt.getlayer(DNSQR).qname
        if rcode == 3:
            print(f'[!] No se encontró el siguiente dominio: {qname}')
            return True
    return False


if __name__ == '__main__':
    unans_reqs = 0
    pkts = rdpcap('domain_flux.pcap')
    for _pkt in pkts:
        if dns_QR_test(_pkt):
            unans_reqs += 1
    print(f'[!] {str(unans_reqs)} Solicitudes de Nombre sin Responder')
