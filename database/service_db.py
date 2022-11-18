##
#Drives públicos
#Autor : Vanessa Ayala Salas
#Descripción: Se crea la clase que contiene los servicios de creación y modificación de registros en la base de datos.

##

import database.db as db
from database.db import Infofiles
from sqlalchemy.orm import Session



class service_db:

# se crea un método para buscar los archivos ya existentes en la base de datos y guardar los nuevos, además de la actualización de cambios en los archivos.
    def create_data(id,title,file_extension,name_owner,shared,modified_date):
        session = Session(db.engineDatabase)

        databd = session.query(Infofiles).filter(
            Infofiles.id_file == id
        ).first()
     
        if databd: 
            changedate = session.query(Infofiles).filter(
                Infofiles.id_file == id 
            ).first()  
            if (Infofiles.modifi_date != modified_date):
                changedate.modifi_date = str(modified_date)
            if (Infofiles.name_file != title):
                changedate.name_file = title
           
            session.add(changedate)
            session.commit()

        else: 
            insert = Infofiles(id = None, id_file = id, name_file = title, 
                extension = file_extension, owner = name_owner, 
                visibility= shared, modifi_date = modified_date, was_public = 'false')

            session.add(insert)
            session.commit()
            session.close()

# Se Crea un método para actualizar en la base de datos el campo "was_public" y actualizar visibilidad.

    def save_history(id):
        session = Session(db.engineDatabase)

        history = session.query(Infofiles).filter(
                        Infofiles.id_file == id
                    ).first()  
        history.was_public = "true"  
        history.visibility = "0"  
        session.add(history)
        session.commit()
