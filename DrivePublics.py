##
#Drives públicos
#Autor : Vanessa Ayala Salas
#Descripción: Método principal encargado de ejecutar las funciones para el desarrollo de la aplicación.

##

# Se importan las librerías necesarias para la ejecución de los métodos en la aplicación.

import os
import database.db as db
from autentication.loguin import service_loguin
from mail.mail_service import mail_service
from database.service_db import service_db
import json

#Se importa el archivo de configuración con los parámetros de filtrado en el metadatos del archivo

with open('./data_query.json') as file: data_query = json.load(file)

# Se define el método buscar para traer la información de los metadatos de los archivos en el drive.

def search(id_folder): #cambiar nombre del método
    
    result = []
    credential = service_loguin.login()
    
    list_files = credential.ListFile({'q': f"parents in '{id_folder}' "}).GetList()
    for f in list_files:
        result.append(f)
    
    return result

# Definición del main.

if __name__ == "__main__":
    
#Parámetros para búsquedas en carpeta

    id_folder = data_query['PARAMS_QUERY']['id_folder']

#Creación de la base de datos.

    if not os.path.exists('driveFiles.db'):
        db

try:
    metadata = search(id_folder)
 
    for data in metadata:

            # Se llama el servicio para la creación y actualización de la información en la base de datos.
                    
            service_db.create_data(data['id'], data['title'], data['fileExtension'], 
                        data['owners'][0]['displayName'], data['shared'], 
                        data['modifiedDate'])

            # Se Valida si el archivo es público y se cambia a privado en el Drive de Google consultado.

            if data['shared'] == True: 

                print(data['title'])
                print(data['owners'][0]['displayName'])

                permissions = data.GetPermissions()
                for permission in permissions:
                    if permission['role'] != 'owner':
                        id = permission['id']
                        data.DeletePermission(id)

            # Se llama el servicio para la actualización del historial de acrhivo público
                        service_db.save_history(data['id'])

            # Se crea un método para enviar correo electrónico al propietario cuando se realice el cambio de un archivo de público a privado.
                    try:
                        email = data['owners'][0]['emailAddress']
                        mail_service.send_mail(email)

                    except:
                        print("Usuario o contraseña de app sevicio de correo errado, por favor verifique el archivo de configuración")

except:
    print("El Id de carperta está errado o no existe, por favor verifique el archivo de configuración"
    + " " +"data_query.json"
    )
    