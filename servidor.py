from flask import *

app = Flask(__name__)

@app.route('/')
def pagina_principal():
    return render_template('index.html')

@app.route('/paginacadastro')
def mostrar_pag_cadastro():
    return render_template('pagcadastro.html')


if __name__ == '__main__':
    app.run()