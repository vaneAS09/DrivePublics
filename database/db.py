##
#Drives públicos
# Autor : Vanessa Ayala Salas
#Descripción: Clase encargada de definir la base de datos en SQLlite haciendo uso de sqlalchemy
# 
#Cambios (Versión)
#-------------------------------------
#No.           Fecha            Autor                    Descripción
# -----        ----------       --------------------     ---------------
# 1.0          14/11/2022       Vanessa Ayala Salas      Creación de la clase.
##

# Se importan las librerías necesarias para la definición de la base de datos y la estructura de la tabla.

from sqlalchemy import create_engine
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engineDatabase = create_engine('sqlite:///driveFiles.db') #database

#Sacar la configuración a los archivos

modeldatabase = declarative_base()

# Se crea la clase que va a gestionar la tabla y su estructura

class Infofiles(modeldatabase): 
    __tablename__ = 'metadatosFile' 

    id = Column(Integer, primary_key=True)
    id_file = Column(String)
    name_file = Column(String)
    extension = Column(String)
    owner = Column(String)
    visibility= Column(String)
    modifi_date = Column(String)
    was_public = Column(String)

    def __init__(self, id, id_file, name_file, extension, owner, visibility, modifi_date, was_public):
        # encapsular parámetros en objetos o buiders
        self.id = id
        self.id_file = id_file
        self.name_file = name_file
        self.extension = extension
        self.owner = owner
        self.visibility = visibility
        self.modifi_date = modifi_date
        self.was_public = was_public

modeldatabase.metadata.create_all(engineDatabase)


