from flask import *
from db import *


#instancia o app
app = Flask(__name__)

#endereço da página
@app.route('/', methods=['GET', 'POST'])

#função que retorna o html salvo na pasta templates
def index():
    #se obtiver "POST" realiza o cadastro das informações no BD e devolve o template de resultado
    #se não, devolve o template index
    if request.method == 'POST':

        placa = request.form['placa']
        dia = request.form['dia']
        horario = request.form['horario']
        insert_ent(placa, dia, horario) #função que realida o cadastro no BD
        return render_template('result.html', placa=placa, dia=dia, horario=horario)

    #função que recebe os dados cadastrados no BD e mostra no template index
    lista = read_ent()
    ini = 0
    fim = len(lista)
    return render_template('index.html', lista=lista, ini=ini, fim=fim)


#inicia o servidor
if __name__ == "__main__":
    app.run()
