from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return '<h1>Página Principal del Proyecto</h1><p>¡Bienvenidos al proyecto colaborativo!</p>'

# --- DEJA ESTE ESPACIO PARA TUS COMPAÑEROS ---


# --- FIN DEL ESPACIO ---

@app.route('/info')
def informacion():
    return '<h1>Información del Proyecto</h1><p>Este es un proyecto para practicar el flujo de Git.</p><p>Aquí aprenderás a usar ramas, commits y push.</p>'


if __name__ == '__main__':
    app.run(debug=True)
