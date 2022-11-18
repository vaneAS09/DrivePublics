##
#Drives públicos
#Autor : Vanessa Ayala Salas
#Descripción: Se crea la clase que contiene la autenticación con Google y define la conexión al drive

##

from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

credentials = './autentication/credentials_module.json'

# Se define la conexión con el drive mediante autenticación con Google.

class service_loguin:
    def login():
        gauth = GoogleAuth()
        gauth.LoadCredentialsFile(credentials)
        
        if gauth.access_token_expired:
            gauth.Refresh()
            gauth.SaveCredentialsFile(credentials)
        else:
            gauth.Authorize()
            
        credential = GoogleDrive(gauth)
        return credential
