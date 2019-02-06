# coding=UTF-8
from flask import *
from db import *
from forms import *


# instancia o app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'teste'

# inicia o site e se não existir usuario logado, envia para a página de login
@app.route('/')
def home():

    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return redirect(url_for('index'))

# app para logar no site caso exista um usuario cadastrado no BD
@app.route('/login', methods=['GET', 'POST'])
def login():

    if not session.get('logged_in'):

        validador = check_usuario(
            request.form['usuario'], request.form['senha'])

        if validador != [] and validador != None and validador != Exception:
            session['logged_in'] = True
        else:
            flash('Login ou senha errada, tente novamente')

    return home()

# Desloga um usuário caso o mesmo realize tal solicitação
@app.route('/logout')
def logout():

    session['logged_in'] = False
    return home()

# App que mostra a page de login da administração
@app.route('/loginadmin', methods=['GET', 'POST'])
def loginadmin():

    if not session.get('logged_in_admin'):

        validador = check_admin(request.form['usuario'], request.form['senha'])

        if validador != [] and validador != None and validador != Exception:
            session['logged_in_admin'] = True
        else:
            flash('Login ou senha errada, tente novamente')

    return homeadmin()

# App para caso o usuário não esteja logado como admin, redireciona o mesmo para a page de loginadmin
@app.route('/homeadmin', methods=['GET', 'POST'])
def homeadmin():

    if not session.get('logged_in_admin'):
        return render_template('loginadmin.html')
    else:
        return redirect(url_for('admin'))

# page que cria usuários para utilizar o site
@app.route('/admin', methods=['GET', 'POST'])
def admin():

    if not session.get('logged_in_admin'):
        return render_template('loginadmin.html')
    else:

        formulario3 = FormularioCriacao(request.form)
        formulario4 = FormularioDeletar(request.form)

        if request.method == 'POST' and formulario3.validate_on_submit:

            cadastro_usuario(request.form['nomeusuario'],
                            request.form['senhausuario'])
            return redirect(url_for('admin'))

        listausuario = read_usuario()
        ini = 0
        fim = len(listausuario)
        return render_template('admin.html', formulario3=formulario3, formulario4=formulario4, listausuario=listausuario, ini=ini, fim=fim)

# Desloga usuário e admin caso o mesmo solicite a opção de configuração e envia para homeadmin
@app.route('/logoutadmin')
def logoutadmin():

    session['logged_in'] = False
    session['logged_in_admin'] = False
    return homeadmin()

# App que para ir ao index da página
@app.route('/index', methods=['GET', 'POST'])
def index():

    if session['logged_in'] == False or session['logged_in_admin'] == True and session['logged_in'] == True:
        session['logged_in_admin'] = False
        session['logged_in'] = False
        return home()
    else:
        # requisita o formulario do arquivo forms.py
        formulario = FormularioDeCadastro(request.form)
        formulario2 = FormularioDeExclusao(request.form)

        # se obtiver "POST" e validate_on_submit realiza o cadastro das informações no BD e devolve o template de resultado
        # se não, devolve o template index
        if request.method == 'POST' and formulario.validate_on_submit():

            insert_ent(request.form['placa'],
                       request.form['data'], request.form['hora'])
            return redirect(url_for('index'))

        # função que recebe os dados cadastrados no BD e mostra no template index
        lista = read_ent()
        ini = 0
        fim = len(lista)

        lista2 = read_sd()
        ini2 = 0
        fim2 = len(lista2)

        return render_template('index.html', lista=lista, ini=ini, fim=fim, formulario=formulario, lista2=lista2, ini2=ini2, fim2=fim2, formulario2=formulario2)

# App que deleta os cadastros no BD
@app.route('/delete', methods=['GET', 'POST'])
def delete():

    placa = None
    formulario2 = FormularioDeExclusao(request.form)

    if request.method == 'POST' and formulario2.validate_on_submit():

        placa = request.form['pkcodentr']
        insert_sd(request.form['placacarsd'], request.form['dataentrsd'],
                  request.form['horaentrsd'], request.form['datasd'], request.form['horasd'])

    delete_ent(placa)
    return redirect(url_for('index'))

# App que deleta usuarios da tbusuarios
@app.route('/deleteusuario', methods=['GET', 'POST'])
def deleteusuario():

    usuario = None

    formulario4 = FormularioDeletar(request.form)

    if request.method == 'POST' and formulario4.validate_on_submit():
        usuario = request.form['pkcodusuario']
        
    delete_usuario(usuario)
    return redirect(url_for('homeadmin'))

# inicia o servidor
if __name__ == "__main__":
    app.run()
