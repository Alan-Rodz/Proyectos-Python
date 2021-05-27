import os
import sqlite3
import argparse

#Escanea el archivo backup de un iPhone y muestra los mensajes (untested)

def es_db_mensajes(iphonedb):
    try:
        with sqlite3.connect(iphonedb) as conn:
            c = conn.cursor()
            c.execute("SELECT tbl_name FROM sqlite_master WHERE type=='table';")
            for row in c:
                if 'message' in str(row):
                    return True
    except Exception as exc:
        print(f'[-] Exception: {exc.__class__.__name__}')
        return False


def imprimir_mensaje(msgdb):
    try:
        with sqlite3.connect(msgdb) as conn:
            c = conn.cursor()
            c.execute("select datetime(date,'unixepoch'), address, text "
                      "from message WHERE address > 0;")
            for row in c:
                date = str(row[0])
                addr = str(row[1])
                text = row[2]
                print(f'\n[+] Fecha: {date}, Direccion: {addr}, Mensaje: {text}')
    except Exception as exc:
        print(f'[-] Excepcion: {exc.__class__.__name__}')
        pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage='python3 iphone_messages.py IPHONE_BACKUP_DIR')
    parser.add_argument('backup_dir', type=str, metavar='IPHONE_BACKUP_DIR',
                        help='specify the path to the directory containing the '
                             'iPhone backup file(s)')
    args = parser.parse_args()
    path_name = args.backup_dir
    dir_list = os.listdir(path_name)

    for filename in dir_list:
        iphone_db = os.path.join(path_name, filename)
        if es_db_mensajes(iphone_db):
            try:
                print('\n[*] --- Mensajes Encontrados ---')
                imprimir_mensaje(iphone_db)
            except Exception as e:
                print(f'[-] Excepcion: {e.__class__.__name__}')
                pass
