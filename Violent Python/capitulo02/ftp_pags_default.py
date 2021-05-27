import ftplib


def return_default(ftp):
    try:
        dir_list = ftp.nlst()
    except Exception as e:
        print(f'[-] No se pudieron enlistar los contenidos del directorio.\n'
              f'[-] Saltando al siguiente objetivo.\n'
              f'[-] Excepcion: {e}')
        return

    ret_list = []
    for file in dir_list:
        fn = file.lower()
        if '.php' in fn or '.htm' in fn or '.asp' in fn:
            print(f'[+] Se encontro pagina default: {file}')
        ret_list.append(file)
    return ret_list


if __name__ == "__main__":
    tgt_host = '192.168.95.179'
    username = 'guest'
    password = 'guest'

    ftp_conn = ftplib.FTP(tgt_host)
    ftp_conn.login(username, password)
    return_default(ftp_conn)
