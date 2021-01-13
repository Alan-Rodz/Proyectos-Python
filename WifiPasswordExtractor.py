import subprocess

#Recuperamos la informacion de las redes
informacion = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

#Filtramos la informacion y obtenemos solamente las redes
wifis = [linea.split(':')[1][1:-1] for linea in informacion if "All User Profile" in linea]

for wifi in wifis:
    resultados = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8').split('\n')
    resultados = [linea.split(':')[1][1:-1] for linea in resultados if "Key Content" in linea]
    try:
        print(f'Nombre: {wifi}, Contraseña: {resultados[0]}')
    except IndexError:
        print(f'Nombre: {wifi}, Contraseña: No puede ser leida!')

