import pytest

from mail.mail_service import mail_service
from database.service_db import service_db
from DrivePublics import search

# Probando método para el envío de correo

def test_mail():
    receiver = "valus14@gmail.com"
    assert mail_service.send_mail(receiver) 

def test_mail():
    receiver = "valus14@gmail"
    assert mail_service.send_mail(receiver) 

# Probando método para la creación de un registro de metadatos.
def test_create_data(): 
    id_file = "yy772828299034bnfld",
    title = "La hojarasca GCM.pdf"
    file_extension = "pdf"
    name_owner = "Vanessa Ayala"
    shared = 0
    modified_date = "22-11-18"
    assert service_db.create_data(id_file,title,file_extension,name_owner,shared,modified_date)

def test_create_data(): 
    id_file = "yy772828299034bnfld",
    title = "La hojarasca GCM - Libro.pdf"
    file_extension = "pdf"
    name_owner = "Vanessa Ayala"
    shared = 1
    modified_date = " "
    assert service_db.create_data(id_file,title,file_extension,name_owner,shared,modified_date)

# Probando método para la actualización del historial "was_public"

def test_history():
    id="1oqSWFLNlP_UmyWgKZDyJ9iknykG3U1o9"
    assert service_db.save_history(id)

def test_history():
    id="1oqSWFLNlP"
    assert service_db.save_history(id)

# Probando método para la actualización del historial "was_public"
def test_search():
    id_file = "1YVGtyZa2_G6oIE1MRxK7HtHbgcmyn2LH"
    assert search(id_file)

def test_search():
    id_file = " "
    assert search(id_file)

