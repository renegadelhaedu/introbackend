import psycopg2

def conectar():
    return psycopg2.connect(
        host='localhost',
        database='noitecomp3',
        user='postgres',
        password='12345',
        port=5432
    )

def inserir(nome, matricula, cpf):
    conexao = conectar()
    cur = conexao.cursor()
    exito = False
    try:
        sql = f"INSERT INTO aluno (nome, matricula, cpf) VALUES ('{nome}', '{matricula}', '{cpf}' )"
        cur.execute(sql)
    except psycopg2.IntegrityError:
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True

    conexao.close()
    return exito

def buscar_usuario(cpf):
    conexao = conectar()
    cur = conexao.cursor()

    cur.execute(f"SELECT * FROM aluno WHERE cpf = '{cpf}'")
    recset = cur.fetchall()

    conexao.close()
    return recset

print(buscar_usuario('12345678909'))



