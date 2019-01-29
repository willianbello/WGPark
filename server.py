# coding=UTF-8
from flask import *
from db import *
from forms import *
from datetime import datetime


# instancia o app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'teste'

# App que para ir ao endereço da página
@app.route('/', methods=['GET', 'POST'])

# função que retorna o html salvo na pasta templates
def index():

    # requisita o formulario do arquivo forms.py
    formulario = FormularioDeCadastro(request.form)

    # se obtiver "POST" e validate_on_submit realiza o cadastro das informações no BD e devolve o template de resultado
    # se não, devolve o template index
    if request.method == 'POST' and formulario.validate_on_submit():

        Cadastro.insert_ent(
            None, request.form['placa'], request.form['data'], request.form['hora'])
        return redirect(url_for('index'))

    # função que recebe os dados cadastrados no BD e mostra no template index
    lista = Cadastro.read_ent(None)
    ini = 0
    fim = len(lista)

    # Função para pegar data e hora atual, converter para o formato normal e mandar para o index
    data = datetime.now()
    datatxt = data.strftime("%d/%m/%Y")
    horatxt = data.strftime("%H:%M:%S")

    return render_template('index.html', lista=lista, ini=ini, fim=fim, formulario=formulario, datatxt=datatxt, horatxt=horatxt)


# App que deleta os cadastros no BD
@app.route('/delete/<int:pkcodentr>')
def delete(pkcodentr):

    
    Cadastro.delete_ent(None, pkcodentr)
    return redirect(url_for('index'))


# inicia o servidor
if __name__ == "__main__":
    app.run()
