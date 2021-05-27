from crypt import crypt


def probar_contraseña(contraseña_encriptada):
    sal = contraseña_encriptada[:2]
    archivo_diccionario = open('diccionario.txt', 'r')

    for palabra in archivo_diccionario.readlines():
        palabra_encriptada = crypt(palabra.strip('\n'), sal)
        if palabra_encriptada == contraseña_encriptada:
            print(f'[+] Contraseña Encontrada: {palabra}\n')
            return

    print('[-] Contraseña no encontrada.\n')
    return


if __name__ == '__main__':
    archivo_contraseñas = open('contraseñas.txt')
    for linea in archivo_contraseñas.readlines():
        if ':' in linea:
            usuario = linea.split(':')[0]
            _contraseña_encriptada = linea.split(':')[1].strip()
            print(f'[*] Crackeando contraseña para usuario: {usuario}')
            probar_contraseña(_contraseña_encriptada)
