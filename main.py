# Importar

from flask import Flask, render_template, request, redirect, jsonify

# Conectando a la biblioteca de bases de datos

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# Conectando SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Creando una base de datos
db = SQLAlchemy(app)
# Creación de una tabla


class Card(db.Model):
    # Creación de columnas
    # id
    id = db.Column(db.Integer, primary_key=True)
    # Título
    title = db.Column(db.String(100), nullable=False)
    # Descripción
    subtitle = db.Column(db.String(300), nullable=False)
    # Texto
    text = db.Column(db.Text, nullable=False)

    # Salida del objeto y del id
    def __repr__(self):
        return f'<Card {self.id}>'


# Asignación #2. Crear la tabla Usuario
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(30), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def login():
    error = ''
    if request.method == 'POST':
        form_login = request.form['email']
        form_password = request.form['password']
        users_db = User.query.all()
        for user in users_db:
            if form_login == user.login and form_password == user.password:
                return redirect('/index')
        error = 'Nombre de usuario o contraseña incorrectos'
        return render_template('login.html', error=error)
    else:
        return render_template('login.html')


@app.route('/reg', methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        login = request.form['email']
        password = request.form['password']
        # Asignación #3.
        # Hacer que los datos del usuario se registren en la base de datos.
        user = User(login=login, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('registration.html')


# Ejecutar la página de contenidos
@app.route('/index')
def index():
    # Visualización de las entradas de la base de datos
    return render_template('index.html')


# Ejecutar la página con la entrada
@app.route('/card/<int:id>')
def card(id):
    card = Card.query.get(id)
    return render_template('card.html', card=card)


# El formulario de inscripción
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title = request.form['title']
        subtitle = request.form['subtitle']
        text = request.form['text']


# Creación de un objeto que se enviará a la base de datos
        card = Card(title=title, subtitle=subtitle, text=text)
        db.session.add(card)
        db.session.commit()
        return redirect('/index')
    else:
        return render_template('create_card.html')


@app.route('/articulo')
def articulo():
    return render_template('articulo.html')


@app.route('/articulo_info')
def articulo_info():
    return render_template('articulo_info.html')


@app.route('/login')
def log():
    return render_template('login.html')

@app.route('/menu_juego')
def menu_juego():
    return render_template('menu_juego.html')

# Segunda página
@app.route('/articulo')
def articles():
    return render_template(
                            'articulo.html'
                           )
# Tercera página
@app.route('/juegos')
def games():
    return render_template(
                            'tarjetas.html'
                           )
# Tercera página
@app.route('/tarjetas')
def tarj():

    return render_template(
                            'tarjetas.html'
                           )




@app.route('/registro-cambio', methods=['POST'])
def registro_cambio():
    data = request.get_json()
    cambiado = data.get('cambiado')
    print(f"Imagen cambiada: {cambiado}")  # Puedes guardar esto en una base de datos si quieres
    return jsonify({"status": "ok", "cambiado": cambiado})

 #- cuestionario 1
def result_calculate(pregunta_agua1, pregunta_agua2, pregunta_agua3):
    return pregunta_agua1  + pregunta_agua2 + pregunta_agua3 


@app.route('/cuestionario')
def cuestionario_agua():
    return render_template('cuestionario.html')

# Segunda página
@app.route('/<pregunta_agua1>')
def cuestionario_agua1(pregunta_agua1):
    return render_template(
                            'cuestionario1.html', 
                            pregunta_agua1 = pregunta_agua1
                           )
# La tercera página
@app.route('/<pregunta_agua1>/<pregunta_agua2>')
def cuestionario_agua2(pregunta_agua1, pregunta_agua2):
    return render_template(
                            'cuestionario2.html',                           
                            pregunta_agua1 = pregunta_agua1, 
                            pregunta_agua2  = pregunta_agua2                           
                           )






# Cálculo
@app.route('/<pregunta_agua1>/<pregunta_agua2>/<pregunta_agua3>')
def end(pregunta_agua1, pregunta_agua2, pregunta_agua3):
    return render_template('end.html', 
                            result=result_calculate(int(pregunta_agua1),
                                                    int(pregunta_agua2),
                                                    int(pregunta_agua3),
                                                    )
                        )



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    users_db = User.query.all()
