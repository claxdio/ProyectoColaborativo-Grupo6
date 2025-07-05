from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return '<h1>Página Principal del Proyecto</h1><p>¡Bienvenidos al proyecto colaborativo!</p>'

# --- DEJA ESTE ESPACIO PARA TUS COMPAÑEROS ---


# --- FIN DEL ESPACIO ---

if __name__ == '__main__':
    app.run(debug=True)
