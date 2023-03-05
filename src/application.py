import os
import openai
from flask import Flask, request, render_template
from dotenv import load_dotenv
from flask_mysqldb import MySQL



os.chdir(os.path.dirname(__file__))

# Traernos la API_KEY
load_dotenv()
openai.api_key = os.getenv("ACCESS_KEY")

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.getenv("HOST_DB")
app.config['MYSQL_USER'] = os.getenv("USERNAME_DB")
app.config['MYSQL_PASSWORD'] = os.getenv("PASSWORD_DB")
app.config['MYSQL_DB'] = 'prompt_database'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# Definir la ruta de la página principal
@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        # Obtener la entrada del usuario desde el formulario
        user_input = request.form['input']

        # Enviar la entrada del usuario a OpenAI API
        response = openai.Completion.create(
            prompt=user_input,
            model="text-davinci-003",
            max_tokens=1000,
            temperature=0.8,
        )
        output = response.choices[0].text

        #Conexión DB
        cursor = mysql.connection.cursor()

        # Seleccionar DB
        use_db = ''' USE prompt_database'''
        cursor.execute(use_db)

        # Guardar pregunta y respuesta en la base de datos
        cursor.execute('''INSERT INTO prompt (question, answer)
                        VALUES (%s, %s)''',
                    (user_input, output))
        mysql.connection.commit()
        cursor.close()
                
        # Renderizar la plantilla del formulario con la respuesta de GPT-3
        return render_template('index.html', output=output)
    else:
        # Renderizar la plantilla del formulario
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)