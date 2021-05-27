import nmap
import argparse


def scan_nmap(tgt_host, tgt_puertos):
    nm_scan = nmap.PortScanner()
    for tgt_puerto in tgt_puertos:
        nm_scan.scan(tgt_host, tgt_puerto)
        state = nm_scan[tgt_host]['tcp'][int(tgt_puerto)]['state']
        print(f'[*] {tgt_host} tcp/{tgt_puerto} {state}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage='nmap_scan.py TARGET_HOST -p TARGET_PUERTOS')
    parser.add_argument('host', type=str, metavar='TARGET_HOST',
                        help="especifica la direccion IP del host")
    parser.add_argument('-p', type=str, metavar='TARGET_PUERTOS',
                        help='especifica los puertos del host separados por una coma (no espacios)')
    args = parser.parse_args()

    args.puertos = str(args.p).split(',')
    scan_nmap(args.host, args.puertos)
