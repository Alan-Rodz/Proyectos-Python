from pexpect import pxssh


class Client:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.conectar()

    def conectar(self):
        try:
            session = pxssh.pxssh()
            session.login(self.host, self.user, self.password)
            return session
        except Exception as e:
            print(f'[-] Error conectando: {e}')

    def enviar_comando(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before


def comando_botnet(command):
    for client in botnet:
        output = client.send_command(command).decode('utf-8')
        print(f'[*] Output de {client.host}')
        print(f'[+] {output}')


def agregar_cliente(host, user, password):
    client = Client(host, user, password)
    botnet.append(client)


if __name__ == '__main__':
    botnet = []
    agregar_cliente('127.0.0.1', 'root', 'toor')
    agregar_cliente('127.0.0.1', 'root', 'toor')
    agregar_cliente('127.0.0.1', 'root', 'toor')

    comando_botnet('uname -v && cat /etc/issue')
