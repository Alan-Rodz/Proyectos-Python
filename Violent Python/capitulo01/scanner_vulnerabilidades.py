import socket
import os
import sys


def ret_banner(ip, puerto):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, puerto))
        banner = s.recv(1024)
        return banner
    except OSError:
        return


def checar_vulnerabilidades(banner, nombreArchivo):
    with open(nombreArchivo) as file:
        for linea in file.readlines():
            if linea.strip('\n') in banner.strip('\n'):
                print(f'[+] El servidor es vulnerable: {banner}')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        _filename = sys.argv[1]
        if not os.path.isfile(_filename):
            print(f'[-] {_filename} no existe.')
            exit(0)

        if not os.access(_filename, os.R_OK):
            print(f'[-] {_filename} acceso denegado.')
            exit(0)

        lista_puertos = [21, 22, 25, 80, 110, 443]

        for x in range(147, 150):
            _ip = '192.168.95.' + str(x)
            for _puerto in lista_puertos:
                _banner = ret_banner(_ip, _puerto)
                if _banner:
                    print(f'[+] {_ip}: {_banner}')
                    checar_vulnerabilidades(_banner, _filename)

    else:
        print(f'[-] Uso: {str(sys.argv[0])} <vuln filename>')
        exit(0)
