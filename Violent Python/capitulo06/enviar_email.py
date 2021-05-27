import smtplib
from email.mime.text import MIMEText


def enviar_mail(user, pwd, to, subject, text):
    msg = MIMEText(text)
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp_server:
            print("[+] Conectando al Servidor de Email.")
            smtp_server.ehlo()

            print("[+] Comenzando sesión encriptada.")
            smtp_server.starttls()
            smtp_server.ehlo()

            print("[+] Iniciando sesión en el Servidor de Email.")
            smtp_server.login(user, pwd)

            print("[+] Enviando Email.")
            smtp_server.sendmail(user, to, msg.as_string())

        print("[+] Email enviado de manera exitosa.")

    except Exception as e:
        print(f'[-] Fallo al enviar el Email.\n'
              f'[-] Excepion: {e.__class__.__name__}')


if __name__ == '__main__':
    _user = 'username'
    _pwd = 'password'

    enviar_mail(_user, _pwd, 'target@tgt.tgt', 'Re: Important', 'Test Message')
