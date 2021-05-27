import pexpect

PROMPT = ['# ', '>>> ', '> ', '\$ ']


def enviar_comando(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before.decode('utf-8'))


def conectar(host, user, password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    conn_str = f'ssh {user}@{host}'
    child = pexpect.spawn(conn_str)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])

    if not ret:
        print('[-] Error Conectando')
        return
    else:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])
        if not ret:
            print('[-] Error Conectando')
            return

    child.sendline(password)
    child.expect(PROMPT)
    return child


if __name__ == '__main__':
    tgt_host = 'localhost'
    tgt_user = 'root'
    tgt_passwd = 'toor'

    conexion = conectar(tgt_host, tgt_user, tgt_passwd)
    enviar_comando(conexion, 'sudo cat /etc/shadow | grep root')
