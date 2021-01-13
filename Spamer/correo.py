import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

#Recuperamos nuestro usuario
with open("usuario.txt", "r") as f:
    usuario = f.read()

#Recuperamos nuestra contraseña
with open("contraseña.txt", "r") as f:
    contraseña = f.read()

#Recuperamos el destinatario de nuestro correo
with open("destinatario.txt", "r") as f:
    destinatario = f.read()

#Tema de nuestro correo
tema = "Saludos desde Python!"

#Mensaje que enviaremos
with open("mensaje.txt", "r") as f:
    mensaje = f.read()

def enviarCorreo(usuario, contraseña, destinatario, tema, mensaje):

    #Servidor SMTP
    servidor = smtplib.SMTP("smtp.gmail.com", 25)

    #Arrancamos el servidor
    servidor.ehlo()
    servidor.starttls()

    #Hacer login en nuestra cuenta
    servidor.login(usuario, contraseña)

    #Creamos el mensaje que queremos enviar
    msj = MIMEMultipart()
    msj["From"] = usuario
    msj["To"] = destinatario
    msj["Subject"] = tema

    #Ponemos todo dentro de un objeto mensaje
    msj.attach(MIMEText(mensaje, "plain"))

    #Añadimos imágenes
    nombreArchivo = "img.jpg"
    archivoAdjunto = open(nombreArchivo, "rb")

    #Creamos un "objeto carga"
    p = MIMEBase("application", "octet-stream")
    p.set_payload(archivoAdjunto.read())

    #Codificar la imagen
    encoders.encode_base64(p)
    p.add_header("Content-Disposition", f"archivoAdjunto; filename={nombreArchivo}")

    #Luego añadimos la imagen al objeto mensaje
    msj.attach(p)

    #Convertimos todo a texto para que pueda ser enviado
    texto = msj.as_string()

    #Enviamos el correo
    servidor.sendmail(usuario, destinatario, texto)
 
#Aquí escribimos la cantidad de veces que queremos enviar el correo
for i in range(3):
    enviarCorreo(usuario, contraseña, destinatario, tema, mensaje)
    
    #Esto nos sirve para ver la iteración en la que vamos. 
    print(i)
