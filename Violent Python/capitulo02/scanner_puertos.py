import argparse
import socket
import threading

#Escaner de puertos básico
#host: página o IP a scannear, -p: puertos a scanear
#Uso: python3 scanner_puertos.py host -p 21,80
def scanear_puertos(tgt_host, tgt_puertos):
    try:
        tgt_ip = socket.gethostbyname(tgt_host)
    except socket.herror:
        print(f'[-] No se pudo encontrar {tgt_host}: Host desconocido')
        return

    try:
        tgt_nombre = socket.gethostbyaddr(tgt_ip)
        print(f'\n[+] Resultados del scan para: {tgt_nombre[0]}')
    except socket.herror:
        print(f'\n[+] Resultados del scan para: {tgt_ip}')

    socket.setdefaulttimeout(1)

    for puertos in tgt_puertos:
        t = threading.Thread(target=conectar_scan, args=(tgt_host, int(puertos)))
        t.start()


def conectar_scan(tgt_host, tgt_port):
    screen_lock = threading.Semaphore()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn_skt:
        try:
            conn_skt.connect((tgt_host, tgt_port))
            conn_skt.send(b'ViolentPython\r\n')
            results = conn_skt.recv(100).decode('utf-8')
            screen_lock.acquire()
            print(f'[+] {tgt_port}/tcp abierto')
            print(f'   [>] {results}')
        except OSError:
            screen_lock.acquire()
            print(f'[-] {tgt_port}/tcp cerrado')
        finally:
            screen_lock.release()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage='port_scan.py TARGET_HOST -p TARGET_PUERTOS'
              '\nexample: python3 port_scan.py scanme.nmap.org -p 21,80')

    parser.add_argument('tgt_host', type=str, metavar='TARGET_HOST',
                        help='specify target host (IP address or domain name)')
    parser.add_argument('-p', required=True, type=str, metavar='TARGET_PUERTOS',
                        help='specify target port[s] separated by comma '
                             '(no spaces)')
    args = parser.parse_args()

    args.tgt_ports = str(args.p).split(',')
    scanear_puertos(args.tgt_host, args.tgt_ports)
