from flask import *
from db import *

#instancia o app
app = Flask(__name__)

#endereço da página
@app.route('/', methods=['GET', 'POST'])
#função que retorna o html salvo na pasta templates
def index():
    if request.method == 'POST':

        placa = request.form['placa']
        dia = request.form['dia']
        horario = request.form['horario']
        insert(placa)
        return render_template('result.html', placa=placa, dia=dia, horario=horario)
    return render_template('index.html')

#inicia o servidor
if __name__ == "__main__":
    app.run()
