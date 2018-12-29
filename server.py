from flask import Flask, render_template

#instancia o app
app = Flask(__name__)

#endereço da página
@app.route('/')
#função que retorna o html salvo na pasta templates
def index():
        return render_template('index.html')

#inicia o servidor
if __name__ == "__main__":
    app.run()

