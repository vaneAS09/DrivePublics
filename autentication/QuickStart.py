##
#Drives públicos
#Autor : Vanessa Ayala Salas
#Descripción: Método encargado de generar la autenticación segura con Google drive mediante la librería pydrive
##

from pydrive.auth import GoogleAuth

# Creación local del webserver y autenticación automática.
gauth = GoogleAuth()
gauth.LocalWebserverAuth() 
