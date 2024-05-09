from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, current_user, logout_user, UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import json
from wtforms.fields import RadioField


app = Flask(__name__)
app.config['SECRET_KEY'] = '90bc04947dce3a57edbd90fefbc1c3d0211739937a6fc5ed'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

#Cargamos los archivos json
data_usuarios = '/Datos/data_usuarios.json'
data_usuarios_administrador = '/Datos/data_usuarios_administrador.json'
data_usuarios_manager = '/Datos/data_usuarios_manager.json'
data_usuarios_worker = '/Datos/data_usuarios_worker.json'
data_proyecto = '/Datos/data_proyecto.json'
data_tarea = '/Datos/data_tarea.json'


# Configuraciones para desactivar la caché en desarrollo
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    role = SelectField('Role', choices=[('administrador', 'Administrador'), ('manager', 'Manager'), ('worker', 'Worker')], validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already taken. Please choose a different one.')
        
class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)# 'manager' or 'worker' or 'administrador'
    
    def __init__(self, username, role):
        self.username = username
        self.role = role
        
    
    def __repr__(self) -> str:
        return f"<User {self.username}>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

login_manager = LoginManager(app)
login_manager.login_view = 'inicio'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/index', methods=['GET', 'POST'])
def login():
    db.create_all()
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Has iniciado sesión correctamente.', 'success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('index'))
        else:
            flash('Usuario o contraseña inválidos.', 'danger')
    return render_template('index.html', form=form)


@app.route('/cerrar-sesion')
def logout():
    logout_user()
    flash('Has cerrado sesión correctamente.', 'info')
    return redirect(url_for('index'))

@app.route('/menu_worker')
def menu_worker():
    if current_user.is_authenticated and current_user.role == 'worker':
        return 'Página de inicio para usuarios worker'
    else:
        flash('Debe iniciar sesión como usuario worker para acceder a esta página.', 'warning')
        return redirect(url_for('index'))

@app.route('/menu_manager')
def menu_manager():
    if current_user.is_authenticated and current_user.role == 'manager':
        return 'Página de inicio para usuarios manager'
    else:
        flash('Debe iniciar sesión como usuario manger para acceder a esta página.', 'warning')
        return redirect(url_for('index'))

@app.route('/menu_admin')
def menu_administrador():
    if current_user.is_authenticated and current_user.role == 'administrador':
        return 'Página de inicio para usuarios administrador'
    else:
        flash('Debe iniciar sesión como usuario administrador para acceder a esta página.', 'warning')
        return redirect(url_for('index'))

@app.route('/create_admin_manager', methods= ['GET', 'POST'])
def create_admin_manager():
    if request.method == 'GET':
        return render_template('create_admin_manager.html', administrador={} , manager={})
    if request.method == 'POST':
        
        administrador={}
        if administrador.count() == 0:
            numero_admin = 1
            id_administrador = "UA" + str(numero_admin)
        else:
            numero_admin = administrador.count() +1
            id_administrador = "UA" + str(numero_admin)
        nombre_administrador = request.form["nombre"]
        apellido_1_administrador = request.form["apellido_1"]
        apellido_2_administrador = request.form["apellido_2"]
        telefono_administrador = request.form["telefono"]
        email_administrador = request.form["email"]
        horas_semanales_administrador = request.form["horas_semanales"]
        coste_hora_administrador = request.form["coste_hora"]
        puesto_trabajo_administrador = request.form["puesto_trabajo"]
        with open(data_usuarios_administrador, 'r+') as ua:
            administrador = json.load(ua)
        administrador.append({"id_administrador": id_administrador, "nombre_administrador": nombre_administrador, "apellido_1_administrador": apellido_1_administrador,
                              "apellido_2_administrador": apellido_2_administrador, "telefono_administrador": telefono_administrador, "email_administrador": email_administrador,
                              "horas_semanales_administrador": horas_semanales_administrador, "coste_hora_administrador": coste_hora_administrador,
                              "puesto_trabajo_administrador": puesto_trabajo_administrador, "contador_tareas_administrador": 0, "contador_proyectos_administrador": 0})
        with open(data_usuarios_administrador,"w") as ua:
            json.dump(administrador,ua)
        return redirect(url_for('menu_admin'))

        manager = {}
        if manager.count() == 0:
            numero_manager = 1
            id_manager = "UM" + str(numero_admin)
        else:
            numero_manager = manager.count() +1
            id_manager = "UA" + str(numero_admin)
        nombre_manager = request.form["nombre"]
        apellido_1_manager = request.form["apellido_1"]
        apellido_2_manager = request.form["apellido_2"]
        telefono_manager = request.form["telefono"]
        email_manager = request.form["email"]
        horas_semanales_manager = request.form["horas_semanales"]
        coste_hora_manager = request.form["coste_hora"]
        puesto_trabajo_manager = request.form["puesto_trabajo"]
        with open(data_usuarios_manager, 'r+') as um:
            manager = json.load(um)
        manager.append({"id_manager": id_manager, "nombre_manager": nombre_manager, "apellido_1_manager": apellido_1_manager,
                              "apellido_2_manger": apellido_2_manger, "telefono_manager": telefono_manager, "email_manager": email_manager,
                              "horas_semanales_manager": horas_semanales_manager, "coste_hora_manager": coste_hora_manger,
                              "puesto_trabajo_manager": puesto_trabajo_manager, "contador_tareas_manager": 0, "contador_proyectos_manager": 0})
        with open(data_usuarios_manager,"w") as um:
            json.dump(manager,um)
        return redirect(url_for('menu_admin'))
        nombre_usuario = request.form["nombre_usuario"]
        contrasena_usuario = request.form["contrasena"]
        tipo_usuario = "manager"
      


@app.route('/create_worker', methods= ['GET', 'POST'])
def create_worker():
    if request.method == 'GET':
        return render_template('create_worker.html', worker={})
    if request.method == 'POST':
        worker = {}
        if worker.count() == 0:
            numero_worker = 1
            id_worker = "UW" + str(numero_worker)
        else:
            numero_worker = worker.count() +1
            id_worker = "UW" + str(numero_worker)
        nombre_worker = request.form["nombre"]
        apellido_1_worker = request.form["apellido_1"]
        apellido_2_worker = request.form["apellido_2"]
        telefono_worker= request.form["telefono"]
        email_worker = request.form["email"]
        horas_semanales_worker = request.form["horas_semanales"]
        coste_hora_worker = request.form["coste_hora"]
        puesto_trabajo_worker = request.form["puesto_trabajo"]
        with open(data_usuarios_worker, 'r+') as uw:
            worker = json.load(uw)
        worker.append({"id_worker": id_worker, "nombre_worker": nombre_worker, "apellido_1_worker": apellido_1_worker,
                              "apellido_2_worker": apellido_2_worker, "telefono_worker": telefono_worker, "email_worker": email_worker,
                              "horas_semanales_worker": horas_semanales_worker, "coste_hora_worker": coste_hora_worker,
                              "puesto_trabajo_worker": puesto_trabajo_worker, "contador_tareas_worker": 0, "contador_proyectos_worker": 0})
        with open(data_usuarios_worker,"w") as uw:
            json.dump(worker,uw)
        return redirect(url_for('menu_manager_empleados'))



if __name__ == '__main__':
    app.run(debug=True)