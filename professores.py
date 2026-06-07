from banco import conectar

def cadastrar_professores(cpf, nome, especialidade):
    conexao, cursor = conectar()
    cursor.execute(
        "INSERT INTO professores (cpf, nome, especialidade) VALUES (%s, %s, %s)",
        (cpf, nome, especialidade)
    )

    conexao.commit()
    conexao.close()

def listar_professores():
    conexao, cursor = conectar()

    cursor.execute("SELECT * FROM professores")
    professores = cursor.fetchall()
    conexao.close()
    return professores

def atualizar_professor(novo_nome, especialidade, cpf):
    conexao, cursor = conectar()
    cursor.execute(
        """UPDATE professores SET nome = %s, especialidade = %s WHERE cpf = %s""",
        (novo_nome, especialidade, cpf)
    )

    conexao.commit()
    conexao.close()

def excluir_professor(cpf_professor):
    conexao, cursor = conectar()
    cursor.execute(
        "DELETE FROM professores WHERE cpf = %s",
        (cpf_professor,)
    )

    conexao.commit()
    conexao.close()

def buscar_professor(cpf_professor):
    conexao, cursor = conectar()
    cursor.execute(
        "SELECT * FROM professores WHERE cpf = %s",
        (cpf_professor,)
    )
    professores = cursor.fetchone()
    conexao.close()
    return professores
