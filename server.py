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

        entrada = Cadastro(request.form['placa'], request.form['dia'], request.form['horario'])
        entrada.insert_ent(entrada.placa, entrada.dia, entrada.horario)
        return render_template('result.html', entrada=entrada)

    if request.method == 'post':

        Cadastro.delete_ent(None, request.form['{{ lista[ini][0] }}'])
        return render_template('delete.html')

    #função que recebe os dados cadastrados no BD e mostra no template index
    lista = Cadastro.read_ent(None)
    ini = 0
    fim = len(lista)
    return render_template('index.html', lista=lista, ini=ini, fim=fim)


#inicia o servidor
if __name__ == "__main__":
    app.run()
