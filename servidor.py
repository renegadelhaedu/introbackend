from flask import *
import dao

app = Flask(__name__)

@app.route('/')
def pagina_principal():
    return render_template('index.html')

@app.route('/paginacadastro', methods=['GET'])
def mostrar_pag_cadastro():
    return render_template('pagcadastro.html')

@app.route('/cadastraraluno', methods=['POST'])
def cadastrar_usuario():
    nome = request.form.get('nomeusuario')
    matricula = request.form.get('matricula')
    cpf = request.form.get('cpf')
    if dao.inserir(nome, matricula, cpf):
        return 'deu certo', 200
    else:
        return 'algo deu errado', 400



if __name__ == '__main__':
    app.run()