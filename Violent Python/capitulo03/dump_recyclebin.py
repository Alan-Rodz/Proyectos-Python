import os
from winreg import OpenKey, QueryValueEx, HKEY_LOCAL_MACHINE

#Nos dice los tipos de archivo recientemente eliminados en la papelera de reciclaje 

def sid_a_usuario(sid):
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE,
                      "SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList"
                      + '\\' + sid)
        value, _type = QueryValueEx(key, 'ProfileImagePath')
        user = value.split('\\')[-1]
        return user
    except Exception as e:
        print(f'{"":>3}[-] Excepcion: {e}')
        return sid


def regresar_directorio():
    dirs = ['C:\\Recycler\\', 'C:\\Recycled\\', 'C:\\$Recycle.Bin\\']
    for directorio_reciclado in dirs:
        if os.path.isdir(directorio_reciclado):
            return directorio_reciclado
    return None


def encontrar_reciclado(directorio_reciclado):
    dir_list = os.listdir(directorio_reciclado)
    for sid in dir_list:
        files = os.listdir(directorio_reciclado + sid)
        user = sid_a_usuario(sid)
        print(f'\n[*] Enlistando archivos para el usuario: {str(user)}')
        for file in files:
            print(f'[+] Archivo encontrado: {str(file)}')


if __name__ == '__main__':
    recycled_dir = regresar_directorio()
    encontrar_reciclado(recycled_dir)
