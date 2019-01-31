# coding=UTF-8
from flask import *
from db import *
from forms import *


# instancia o app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'teste'

# App que para ir ao endereço da página


@app.route('/', methods=['GET', 'POST'])
# função que retorna o html salvo na pasta templates
def index():

    # requisita o formulario do arquivo forms.py
    formulario = FormularioDeCadastro(request.form)
    formulario2 = FormulariodeExclusao(request.form)

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

    formulario2 = FormulariodeExclusao(request.form)
    placa = None

    if request.method == 'POST' and formulario2.validate_on_submit():

        placa = request.form['pkcodentr']
        insert_sd(request.form['placacarsd'], request.form['dataentrsd'],
                  request.form['horaentrsd'], request.form['datasd'], request.form['horasd'])

    delete_ent(placa)
    return redirect(url_for('index'))


# inicia o servidor
if __name__ == "__main__":
    app.run()
