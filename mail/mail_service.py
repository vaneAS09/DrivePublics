##
#Drives públicos
#Autor : Vanessa Ayala Salas
#Descripción: Se crea la clase para la definición del servicio de envío de correo automático desde Python

##
#Se Importan las librerías correspondientes
import smtplib 
import json

#Se importa el archivo de configuración

with open('./mail/setting_mail.json') as file: setting_mail = json.load(file)


#Se construye la clase para el servicio de envío de correo

class mail_service:
    
    def send_mail(receiver):
        try:
            #se construye la estructura de envío de correo desde el archivo de configuración.

            message = f"Subject: {setting_mail['MESSAGE']['subject']}\n\n{setting_mail['MESSAGE']['message']}" 

            # Configuracion del servidor
            server = smtplib.SMTP('smtp.gmail.com', 587) 
            server.starttls() 
            #logueo con credenciales, parametros(usuario, contraseña)
            server.login(setting_mail['USER']['user'], setting_mail['USER']['password']) 
            #Envío de correo, parametros(remitente, destinatario, mensaje)
            server.sendmail(setting_mail['USER']['sender'],receiver,message) 
            server.quit() 

            print("El correo se ha enviado satisfactoriamente")

        except:
            print("Por favor valide los datos de envío de correo en el archivo"
            + " " + "setting_mail.json"
            )
