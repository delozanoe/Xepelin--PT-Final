# Xepelin -PT Final
La siguiente es la entrega de la prueba técnica para el puesto de Producto Enginnering para Xepelin. 
[Resultado final](https://62eaae2bb1e2ed059df9006e--lustrous-gingersnap-9fde1f.netlify.app)

Contando de 2 partes: La primera 2 problemas de razonamientos logicos que fueron desarollados en python. La segunda, siendo un portal we donde debia tener un login básico y una lista con ids de tasa que permitia editarlas y posteriormente se hacia el llamado a un API que envia un correo al usuario.

## Problemas logicos
Desarrollado en python: los 2 cuentan se pueden correr independientes y con ingresar los datos requeridos por consola (y que seran solicitados) basta, para ver si correcto funcionamiento.

## Desarrollo del caso
### Manejo de GSheet
El sheet de google utilizado es el siguiente: [Gheet Utilizada](https://docs.google.com/spreadsheets/d/10KYwKdS3RPsnrUhuI3kb_gruvj5gYFYrINdDHwdxe8c/edit?usp=sharing), ésta última es una copia exacta de la que me fue suministrada en la descripcion del problema. 

Para hacer la lectura y modificación de los datos en ésta, se crearon scripts utilizando la herramienta Apps Scrips, la cual es suministrada por el mismo Google. Esta herramienta, permite hacer el manejo de GSheet y crear endpoints que correrán scripts desarrollados en .gs (lenjuaje especifico de la herramienta), esto con el fin de ser consumido por el Front-End. Es por eso que se implementan 2 servicios en específico; uno, para obtener todos los datos del Gsheet y otro para modificar una tasa con un id especifico (suministrados en los parámetros Query).

### LLamado al Hook
Para el llamado al hook que enviará el correo (este fue suministrado por el equipo de Xepelin), fue necesario crear un pequeño API Rest (utilizando la librería de pyhton FastAPI), esto pues no se podría hacer directamente el llamado por problemas de CORS. Para poder solucionarlo, es necesario modificar el servicio desde el servidor que lo expone o hacer el llamado desde un lenguaje server-side, al no tener acceso al primero y sin poder hacer el llamado desde el Front-End, se crea el API. Desarrollado en Python y desplegado utilizando Heroku, obteniendo el siguiente endpoint: [API Heroku](https://xepelin-backpt.herokuapp.com) y con el servicio para hacer el llamado del WS (con el siguiente ejemplo):
                [WS Ejemplo](https://xepelin-backpt.herokuapp.com/send-email/?idOp=101&tasa=1,8&email=daniellozano.ee@gmail.com)

### Creacion del Front-End
Para la creación del Front-End de la aplicación web, se hace un desarrollo con la librería Ract.JS en donde se crean 2 paginas como componentes, una de login y otra para el manejo del GSheet.

Para el login, se desarrolló un login sencillo, verificando que el usuario y la contraseña coincidan con las de la siguiente base de datos.


| Username        | Password    |
| ------------- |:-------------:|
| user1      | pass1 |
| user2      | pass2      |
| daniellozano.ee@gmail.com | daniellozano      |
| ianiv@xepelin.com      | xepelin      |
| admin@xepelin.com      | admin      |


Una vez ingrese al portal, se empezará a cargar los datos de las GSheet, se realiza por medio de fetch llamando al API de Apps Script, desarrollado anteriormente. Al terminar el llamado, los datos, se observarán en una tabla donde se podrá modificar las tasas. En cada línea se mostrará, el id y el correo al cual en caso de modificar la tasa se enviará el mail. Una vez modificada la casilla de la tasa, se deshabilitarán las casillas de edición mientras se envía el correo (por medio de fetch al API desarrollado y desplegado en Heroku), proceso el cual normalmente toma 2 segundos, esto para no generar confusiones y mitigar errores. 


Finalmente, se deja la posibilidad de cerrar la sesión, con un botón a la derecha del logo de Xapier. 


Si se desea conocer los repositorios de los códigos desarrollados anteriormente, se puede encontrar en los siguientes links.


[Back-End](https://github.com/delozanoe/xepelin-back/)
[Front-End](https://github.com/delozanoe/Xepelin-PE-Test)
