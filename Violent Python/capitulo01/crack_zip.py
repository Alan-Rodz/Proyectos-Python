import zipfile
import argparse
from threading import Thread


def extraer_archivo(zfile, contraseña):
    try:
        zfile.extractall(pwd=contraseña.encode('utf-8'))
        print(f'[+] Contraseña encontrada: {contraseña}\n')
    except RuntimeError:
        pass


def main(zname, dname):
    z_file = zipfile.ZipFile(zname)
    with open(dname) as pass_file:
        for linea in pass_file.readlines():
            contraseña = linea.strip('\n')
            t = Thread(target=extraer_archivo, args=(z_file, contraseña))
            t.start()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage='zip_crack.py ARCHIVOZIP ARCHIVODICCIONARIO')
    parser.add_argument('archivozip', type=str, metavar='ARCHIVOZIP',
                        help='especifica el archivo zip')
    parser.add_argument('archivodiccionario', type=str, metavar='ARCHIVODICCIONARIO',
                        help='especifica el archivo diccionario')
    args = parser.parse_args()
    main(args.archivozip, args.archivodiccionario)
