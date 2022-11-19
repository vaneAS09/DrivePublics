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
5- Actualización de cambios en los metadatos como nombre y fecha de modificación,
6- Privatización de archivos publicos.
7- Actualización de historial en la base de datos si un archivo fue público.
