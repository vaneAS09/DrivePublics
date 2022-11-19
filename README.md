Aplicación para inventariar en una Base de Datos todos los archivos pertenecientes a la unidad de Drive de un usuario.

PASO # 0 PREPARACIÓN DEL AMBIENTE DE TRABAJO

INSTALACIONES

python.exe -m pip install --upgrade pip      
pip install build-essential libssl-dev libffi-dev python3-dev cargo   
pip3 install setuptools-rust
pyenv install -l    
pip install pydrive --upgrade  
python -m venv venv
pip3 install PyDrive2    
pip install SQLAlchemy        
pip install pytest   

Para acceder a la documentación de Python haga click en el siguiente enlace:

https://wiki.python.org/moin/BeginnersGuide

PASO # 1 AUTENTICACIÓN

Para acceder al Drive de Google, se requiere generar una autenticación, para esto se realiza la creación de un proyecto en Google Cloud que permite agregar un usuario autorizado y una firma de consentimiento para establecer una conexión con el drive.

Para acceder a la documentación por favor haga click en el siguiente enlace: 

https://developers.google.com/drive/api/quickstart/python

PASO # 2 CONEXIÓN AL DRIVE DESDE PYTHON.

Con el fin de poder establecer conexión con los archivos en el Drive de Google, Python hace uso de la librería Pydrive2 que permite gestionar los metadatos de los archivos, realizando transacciones como: obtener metadatos, subir un archivo, cambiar ubicación de un archivo, modificar metadatos, cambiar permisos entre otras.

Para acceder a la documentación por favor haga click en el siguiente enlace: 

https://docs.iterative.ai/PyDrive2/

PASO # 3 GESTIÓN DE BASES DE DATOS.

Para la establecer conexión con una base de datos en la que se pudiese administrar la información de los matadatos de los arhivos en el drive, se hace uso de Sqllite bajo la librería de Sqlalchemy, que permite gestionar transacciones a la base de datos de forma sencilla mediante el modelo de ORM. 

Para acceder a la documentación por favor haga click en el siguiente enlace: 

https://docs.sqlalchemy.org/en/14/orm/queryguide.html

https://www.sqlitetutorial.net/sqlite-python/

PASO # 4 SERVICIO DE ENVÍO AUTOMÁTICO DE CORREO ELECTRÓNICO.

Para el envío de correo automático, para el caso de este proyecto: notificación al correo electrónico informándole al propietario de un archivo que el documento ha cambiado de público a privado, se hace uso de la librería smtplib de python que permite mediante una estructura simple configurar un servidor de envío de correo, permtiendo la generación de un servicio de notificación automática.
En este paso, se hace necesario la importación de un archivo Json con el fin de establecer parámetros de configuración del servidor de envío de correo, y así automatizar el servicio para futuros desarrolladores.

Para acceder a la documentación por favor haga click en el siguiente enlace: 

https://docs.python.org/3/library/smtplib.html

PASO # 5 CONSTRUCCIÓN DEL MAIN

Para la construcción del main se genera la estructura de interacción con el drive, importando los servicios necesarios para su funcionamiento tales como: 

1- Autenticación.

2- Consulta de los metadatos.

3- Creación automática de la base de datos y la tabla de almacenamiento de los metadatos.

4- Creación registros de metadatos por archivos nuevos.

5- Actualización de cambios en los metadatos como nombre y fecha de modificación.

6- Privatización de archivos publicos.

7- Actualización de historial en la base de datos si un archivo fue público.

8- Envío de correo electrónico automático a al propietario de un arhivo cuando cambia la privacidad. 

**** PROPUESTA DE INTERACCIÓN CON LOS METADATOS DEL DRIVE DE UN USUARIO.****

- Para la interacción con los metadatos, se propone búsqueda por id_folder en el drive o por FyleExtension del documento, esto debido a que la utlidad de mapeo de metadatos en el drive reconoce las carpetas como elementos y devuelve la información de la carpeta ignorando los documentos relacionados en ella, esto nos genera una excepción por lo que la funcionalidad de privatización de documentos no estaría cumpliendo al 100% con su propósito.

PASO # 6 PRUEBAS

Para la generación de pruebas unitarias, se hace uso de la herramienta pytest que permite evaluar el buen funcionamiento del código en Python replicando los métodos mediante parámetros para obtener una respuesta.

Para acceder a la documentación por favor haga click en el siguiente enlace: 

https://docs.pytest.org/en/7.2.x/
