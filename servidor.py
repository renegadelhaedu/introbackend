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

@app.route('/paginabusca')
def mostrar_pag_busca():
    return render_template('busca.html')


@app.route('/buscarcpf', methods=['POST'])
def buscar_cpf():
    cpf = request.form.get('cpfaluno')
    aluno = dao.buscar_usuario(cpf)
    if len(aluno) > 0:
        nome = aluno[0][0]
        matric = aluno[0][1]
        cpf = aluno[0][2]
        return render_template('exibiraluno.html', nome=nome, matricula=matric, cpf=cpf)
    else:
        return 'usuário nao encontrado'




if __name__ == '__main__':
    app.run()