from flask import Flask, render_template, url_for, redirect, request, session
from dao import Usuarios
import os

app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route('/')
def index():
    if 'username' in session:
        lista_usuario = Usuarios().select_todos_usuarios()
        return render_template('index.html', usuarios = lista_usuario, nome_usuario = session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/login')
def login():
    usuario = Usuarios().select_todos_usuarios()
    if usuario != []:
        return render_template('login.html')
    else:
        return redirect(url_for('primeiro_cadastro'))

@app.route('/primeiro_cadastro')
def primeiro_cadastro():
    return render_template('cadastro.html')

@app.route('/primeiro_cadastro', methods = ['POST'])
def fazer_primeiro_cadastro():
    lista_usuario = Usuarios().select_todos_usuarios()
    if lista_usuario == []:
        usuario = request.form['usuario']
        senha = request.form['senha']
        Usuarios(None,usuario, senha).registra_usuario()
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

@app.route('/cadastrar_usuarios', methods = ['POST'])
def cadastra_usuario():
    try:
        usuario = request.form['usuario']
        senha = request.form['senha']
        Usuarios(None,usuario,senha).registra_usuario()
        return redirect(url_for('index'))
    except:
        lista_usuario = Usuarios().select_todos_usuarios()
        return render_template('index.html', usuarios = lista_usuario, nome_usuario = session['username'], msg = 'usuario já existe')

@app.route('/excluir_usuario', methods = ['POST'])
def excluir_usuario():
    id_usuario = request.form['id_usuario']
    Usuarios().exclui_usuario(id_usuario)
    return redirect(url_for('index'))

@app.route('/login', methods = ['POST'])
def fazer_login():
    usuario = request.form['usuario']
    senha = request.form['senha']
    usuario_logado = Usuarios(None,usuario, senha)

    if usuario_logado.valida_login() == True:
        session['username'] = usuario_logado.usuario
        return redirect(url_for('index'))
    else:
        return render_template('login.html', msg = 'login/senha inválidos')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


app.run(debug=True)