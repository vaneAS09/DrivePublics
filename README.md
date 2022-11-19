Aplicación para inventariar en una Base de Datos todos los archivos pertenecientes a la unidad de Drive de un usuario.

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

