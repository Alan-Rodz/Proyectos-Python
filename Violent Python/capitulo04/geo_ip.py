import argparse
import geoip2.database

#Recibe una direccion IP, consulta a geolite2_city.mmdb, nos regresa la ubicación de la dirección IP

def imprimir_registro(target_ip):
    """ This function is not part of the original code of Violent
    Python. It used the deprecated 'pygeoip' library to perform
    the same task. A new solution using the API to the database
    provided by the MaxMind service has been implemented here by
    EONRaider. https://github.com/EONRaider"""

    with geoip2.database.Reader('geolite2_city.mmdb') as gi:
        rec = gi.city(target_ip)

        city = rec.city.name
        region = rec.subdivisions.most_specific.name
        country = rec.country.name
        lat = rec.location.latitude
        long = rec.location.longitude

        print(f'[*] Objetivo: {target_ip} Geo-localizado.')
        print(f'{"":>3}[+] {city}, {region}, {country}')
        print(f'{"":>3}[+] Latitud: {lat}, Longitud: {long}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        usage='python3 geo_ip.py TARGET_IP')
    parser.add_argument('tgt_ip', type=str, metavar='TARGET_IP',
                        help='IP address of the target to geolocate')

    imprimir_registro(parser.parse_args().tgt_ip)
