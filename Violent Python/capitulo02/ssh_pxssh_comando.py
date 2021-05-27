from pexpect import pxssh


def enviar_comando(session, cmd):
    session.sendline(cmd)
    session.prompt()
    print(session.before.decode('utf-8'))


def conectar(host, user, password):
    try:
        session = pxssh.pxssh()
        session.login(host, user, password)
        return session
    except Exception as e:
        print(f'[-] Error Conectando: {e}')
        exit(0)


if __name__ == '__main__':
    conexion = conectar('127.0.0.1', 'root', 'toor')
    enviar_comando(conexion, 'sudo cat /etc/shadow | grep root')
