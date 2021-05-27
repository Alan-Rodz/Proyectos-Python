import ftplib


def anon_login(hostname):
    ftp = ftplib.FTP(hostname)
    try:
        ftp.login('anonymous', 'me@your.com')
        print(f'\n[*] {str(hostname)} FTP Login Anonimo Exitoso.')
        return True
    except Exception as e:
        print(f'\n[-] {str(hostname)} FTP Login Anonimo Ha Fallado.')
        print(f'[-] Excepcion: {e}')
        return False
    finally:
        ftp.quit()


if __name__ == "__main__":
    host = ''
    anon_login(host)
