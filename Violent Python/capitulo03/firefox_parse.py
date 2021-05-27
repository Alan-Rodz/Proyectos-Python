import re
import argparse
import os
import sqlite3

#Escanea los archivos .sqlite que guarda Firefox 

def imprimir_descargas(download_db):
    with sqlite3.connect(download_db) as conn:
        c = conn.cursor()
        c.execute("SELECT name, source, datetime(endTime/1000000, 'unixepoch') "
                  "FROM moz_downloads;")
        print('\n[*] -- Archivos descargados -- ')
        for row in c:
            print(f'{"":>3}[+] Archivo: {str(row[0])} desde fuente: '
                  f'{str(row[1])} en: {str(row[2])}')


def imprimir_cookies(cookies_db):
    try:
        with sqlite3.connect(cookies_db) as conn:
            c = conn.cursor()
            c.execute('SELECT host, name, value FROM moz_cookies')

            print('\n[*] -- Cookies Encontradas --')

            for row in c:
                host = str(row[0])
                name = str(row[1])
                value = str(row[2])
                print(f'{"":>3}[+] Host: {host}, Cookie: {name}, Valor: {value}')

    except Exception as e:
        if 'encrypted' in str(e):
            print(f'\n{"":>3}[*] Error leyendo las cookies desde la base de datos.'
                  f'{"":>3}[*] Actualiza tu librería Python-Sqlite3')


def imprimir_historial(places_db):
    try:
        with sqlite3.connect(places_db) as conn:
            c = conn.cursor()
            c.execute("select url, datetime(visit_date/1000000, 'unixepoch') "
                      "from moz_places, moz_historyvisits where "
                      "visit_count > 0 "
                      "and moz_places.id==moz_historyvisits.place_id;")

            print('\n[*] -- Historial Encontrado --')

            for row in c:
                url = str(row[0])
                date = str(row[1])
                print(f'{"":>3}[+] {date} - Visita a: {url}')

    except Exception as e:
        if 'encrypted' in str(e):
            print(f'\n{"":>3}[*] Error leyendo la base de datos places.'
                  f'{"":>3}[*] Actualiza tu librería Python-Sqlite3')


def print_google(places_db):
    with sqlite3.connect(places_db) as conn:
        c = conn.cursor()
        c.execute("select url, datetime(visit_date/1000000, 'unixepoch') "
                  "from moz_places, moz_historyvisits where visit_count > 0 "
                  "and moz_places.id==moz_historyvisits.place_id;")

        print('\n[*] -- Queries a Google Encontrados: --')

        for row in c:
            url = str(row[0])
            date = str(row[1])
            if 'google' in url.lower():
                r = re.findall(r'q=.*', url)
                if r:
                    search = r[0].split('&')[0]
                    search = search.replace('q=', '').replace('+', ' ')
                    print(f'[+] {date} - Se buscó: {search}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        usage='python3 firefox_parse.py FIREFOX_PROFILE')
    parser.add_argument('firefox_prof', type=str, metavar='FIREFOX_PROFILE',
                        help='specify path to the directory containing '
                             'the firefox profile database file(s)')

    args = parser.parse_args()
    path_name = args.firefox_prof

    download_dbase = os.path.join(path_name, 'downloads.sqlite')
    if os.path.isfile(download_dbase):
        imprimir_descargas(download_dbase)
    else:
        print(f'[!] La base de datos de Descargas no existe: {download_dbase}')

    cookies_dbase = os.path.join(path_name, 'cookies.sqlite')
    if os.path.isfile(cookies_dbase):
        imprimir_cookies(cookies_dbase)
    else:
        print(f'[!] La base de datos de Cookies no existe: {cookies_dbase}')

    places_dbase = os.path.join(path_name, 'places.sqlite')
    if os.path.isfile(places_dbase):
        imprimir_historial(places_dbase)
        print_google(places_dbase)
    else:
        print(f'[!] La base de datos de Places no existe: {places_dbase}')
