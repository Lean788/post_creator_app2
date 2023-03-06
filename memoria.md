# Memoria
#### _Explicación detallada de los pasos que hemos seguido, como se ha construido y las particularidades del trabajo_


## Introducción

La productivización es uno de los aspectos clave en cualquier ámbito profesional, y en el Bootcamp de Data Science se ha identificado como una oportunidad para aplicar la tecnología y mejorar los procesos en la generación de contenido. Es por ello que se ha planteado el desarrollo de una **aplicación web** en Python que utilice la tecnología de GPT3 para generar automáticamente post en base a preguntas específicas.
El objetivo principal de este proyecto es crear una herramienta capaz de generar respuestas precisas y coherentes en cuestión de segundos, evitando así la necesidad de dedicar tiempo y esfuerzo a la creación manual de contenido. Para ello, se ha seleccionado el modelo preentrenado de ChatGPT, una herramienta avanzada de generación de lenguaje natural que utiliza técnicas de aprendizaje profundo para generar textos de alta calidad.

Para lograr este objetivo, se ha propuesto desarrollar una aplicación web en **Python** con **Flask** que permita al usuario realizar preguntas específicas y obtener respuestas automáticas generadas por ChatGPT. La interfaz de usuario será sencilla y fácil de usar, permitiendo una interacción fluida y eficiente con la herramienta.

Además, se ha previsto la necesidad de almacenar todas las preguntas y respuestas generadas, así como las fechas correspondientes, en una base de datos alojada en la nube de **Amazon Web Services (AWS)**. Esto permitirá un acceso fácil y seguro a los datos, y la posibilidad de realizar análisis posteriores sobre los mismos.

Finalmente, se ha establecido como objetivo el despliegue de la aplicación en **Docker**, una plataforma de virtualización que permite la creación y ejecución de aplicaciones en contenedores independientes y escalables.

Con este planteamiento inicial, se ha comenzado a trabajar en el desarrollo de la aplicación, siguiendo un enfoque metodológico basado en el ciclo de vida de software. Se ha trabajado en el diseño de la arquitectura, la selección de las herramientas y tecnologías necesarias, la implementación de las funcionalidades principales, la integración con la API de GPT3 y la base de datos en la nube, y finalmente *el despliegue en Docker*. Todo ello, con el objetivo de ofrecer una herramienta completa, funcional y eficiente para la generación automática de post.

## Árbol de directorios

Para continuar con el desarrollo de la aplicación en Flask, es importante tener en cuenta el árbol de directorios proporcionado.  

```
├── post_creator_app2/                                                   
├── src/
│   ├── static/                                     
│   │     └── css/ style.css  
│   ├── img/ image.png               
│   ├── templates/                                   
│   │     ├── 404.html
│   │     ├── index.html   
│   │     └── layout.html  
│   ├── .env.example  
│   ├── requeriments.txt                                                   
│   └── application.py  
├── .env                                          
├── .gitignore   
├── .python-version                                          
├── Dockerfile
├── memoria.md                                    
└── README.md 
```

- post_creator_app2/: es el directorio raíz de la aplicación.
- src/: es el directorio donde se encuentra el código fuente de la aplicación.
- src/static/css/style.css: archivo que contiene los estilos CSS utilizados por la aplicación.
- src/img/image.png: archivo de imagen utilizado por la aplicación.
- src/templates/404.html: archivo HTML de la página de error 404.
- src/templates/index.html: archivo HTML de la página principal de la aplicación.
- src/templates/layout.html: archivo HTML que define la estructura básica de las páginas de la aplicación.
- src/.env.example: archivo que muestra un ejemplo de cómo configurar las variables de entorno necesarias para la aplicación.
- src/requeriments.txt: archivo que especifica las dependencias necesarias para la aplicación.
- src/application.py: archivo que contiene el código principal de la aplicación Flask.
- .env: archivo que contiene las variables de entorno necesarias para el entorno de desarrollo.
- .gitignore: archivo que especifica los archivos y directorios que deben ser ignorados por Git.
- .python-version: archivo que especifica la versión de Python utilizada por la aplicación.
- Dockerfile: archivo que especifica las instrucciones necesarias para construir la imagen de Docker de la aplicación.
- memoria.md: archivo donde se debe escribir la memoria del proyecto.
- README.md: archivo que contiene información básica sobre la aplicación y cómo ejecutarla.

## Desarrollando la aplicación

Este proyecto se realizó con **Python 3.9.4**, usando **pyenv** y **virtualenv**. 

Se ha optado por esta versión de Python, ya que lo requería una de las dependencias que necesitabamos para nuestro desarrollo. 

En este sentido, hemos tenido varios **problemas** para poner en común los entornos de desarrollo de cada uno de los contribuidores, por lo que optamos por trabajar con un entorno en el que se ejecute con el interprete adecuado, e instalando las dependencias necesarias para la aplicación. 

### application.py

En este caso, la aplicación se encuentra en el archivo "application.py", que se ubica dentro de la carpeta "src". 

En este archivo, es necesario definir las rutas y las funcionalidades que tendrá la aplicación. 

Para definir las rutas, se puede utilizar la función `route()` de **Flask**, que permite asociar una URL a una función específica que se encargará de procesar la petición y generar la respuesta correspondiente.
En nuestro caso, definimos la ruta principal de esta manera:
`@app.route('/', methods=['GET', 'POST'])`
decorador, que irá acompañado de la función que la define:
`def index():`

En la aplicación, cabe destacar los siguientes puntos:

•	Importamos las dependencias necesarias. 

•	`os.chdir(os.path.dirname(__file__))`: establece el directorio de trabajo actual de la aplicación al directorio del archivo actual.

•	`openai.api_key = os.getenv("ACCESS_KEY")`: establece la clave de API de OpenAI a la variable de entorno "ACCESS_KEY" utilizando la función getenv() del módulo os.

•	app = Flask(__name__): crea una instancia de la clase Flask y la almacena en la variable app.

•	Con `app.config['…'] = os.getenv("…")`: establece la información pertinente de la base de datos MySQL a la variable de entorno que corresponde.

•	`app.config['MYSQL_CURSORCLASS'] = 'DictCursor'`: configura el cursor MySQL para que devuelva los resultados como un diccionario en lugar de una tupla.

•	`mysql = MySQL(app)`: crea una instancia de la clase MySQL y la almacena en la variable mysql.

•	Definimos la ruta de la página principal y los métodos HTTP que se admiten (en este caso, GET y POST).

•	Dentro ya de la función, creamos un condicional que verifica si el método HTTP utilizado es POST (lo que indica que el usuario ha enviado un formulario), si es True, obtiene la entrada del usuario desde el formulario.

•	Se guarda el dato en una variable y luego se crea la respuesta a esta pregunta, enviándole dicha variable como input, así: 

`response = openai.Completion.create(prompt=user_input, model="text-davinci-003", max_tokens=1000, temperature=0.8)`

cabe destacar que la entrada del usuario a la API de OpenAI generará una respuesta utilizando el modelo de lenguaje natural **"text-davinci-003"**. 

A continuación, esta respuesta se guardará también en una variable llamada `output` (se escoge la primera respuesta de la paleta de respuestas que genera el modelo, y se guarda en dicha variable),que junto a la consulta inicial, serán pasadas a la base de datos que la registrará. Usará como ID la fecha y hora de dicha consulta.


Finalmente se Renderiza la plantilla index.html con la respuesta generada por OpenAI.

Si la solicitud HTTP es una solicitud GET, la función index simplemente renderiza la plantilla index.html.

Por último, el bloque `if __name__ == '__main__':` verifica si el archivo Python está siendo ejecutado directamente como un script, en lugar de ser importado como un módulo. Si se está ejecutando como un script, la aplicación **Flask** se inicia en modo de depuración y se ejecuta en el host 0.0.0.0.

### Frontend

El frontend de la aplicación ha sido desarrollado en **Flask** utilizando plantillas de **Jinja**. Se han creado tres archivos HTML para el layout, la página principal y la página de error 404, respectivamente: layout.html, index.html y 404.html.

El archivo layout.html define la estructura base de las páginas, incluyendo la declaración del título, la codificación y la hoja de estilo CSS.

El archivo index.html extiende del layout y define la página principal, con un formulario para realizar una pregunta y un contenedor para mostrar la respuesta generada por la aplicación.

El archivo 404.html también extiende del layout y muestra un mensaje de error cuando el usuario intenta acceder a una página que no existe en la aplicación.

### Docker

El despliegue de la aplicación en **Docker** es una tarea importante para asegurar su portabilidad y escalabilidad. A continuación, se detallan los pasos que hemos seguido para para desplegar la aplicación:

**1.	Construir la imagen de Docker**: para ello, se debe crear un archivo "Dockerfile" en la raíz del proyecto, que especifique la imagen base de Docker a utilizar y las dependencias necesarias para la aplicación. A continuación, se debe ejecutar el siguiente comando en la terminal:

`docker build -t post_creator .`

Donde "post_creator" es el nombre que se le quiere dar a la imagen de Docker. El punto al final indica que se debe utilizar el Dockerfile en la carpeta actual.

**2.	Crear un contenedor de Docker a partir de la imagen**: una vez que se ha construido la imagen de Docker, se debe crear un contenedor que la ejecute. 

El comando Docker que se utiliza para ejecutar el contenedor de la aplicación Flask incluye variables de entorno que deben ser reemplazadas con las credenciales correspondientes de cada usuario. Estas variables son:

- ACCESS_KEY: Es la clave de acceso de la aplicación que se utiliza para la autenticación. Cada usuario debe reemplazar este valor con su propia clave de acceso.

- USERNAME_DB: Es el nombre de usuario de la base de datos utilizada por la aplicación. Cada usuario debe reemplazar este valor con su propio nombre de usuario.

- PASSWORD_DB: Es la contraseña de la base de datos utilizada por la aplicación. Cada usuario debe reemplazar este valor con su propia contraseña.

 - HOST_DB: Es la dirección del host de la base de datos utilizada por la aplicación. Cada usuario debe reemplazar este valor con la dirección de host correspondiente.



A continuación se muestra un ejemplo del comando Docker con las variables de entorno reemplazadas por los valores correspondientes:

```docker run -d -t --name container_post_creator -p 5000:5000 -e "ACCESS_KEY=my_access_key" -e "USERNAME_DB=my_username" -e "PASSWORD_DB=my_password" -e "HOST_DB=mi_host" post_creator```



**3.	Verificar el funcionamiento de la aplicación**: para verificar que la aplicación se ha desplegado correctamente en Docker, hemos accedido a "http://localhost:5000" desde el navegador. hemos comprobado con una pregunta de prueba y hemos comprobado que la aplicación funciona perfectamente, así como también su registro en la base de datos.


