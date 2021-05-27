from scapy.all import rdpcap
from scapy.layers.dns import DNSRR

dns_records = {}

#Este programa recibe como argumento un archivo .pcap con trafico que queremos analizar 
#Nos dice la cantidad de IPs unicas que tienen los dominios presentes en el .pcap
#Esto se hace para poder detectar dominios especificos de un ataque fast_flux

def procesar_paquete(pkt):
    if pkt.haslayer(DNSRR):
        rrname = pkt.getlayer(DNSRR).rrname
        rdata = pkt.getlayer(DNSRR).rdata
        if rrname in dns_records:
            if rdata not in dns_records[rrname]:
                dns_records[rrname].append(rdata)
        else:
            dns_records[rrname] = []
            dns_records[rrname].append(rdata)


if __name__ == '__main__':
    pkts = rdpcap('fast_flux.pcap')
    for _pkt in pkts:
        procesar_paquete(_pkt)
    
    for item in dns_records:
        print(f"[+] {item.decode('utf-8')} tiene {str(len(dns_records[item]))} "
              f"IPs unicas.")
