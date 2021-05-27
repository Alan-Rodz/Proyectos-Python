import socket
import struct
import textwrap

TAB_1 = '\t - '
TAB_2 = '\t\t - '
TAB_3 = '\t\t\t - '
TAB_4 = '\t\t\t\t - '

TAB_INFORMACION_1 = '\t '
TAB_INFORMACION_2 = '\t\t '
TAB_INFORMACION_3 = '\t\t\t '
TAB_INFORMACION_4 = '\t\t\t\t '

# procesa ethernet frames
def procesar_ethernet_frame(info):
    # ! es para indicar que estamos manejando informacion de red (big-little endian, etc)
    # 6s = 6 characters = los primeros 6 bytes
    # H = small unsigned int (2 bytes)
    mac_destino, mac_fuente, protocolo = struct.unpack('! 6s 6s H', info[:14])
    return formato_direccion_mac(mac_destino), formato_direccion_mac(mac_fuente), socket.htons(protocolo), info[14:]

# procesa direcciones MAC
def formato_direccion_mac(bytes_direccion):
    direccion_mac = map('{:02x}'.format, bytes_direccion)
    return ':'.join(direccion_mac).upper()

# procesa paquetes IPv4
def procesar_paquete_ipv4(informacion):
    longitud_header_version = informacion[0]
    version = longitud_header_version >> 4 
    longitud_header = (longitud_header_version & 15) * 4
    ttl, protocolo, fuente, destino = struct.unpack('! 8x B B 2x 4s 4s', informacion[:20])
    return version, longitud_header, ttl, protocolo, formato_ipv4(fuente), formato_ipv4(destino), informacion[longitud_header:] 

# regresa direcciones IPv4 correctas
def formato_ipv4(direccion):
    return '.'.join(map(str, direccion))

# procesa paquetes ICMP
def procesar_paquete_icmp(informacion):
    icmp_tipo, icmp_codigo, icmp_checksum = struct.unpack('! B B H', informacion[:4])
    return icmp_tipo, icmp_codigo, icmp_checksum, informacion[4:]

# procesa segmentos TCP
def procesar_segmento_tcp(informacion):
    (puerto_fuente, puerto_destino, secuencia, acknowledgement, banderas_reservadas_offset) = struct.unpack('! H H L L H', informacion[:14])
    offset = (banderas_reservadas_offset >> 12) * 4
    bandera_urg = (banderas_reservadas_offset & 32) >> 5
    bandera_ack = (banderas_reservadas_offset & 16) >> 4
    bandera_psh = (banderas_reservadas_offset & 8) >> 3
    bandera_rst = (banderas_reservadas_offset & 4) >> 2
    bandera_syn = (banderas_reservadas_offset & 2) >> 1
    bandera_fin = banderas_reservadas_offset & 1
    return puerto_fuente, puerto_destino, secuencia, acknowledgement, bandera_urg, bandera_ack, bandera_psh, bandera_rst, bandera_syn, bandera_fin, informacion[offset:]

# procesa segmentos UDP
def procesar_segmento_udp(informacion):
    puerto_fuente, puerto_destino, tamano = struct.unpack('! H H 2x H', informacion[:8])
    return puerto_fuente, puerto_destino, tamano, informacion[8:]

# Le da formato a informacion multi linea
def formato_multi_linea(prefijo, string, tamano=80):
    tamano -= len(prefijo)
    if isinstance(string, bytes):
        string = ''.join(r'\x{:02x}'.format(byte) for byte in string)
        if tamano % 2:
            tamano -= 1
    return '\n'.join([prefijo + line for line in textwrap.wrap(string, tamano)])



# main
def main():
    conexion = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    while True:
        informacion_sin_procesar, addr = conexion.recvfrom(65535)
        mac_destino, mac_fuente, protocolo_ethernet, info = procesar_ethernet_frame(informacion_sin_procesar)
        print('\nEthernet Frame:')
        print(TAB_1 + 'Destino: {}, Fuente: {}, Protocolo: {}'.format(mac_destino, mac_fuente, protocolo_ethernet))

        # 8 para IPv4
        if protocolo_ethernet == 8:
            (version, longitud_header, ttl, protocolo, fuente, destino, info) = procesar_paquete_ipv4(info)
            print(TAB_1 + 'Paquete IPv4: ')
            print(TAB_2 + 'Version: {}, Longitud de Cabecera: {}, TTL: {}'.format(version,longitud_header,ttl))
            print(TAB_2 + 'Protocolo: {}, Direccion Fuente: {}, Destino: {}'.format(protocolo, fuente,destino))

            # ICMP
            if protocolo == 1:
                icmp_tipo, icmp_codigo, icmp_checksum, info = procesar_paquete_icmp(info)
                print(TAB_1 + 'Paquete ICMP: ')
                print(TAB_2 + 'Tipo: {}, Codigo: {}, Checksum: {}'.format(icmp_tipo, icmp_codigo, icmp_checksum))
                print(TAB_2 + 'Informacion: ' )
                print(formato_multi_linea(TAB_INFORMACION_3, info))

            # TCP 
            elif protocolo == 6:
                (puerto_fuente, puerto_destino, secuencia, acknowledgement, bandera_urg, bandera_ack, bandera_psh, bandera_rst, bandera_syn, bandera_fin, info) = procesar_segmento_tcp(info)
                print(TAB_1 + 'Segmento TCP: ')
                print(TAB_2 + 'Puerto Fuente: {}, Puerto Destino: {}'.format(puerto_fuente, puerto_destino))
                print(TAB_2 + 'Secuencia: {}, Acknowledgement: {}'.format(secuencia, acknowledgement))
                print(TAB_2 + 'Banderas: ')
                print(TAB_3 + 'URG: {}, ACK: {}, PSH: {}, RST: {}, SYN: {}, FIN: {}'.format(bandera_urg, bandera_ack, bandera_psh, bandera_rst, bandera_syn, bandera_fin))
                print(TAB_2 + 'Informacion: ')
                print(formato_multi_linea(TAB_INFORMACION_3, info))

            # UDP
            elif protocolo == 17:
                puerto_fuente, puerto_destino, longitud, info = procesar_segmento_udp(info)
                print(TAB_1 + 'Segmento UDP: ')
                print(TAB_2 + 'Puerto Fuente: {}, Puerto Destino: {}, Longitud: {}'.format(puerto_fuente, puerto_destino, longitud))

            # Otro
            else:
                print(TAB_1 + 'Informacion: ')
                print(formato_multi_linea(TAB_INFORMACION_2, info))


main()
