import dpkt
import socket
import geoip2.database
import argparse

#Este programa nos dice las locaciones a las que viajan los paquetes que se envían en nuestra red
#Requiere que el archivo geolite2_city.mmdb esté presente ya que es el que contiene la base de datos de IPs
#Requiere un archivo .pcap en los argumentos, que es producido x wireshark

def ret_geo_str(ip):
    """ This function is not part of the original code of Violent
    Python. It used the deprecated 'pygeoip' library to perform
    the same task. A new solution using the API to the database
    provided by the MaxMind service has been implemented here by
    EONRaider. https://github.com/EONRaider"""

    try:
        with geoip2.database.Reader('geolite2_city.mmdb') as gi:
            rec = gi.city(ip)
            city = rec.city.name
            country = rec.country.name
            return f'{city}, {country}' if city else country

    except Exception as e:
        print(f'{"":>3}[-] Excepcion: {e.__class__.__name__}')
        return 'No registrado'


def imprimir_pcap(pcap_file):
    for ts, buf in pcap_file:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            print(f'[+] Fuente: {ret_geo_str(src)} --> Destino: {ret_geo_str(dst)}')
        except Exception as e:
            print(f'{"":>3}[-] Excepcion: {e.__class__.__name__}')
            pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage='python3 geo_print PCAP_FILE')
    parser.add_argument('pcap', type=str, metavar='PCAP_FILE',
                        help='specify the name of the PCAP file')
    args = parser.parse_args()
    pcap = args.pcap

    with open(pcap, 'rb') as file:
        pcap = dpkt.pcap.Reader(file)
        imprimir_pcap(pcap)