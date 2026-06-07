from banco import conectar

def cadastrar_aluno(cpf, nome, data_de_nascimento, nome_mae, nome_pai):
    conexao, cursor = conectar()
    cursor.execute(
        "INSERT INTO alunos (cpf, nome, data_de_nascimento, nome_mae, nome_pai) VALUES (%s, %s, %s, %s, %s)",
        (cpf, nome, data_de_nascimento, nome_mae, nome_pai)
    )

    conexao.commit()
    conexao.close()

def listar_alunos():
    conexao, cursor = conectar()
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    conexao.close()
    return alunos

def buscar_aluno(cpf_aluno):
    conexao, cursor = conectar()
    cursor.execute(
        "SELECT * FROM alunos WHERE cpf = %s",
        (cpf_aluno,)
    )
    alunos = cursor.fetchone()
    conexao.close()
    return alunos

def atualizar_aluno(cpf_aluno, novo_nome, data_de_nascimento, nome_mae, nome_pai):
    conexao, cursor = conectar()
    cursor.execute(
        """UPDATE alunos  SET nome = %s, data_de_nascimento = %s, nome_mae = %s, nome_pai = %s WHERE CPF = %s""",
        (novo_nome, data_de_nascimento, nome_mae, nome_pai, cpf_aluno)
    )
    conexao.commit()
    conexao.close()

def excluir_aluno(cpf_aluno):
    conexao, cursor = conectar()
    cursor.execute(
        "DELETE FROM alunos WHERE cpf = %s",
        (cpf_aluno,)
    )

    conexao.commit()
    conexao.close()