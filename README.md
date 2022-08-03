# Xepelin -PT Final
El siguiente es la entraga de la prueba tecnica para el puesto de Producto Enginnering para Xepelin. 
[Resultado final](https://62eaae2bb1e2ed059df9006e--lustrous-gingersnap-9fde1f.netlify.app)

Contando de 2 partes, la primera 2 problemas de razonamientos logicos que fueron desarollados en python. La segunda, siendo un portal we donde debia tener un login basico y una lista con ids de tasa que permitia editiarlas y posteriormente se hacia el llamado a un API que envia un correo al usuario.

## Problemas logicos
Desarrollado en python, los 2 cuentan se pueden correr independientes y con ingresar los datos requeridos por consola (y que seran solicitados) basta, para ver si correcto funcionamiento.

## Desarrollo del caso
### Manejo de GSheet
El sheet de google utilizado es el siguiente: [Gheet Utilizada](https://docs.google.com/spreadsheets/d/10KYwKdS3RPsnrUhuI3kb_gruvj5gYFYrINdDHwdxe8c/edit?usp=sharing) , esta ultima es una copa exacta de la que se me fue suministrada en la descripcion del problema. 

Para hacer la lectura y moficiacion de los datos en esta, se creacion scripts utilizando la herramenta Apps Scrips, la cual es suminsitrada por el mismo google. Esta herramienta, permite hacer el manejo de GSheet y crear endpoints que correran scripts desarollados en .gs (lenjuaje especifico de la herramienta), esto con el fin de ser consumido por el front end. Es por esto que se implementan 2 servicios en especifico, uno para la obtener todos los datos del gsheet y otro para modificar una tasa con un id espefico (suministrados en los parametros query).

### LLamado al Hook
Para el llamado al hook que enviara el correo (este fue suministrado por el equipo de Xepelin), fue necesario crear un pequeño API Rest (utilizando la libreria de pyhton FastAPI), esto pues no se podria hacer directamente el llamado por problemas de CORS. Para poder solucionar los problemas de CORS, es necesario modificar el servicio desde el servidor que lo expone o hacer el llamdo desde un lenguaje server-side, al no tener acceso al primero y sin poder hacer el llamado desde el front-end, se crea el API. Desarrollado en python y desplegado utilizando heroku, obeteneindo el siguiente endpoint: [API Heroku](https://xepelin-backpt.herokuapp.com) y con el servicio para hacer el llamado del WS (con el siguiente ejemplo):
                [WS Ejemplo](https://xepelin-backpt.herokuapp.com/send-email/?idOp=101&tasa=1,8&email=daniellozano.ee@gmail.com)

### Creacion del Front-End
Para la creacion del Front-End de la aplicacion web, se hace un desarrollo con la liberia Ract.JS en donde se crean 2 paginas como componentes, una de login y otra para el manejo del GSheet.

Para el login, se desarrollo un login sencillo, verificando que el usuario y la contraseña coicidan con las de la siguiente base de datos.


| Username        | Password    |
| ------------- |:-------------:|
| user1      | pass1 |
| user2      | pass2      |
| daniellozano.ee@gmail.com | daniellozano      |
| ianiv@xepelin.com      | xepelin      |
| admin@xepelin.com      | admin      |


Una vez ingrese al portal, se empezara a cargar los datos de las GSheet, una vez cargados (esto por medio de fetch llamando al API de Apps Script, desarollado anteriormente) los datos, se observaran en la una tabla donde se podra modoficar las tasa de casa linea. En cada linea se motrara, el id y el correo al cual en caso de modificar la tasa se enviara el mail. Una vez modificada la casilla de la tasa, se desabilitaran las casillas de edicion mientras se envia el correo (por medio de fetch al API desarroollado y desplegado en Heroku), proceso el cual normalmente toma 2 segundos, esto para no generar confuciones y mitigar errores. 


Finalmente, se deja la posibiliddad de cerrar la sesion, con un boton a la derecha del logo de Xapier. 


Si se desea conoder los repositios de los codigos desarrollados anteriormente, se puede encontrar en los siguientes links.

[Back-End](https://github.com/delozanoe/xepelin-back/)
[Front-End](https://github.com/delozanoe/Xepelin-PE-Test)
