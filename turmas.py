from banco import conectar

def cadastrar_turma(numero_turma, periodo):
    conexao, cursor = conectar()
    cursor.execute(
        "INSERT INTO turmas (numero_turma, periodo) VALUES (%s, %s)",
        (numero_turma, periodo)
    )
    conexao.commit()
    conexao.close()

def listar_turma():
    conexao, cursor = conectar()

    cursor.execute("SELECT * FROM turmas")
    turmas = cursor.fetchall()
    conexao.close()
    return turmas

def buscar_turma(numero_turma):
    conexao, cursor = conectar()
    cursor.execute(
        "SELECT * FROM turmas WHERE numero_turma = %s",
        (numero_turma,)
    )
    turmas = cursor.fetchone()
    conexao.close()
    return turmas

def atualizar_turma(novo_periodo, numero_turma):
    conexao, cursor = conectar()
    cursor.execute(
        """UPDATE turmas SET periodo = %s WHERE numero_turma = %s""",
        (novo_periodo, numero_turma)
    )

    conexao.commit()
    conexao.close()

def excluir_turma(numero_turma):
    conexao, cursor = conectar()
    cursor.execute(
        "DELETE FROM turmas WHERE numero_turma = %s",
        (numero_turma,)
    )

    conexao.commit()
    conexao.close()
