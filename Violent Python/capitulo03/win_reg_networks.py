import argparse
import requests
import winreg

#Escanea las redes del registro de Windows para decirnos de dónde se ha conectado la máquina actual,
#haciendo consultas a Wigle

def valor_a_direccion(val):
    addr = ''
    print(val)
    for ch in val:
        print(ch)
        addr += '%02x ' % ord(ch)
    return addr.strip(' ').replace(' ', ':')[:17]


def imprimir_wigle(username, password, netid):
    """ This function is not part of the original code of Violent 
    Python. It used the deprecated 'mechanize' library to perform
    the same task. A new solution using the API to the WiGLE
    service has been implemented here by EONRaider.
    https://github.com/EONRaider"""

    url = "https://api.wigle.net/api/v2/network/detail"
    net_info = requests.get(url, auth=(username, password),
                            params=netid)
    net_info.raise_for_status()
    response = net_info.json()

    try:
        map_lat = response['results'][0]['trilat']
        map_lon = response['results'][0]['trilong']
        print(f'[-] Lat: {map_lat}, Lon: {map_lon}')
    except KeyError:
        print(f'{"":>3}[-] {response["message"]}')


def print_nets(username, password):
    net = "SOFTWARE\Microsoft\Windows NT\CurrentVersion\\NetworkList\Signatures\\Unmanaged"
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, net)
    print('\n[*] Redes a las que te has unido.')

    for i in range(100):
        try:
            guid = winreg.EnumKey(key, i)
            net_key = winreg.OpenKey(key, str(guid))
            (n, addr, t) = winreg.EnumValue(net_key, 5)
            (n, name, t) = winreg.EnumValue(net_key, 4)
            mac_addr = valor_a_direccion(addr)
            net_name = str(name)
            print(f'[+] {net_name} {mac_addr}')
            imprimir_wigle(username, password, mac_addr)
            winreg.CloseKey(net_key)
        except IndexError:
            break
        except OSError as e:
            print(f'{"":>3}[-] Excepcion: {e}')
            break


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage='python3 discover_networks.py -u WIGLE_USERNAME '
              '-p WIGLE_PASSWORD')
    parser.add_argument('-u', type=str, metavar='WIGLE_USERNAME', required=True,
                        help='specify WiGLE username')
    parser.add_argument('-p', type=str, metavar='WIGLE_PASSWORD', required=True,
                        help='specify WiGLE password')
    args = parser.parse_args()

    print_nets(args.u, args.p)
