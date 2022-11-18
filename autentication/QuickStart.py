##
#Drives públicos
# Autor : Vanessa Ayala Salas
#Descripción: Método encargado de generar la autenticación segura con Google drive mediante la librería pydrive
# 
#Cambios (Versión)
#-------------------------------------
#No.           Fecha            Autor                    Descripción
# -----        ----------       --------------------     ---------------
# 1.0          13/11/2022       Vanessa Ayala Salas      Creación de la clase.
##

from pydrive.auth import GoogleAuth

# Creación local del webserver y autenticación automática.
gauth = GoogleAuth()
gauth.LocalWebserverAuth() 
