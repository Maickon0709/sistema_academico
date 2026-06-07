from banco import conectar

def criar_disciplina(nome):
    conexao, cursor = conectar()
    cursor.execute(
        "INSERT INTO disciplinas (nome) VALUES (%s)",
        (nome,)
    )
    conexao.commit()
    conexao.close()

def buscar_disciplina(id_disciplina):
    conexao, cursor = conectar()
    cursor.execute(
        "SELECT * FROM disciplinas WHERE id = %s",
        (id_disciplina,)
    )
    disciplinas = cursor.fetchone()
    conexao.close()
    return disciplinas

def listar_disciplinas():
    conexao, cursor = conectar()
    cursor.execute("SELECT * FROM disciplinas")
    disciplinas = cursor.fetchall()
    conexao.close()
    return disciplinas

def atualizar_disciplina(nome, id):
    conexao, cursor = conectar()
    cursor.execute(
        "UPDATE disciplinas SET nome = %s WHERE id = %s",
        (nome, id)
    )
    conexao.commit()
    conexao.close()

def excluir_disciplinas(id):
    conexao, cursor = conectar()
    cursor.execute(
        "DELETE FROM disciplinas WHERE id = %s",
        (id,)
    )
    conexao.commit()
    conexao.close()