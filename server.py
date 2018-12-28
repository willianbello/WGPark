from flask import Flask, render_template

#instancia o app
app = Flask(__name__)

#endereço da página
@app.route('/')
#função que retorna o html salvo na pasta templates
def index():
        return render_template('login.html')

#inicia o servidor
if __name__ == "__main__":
    app.run()
#acesso a url
url_for('static', filename='bootstrap/css/bootstrap.min.css')

