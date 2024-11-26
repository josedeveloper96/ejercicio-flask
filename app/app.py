from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():

    cursos = ['PHP', 'Python', 'Java', 'Kotlin', 'Javascript']
    data = {
        'titulo': 'index123',
        'bienvenido':'saludos',
        'cursos':cursos,
        'numero_cursos':len(cursos)
    }
    return render_template ('index.html', data=data)

@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre,edad):
    data={
        'titulo':'Contacto',
        'nombre':nombre,
        'edad':edad
    }
    return render_template('contacto.html',data=data)
if __name__ == "__main__":
    app.run(debug=True, port=5000)