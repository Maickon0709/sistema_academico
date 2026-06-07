import tkinter as tk
from tkinter import messagebox
from alunos import cadastrar_aluno, listar_alunos, buscar_aluno, atualizar_aluno, excluir_aluno
from professores import cadastrar_professores, listar_professores, buscar_professor, atualizar_professor, excluir_professor
from turmas import cadastrar_turma, listar_turma, buscar_turma, atualizar_turma, excluir_turma
from disciplinas import criar_disciplina, listar_disciplinas, buscar_disciplina, atualizar_disciplina, excluir_disciplinas

janela = tk.Tk()
janela.title("Sistema Acadêmico")
janela.geometry("900x600")
janela.configure(bg="white")

frame_menu = tk.Frame(janela, bg="navy", width=200)
frame_menu.pack(side="left", fill="y")
frame_menu.pack_propagate(False)

frame_conteudo = tk.Frame(janela, bg="white")
frame_conteudo.pack(side="right", fill="both", expand=True)

tk.Label(frame_menu, text="Sistema\nAcadêmico", bg="navy", fg="white", font=("Arial", 14, "bold")).pack(pady=30)

def limpar_conteudo():
    for widget in frame_conteudo.winfo_children():
        widget.destroy()

def titulo_conteudo(texto):
    tk.Label(frame_conteudo, text=texto, font=("Arial", 18, "bold"), bg="white", fg="navy").pack(pady=20)

# ==================== ALUNOS ====================

def tela_cadastrar_aluno():
    limpar_conteudo()
    titulo_conteudo("Cadastrar Aluno")
    campos = {}
    for label in ["CPF", "Nome", "Data de Nascimento (AAAA-MM-DD)", "Nome da Mãe", "Nome do Pai"]:
        tk.Label(frame_conteudo, text=label, bg="white", font=("Arial", 11)).pack()
        entry = tk.Entry(frame_conteudo, width=40, font=("Arial", 11))
        entry.pack(pady=5)
        campos[label] = entry

    def confirmar():
        cpf = campos["CPF"].get()
        nome = campos["Nome"].get()
        data = campos["Data de Nascimento (AAAA-MM-DD)"].get()
        mae = campos["Nome da Mãe"].get()
        pai = campos["Nome do Pai"].get()
        if not all([cpf, nome, data, mae, pai]):
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
            return
        try:
            cadastrar_aluno(cpf, nome, data, mae, pai)
            messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
            mostrar_alunos()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    tk.Button(frame_conteudo, text="Cadastrar", bg="navy", fg="white", font=("Arial", 11), width=20, command=confirmar).pack(pady=15)
    tk.Button(frame_conteudo, text="Voltar", font=("Arial", 10), width=20, command=mostrar_alunos).pack()

def tela_listar_alunos():
    limpar_conteudo()
    titulo_conteudo("Lista de Alunos")
    frame_lista = tk.Frame(frame_conteudo, bg="white")
    frame_lista.pack(fill="both", expand=True, padx=20)
    try:
        alunos = listar_alunos()
        if not alunos:
            tk.Label(frame_lista, text="Nenhum aluno cadastrado.", bg="white", font=("Arial", 11)).pack(pady=20)
        else:
            for aluno in alunos:
                frame_aluno = tk.Frame(frame_lista, bg="#f0f0f0", pady=8, padx=10)
                frame_aluno.pack(fill="x", pady=5)
                tk.Label(frame_aluno, text=f"CPF: {aluno[0]}  |  Nome: {aluno[1]}  |  Nasc: {aluno[2]}  |  Mãe: {aluno[3]}  |  Pai: {aluno[4]}", bg="#f0f0f0", font=("Arial", 10)).pack(anchor="w")
    except Exception as e:
        messagebox.showerror("Erro", str(e))
    tk.Button(frame_conteudo, text="Voltar", font=("Arial", 10), width=20, command=mostrar_alunos).pack(pady=10)

def tela_buscar_aluno():
    limpar_conteudo()
    titulo_conteudo("Buscar Aluno")
    tk.Label(frame_conteudo, text="CPF do Aluno", bg="white", font=("Arial", 11)).pack()
    entry_cpf = tk.Entry(frame_conteudo, width=40, font=("Arial", 11))
    entry_cpf.pack(pady=5)
    frame_resultado = tk.Frame(frame_conteudo, bg="white")
    frame_resultado.pack(pady=10)

    def buscar():
        for w in frame_resultado.winfo_children():
            w.destroy()
        try:
            aluno = buscar_aluno(entry_cpf.get())
            if aluno:
                tk.Label(frame_resultado, text=f"CPF: {aluno[0]}", bg="white", font=("Arial", 11)).pack()
                tk.Label(frame_resultado, text=f"Nome: {aluno[1]}", bg="white", font=("Arial", 11)).pack()
                tk.Label(frame_resultado, text=f"Nascimento: {aluno[2]}", bg="white", font=("Arial", 11)).pack()
                tk.Label(frame_resultado, text=f"Mãe: {aluno[3]}", bg="white", font=("Arial", 11)).pack()
                tk.Label(frame_resultado, text=f"Pai: {aluno[4]}", bg="white", font=("Arial", 11)).pack()
            else:
                tk.Label(frame_resultado, text="Aluno não encontrado.", bg="white", font=("Arial", 11), fg="red").pack()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    tk.Button(frame_conteudo, text="Buscar", bg="navy", fg="white", font=("Arial", 11), width=20, command=buscar).pack(pady=10)
    tk.Button(frame_conteudo, text="Voltar", font=("Arial", 10), width=20, command=mostrar_alunos).pack()

def tela_atualizar_aluno():
    limpar_conteudo()
    titulo_conteudo("Atualizar Aluno")
    tk.Label(frame_conteudo, text="CPF do Aluno", bg="white", font=("Arial", 11)).pack()
    entry_cpf = tk.Entry(frame_conteudo, width=40, font=("Arial", 11))
    entry_cpf.pack(pady=5)
    campos = {}
    for label in ["Novo Nome", "Nova Data de Nascimento (AAAA-MM-DD)", "Novo Nome da Mãe", "Novo Nome do Pai"]:
        tk.Label(frame_conteudo, text=label, bg="white", font=("Arial", 11)).pack()
        entry = tk.Entry(frame_conteudo, width=40, font=("Arial", 11))
        entry.pack(pady=3)
        campos[label] = entry

    def confirmar():
        try:
            atualizar_aluno(entry_cpf.get(), campos["Novo Nome"].get(), campos["Nova Data de Nascimento (AAAA-MM-DD)"].get(), campos["Novo Nome da Mãe"].get(), campos["Novo Nome do Pai"].get())
            messagebox.showinfo("Sucesso", "Aluno atualizado!")
            mostrar_alunos()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    tk.Button(frame_conteudo, text="Atualizar", bg="navy", fg="white", font=("Arial", 11), width=20, command=confirmar).pack(pady=10)
    tk.Button(frame_conteudo, text="Voltar", font=("Arial", 10), width=20, command=mostrar_alunos).pack()

def tela_excluir_aluno():
    limpar_conteudo()
    titulo_conteudo("Excluir Aluno")
    tk.Label(frame_conteudo, text="CPF do Aluno", bg="white", font=("Arial", 11)).pack()
    entry_cpf = tk.Entry(frame_conteudo, width=40, font=("Arial", 11))
    entry_cpf.pack(pady=5)

    def confirmar():
        cpf = entry_cpf.get()
        if messagebox.askyesno("Confirmar", f"Deseja excluir o aluno com CPF {cpf}?"):
            try:
                excluir_aluno(cpf)
                messagebox.showinfo("Sucesso", "Aluno excluído!")
                mostrar_alunos()
            except Exception as e:
                messagebox.showerror("Erro", str(e))

    tk.Button(frame_conteudo, text="Excluir", bg="red", fg="white", font=("Arial", 11), width=20, command=confirmar).pack(pady=10)
    tk.Button(frame_conteudo, text="Voltar", font=("Arial", 10), width=20, command=mostrar_alunos).pack()

def mostrar_alunos():
    limpar_conteudo()
    titulo_conteudo("Alunos")
    tk.Button(frame_conteudo, text="Cadastrar Aluno", width=30, font=("Arial", 11), command=tela_cadastrar_aluno).pack(pady=5)
    tk.Button(frame_conteudo, text="Listar Alunos", width=30, font=("Arial", 11), command=tela_listar_alunos).pack(pady=5)
    tk.Button(frame_conteudo, text="Buscar Aluno", width=30, font=("Arial", 11), command=tela_buscar_aluno).pack(pady=5)
    tk.Button(frame_conteudo, text="Atualizar Aluno", width=30, font=("Arial", 11), command=tela_atualizar_aluno).pack(pady=5)
    tk.Button(frame_conteudo, text="Excluir Aluno", width=30, font=("Arial", 11), command=tela_excluir_aluno).pack(pady=5)

# ==================== PROFESSORES ====================

def tela_cadastrar_professor():
    limpar_conteudo()
    titulo_conteudo("Cadastrar Professor")
    campos = {}
    for label in ["CPF", "Nome", "Especialidade"]:
        tk.Label(frame_conteudo, text=label, bg="white", font=("Arial", 11)).pack()
        entry = tk.Entry(frame_conteudo, width=40, font=("Arial", 11))
        entry.pack(pady=5)
        campos[label] = entry

    def confirmar():
        cpf = campos["CPF"].get()
        nome = campos["Nome"].get()
        especialidade = campos["Especialidade"].get()
        if not all([cpf, nome, especialidade]):
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
            return
        try:
            cadastrar_professores(cpf, nome, especialidade)
            messagebox.showinfo("Sucesso", "Professor cadastrado!")
            mostrar_professores()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    tk.Button(frame_conteudo, text="Cadastrar", bg="navy", fg="white", font=("Arial", 11), width=20, command=confirmar).pack(pady=15)
    tk.Button(frame_conteudo, text="Voltar", font=("Arial", 10), width=20, command=mostrar_professores).pack()

def tela_listar_professores():
    limpar_conteudo()
    titulo_conteudo("Lista de Professores")
    frame_lista = tk.Frame(frame_conteudo, bg="white")
    frame_lista.pack(fill="both", expand=True, padx=20)
    try:
        professores = listar_professores()
        if not professores:
            tk.Label(frame_lista, text="Nenhum professor cadastrado.", bg="white", font=("Arial", 11)).pack(pady=20)
        else:
            for professor in professores:
                frame_p = tk.Frame(frame_lista, bg="#f0f0f0", pady=8, padx=10)
                frame_p.pack(fill="x", pady=5)
                tk.Label(frame_p, text=f"CPF: {professor[0]}  |  Nome: {professor[1]}  |  Especialidade: {professor[2]}", bg="#f0f0f0", font=("Arial", 10)).pack(anchor="w")
    except Exception as e:
        messagebox.showerror("Erro", str(e))
    tk.Button(frame_conteudo, text="Voltar", font=("Arial", 10), width=20, command=mostrar_professores).pack(pady=10)

def tela_buscar_professor():
    limpar_conteudo()
    titulo_conteudo("Buscar Professor")
    tk.Label(frame_conteudo, text="CPF do Professor", bg="white", font=("Arial", 11)).pack()
    entry_cpf = tk.Entry(frame_conteudo, width=40, font=("Arial", 11))
    entry_cpf.pack(pady=5)
    frame_resultado = tk.Frame(frame_conteudo, bg="white")
    frame_resultado.pack(pady=10)

    def buscar():
        for w in frame_resultado.winfo_children():
            w.destroy()
        try:
            professor = buscar_professor(entry_cpf.get())
            if professor:
                tk.Label(frame_resultado, text=f"CPF: {professor[0]}", bg="white", font=("Arial", 11)).pack()
                tk.Label(frame_resultado, text=f"Nome: {professor[1]}", bg="white", font=("Arial", 11)).pack()
                tk.Label(frame_resultado, text=f"Especialidade: {professor[2]}", bg="white", font=("Arial", 11)).pack()
            else:
                tk.Label(frame_resultado, text="Professor não encontrado.", bg="white", font=("Arial", 11), fg="red").pack()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    tk.Button(frame_conteudo, text="Buscar", bg="navy", fg="white", font=("Arial", 11), width=20, command=buscar).pack(pady=10)
    tk.Button(frame_conteudo, text="Voltar", font=("Arial", 10), width=20, command=mostrar_professores).pack()

def tela_atualizar_professor():
    limpar_conteudo()
    titulo_conteudo("Atualizar Professor")
    tk.Label(frame_conteudo, text="CPF do Professor", bg="white", font=("Arial", 11)).pack()
    entry_cpf = tk.Entry(frame_conteudo, width=40, font=("Arial", 11))
    entry_cpf.pack(pady=5)
    campos = {}
    for label in ["Novo Nome", "Nova Especialidade"]:
        tk.Label(frame_conteudo, text=label, bg="white", font=("Arial", 11)).pack()
        entry = tk.Entry(frame_conteudo, width=40, font=("Arial", 11))
        entry.pack(pady=3)
        campos[label] = entry

    def confirmar():
        try:
            atualizar_professor(campos["Novo Nome"].get(), campos["Nova Especialidade"].get(), entry_cpf.get())
            messagebox.showinfo("Sucesso", "Professor atualizado!")
            mostrar_professores()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    tk.Button(frame_conteudo, text="Atualizar", bg="navy", fg="white", font=("Arial", 11), width=20, command=confirmar).pack(pady=10)
    tk.Button(frame_conteudo, text="Voltar", font=("Arial", 10), width=20, command=mostrar_professores).pack()

def tela_excluir_professor():
    limpar_conteudo()
    titulo_conteudo("Excluir Professor")
    tk.Label(frame_conteudo, text="CPF do Professor", bg="white", font=("Arial", 11)).pack()
    entry_cpf = tk.Entry(frame_conteudo, width=40, font=("Arial", 11))
    entry_cpf.pack(pady=5)

    def confirmar():
        cpf = entry_cpf.get()
        if messagebox.askyesno("Confirmar", f"Deseja excluir o professor com CPF {cpf}?"):
            try:
                excluir_professor(cpf)
                messagebox.showinfo("Sucesso", "Professor excluído!")
                mostrar_professores()
            except Exception as e:
                messagebox.showerror("Erro", str(e))

    tk.Button(frame_conteudo, text="Excluir", bg="red", fg="white", font=("Arial", 11), width=20, command=confirmar).pack(pady=10)
    tk.Button(frame_conteudo, text="Voltar", font=("Arial", 10), width=20, command=mostrar_professores).pack()

def mostrar_professores():
    limpar_conteudo()
    titulo_conteudo("Professores")
    tk.Button(frame_conteudo, text="Cadastrar Professor", width=30, font=("Arial", 11), command=tela_cadastrar_professor).pack(pady=5)
    tk.Button(frame_conteudo, text="Listar Professores", width=30, font=("Arial", 11), command=tela_listar_professores).pack(pady=5)
    tk.Button(frame_conteudo, text="Buscar Professor", width=30, font=("Arial", 11), command=tela_buscar_professor).pack(pady=5)
    tk.Button(frame_conteudo, text="Atualizar Professor", width=30, font=("Arial", 11), command=tela_atualizar_professor).pack(pady=5)
    tk.Button(frame_conteudo, text="Excluir Professor", width=30, font=("Arial", 11), command=tela_excluir_professor).pack(pady=5)

# ==================== TURMAS ====================

def tela_cadastrar_turma():
    limpar_conteudo()
    titulo_conteudo("Cadastrar Turma")
    tk.Label(frame_conteudo, text="Número da Turma (ex: 3A)", bg="white", font=("Arial", 11)).pack()
    entry_numero = tk.Entry(frame_conteudo, width=40, font=("Arial", 11))
    entry_numero.pack(pady=5)
    tk.Label(frame_conteudo, text="Período", bg="white", font=("Arial", 11)).pack()
    periodo_var = tk.StringVar(value="Manhã")
    for opcao in ["Manhã", "Tarde", "Noite"]:
        tk.Radiobutton(frame_conteudo, text=opcao, variable=periodo_var, value=opcao, bg="white", font=("Arial", 11)).pack()

    def confirmar():
        numero = entry_numero.get()
        if not numero:
            messagebox.showwarning("Atenção", "Preencha o número da turma!")
            return
        try:
            cadastrar_turma(numero, periodo_var.get())
            messagebox.showinfo("Sucesso", "Turma cadastrada!")
            mostrar_turmas()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    tk.Button(frame_conteudo, text="Cadastrar", bg="navy", fg="white", font=("Arial", 11), width=20, command=confirmar).pack(pady=15)
    tk.Button(frame_conteudo, text="Voltar", font=("Arial", 10), width=20, command=mostrar_turmas).pack()

def tela_listar_turmas():
    limpar_conteudo()
    titulo_conteudo("Lista de Turmas")
    frame_lista = tk.Frame(frame_conteudo, bg="white")
    frame_lista.pack(fill="both", expand=True, padx=20)
    try:
        turmas = listar_turma()
        if not turmas:
            tk.Label(frame_lista, text="Nenhuma turma cadastrada.", bg="white", font=("Arial", 11)).pack(pady=20)
        else:
            for turma in turmas:
                frame_t = tk.Frame(frame_lista, bg="#f0f0f0", pady=8, padx=10)
                frame_t.pack(fill="x", pady=5)
                tk.Label(frame_t, text=f"ID: {turma[0]}  |  Número: {turma[1]}  |  Período: {turma[2]}", bg="#f0f0f0", font=("Arial", 10)).pack(anchor="w")
    except Exception as e:
        messagebox.showerror("Erro", str(e))
    tk.Button(frame_conteudo, text="Voltar", font=("Arial", 10), width=20, command=mostrar_turmas).pack(pady=10)

def tela_buscar_turma():
    limpar_conteudo()
    titulo_conteudo("Buscar Turma")
    tk.Label(frame_conteudo, text="Número da Turma", bg="white", font=("Arial", 11)).pack()
    entry_numero = tk.Entry(frame_conteudo, width=40, font=("Arial", 11))
    entry_numero.pack(pady=5)
    frame_resultado = tk.Frame(frame_conteudo, bg="white")
    frame_resultado.pack(pady=10)

    def buscar():
        for w in frame_resultado.winfo_children():
            w.destroy()
        try:
            turma = buscar_turma(entry_numero.get())
            if turma:
                tk.Label(frame_resultado, text=f"ID: {turma[0]}", bg="white", font=("Arial", 11)).pack()
                tk.Label(frame_resultado, text=f"Número: {turma[1]}", bg="white", font=("Arial", 11)).pack()
                tk.Label(frame_resultado, text=f"Período: {turma[2]}", bg="white", font=("Arial", 11)).pack()
            else:
                tk.Label(frame_resultado, text="Turma não encontrada.", bg="white", font=("Arial", 11), fg="red").pack()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    tk.Button(frame_conteudo, text="Buscar", bg="navy", fg="white", font=("Arial", 11), width=20, command=buscar).pack(pady=10)
    tk.Button(frame_conteudo, text="Voltar", font=("Arial", 10), width=20, command=mostrar_turmas).pack()

def tela_atualizar_turma():
    limpar_conteudo()
    titulo_conteudo("Atualizar Turma")
    tk.Label(frame_conteudo, text="Número da Turma", bg="white", font=("Arial", 11)).pack()
    entry_numero = tk.Entry(frame_conteudo, width=40, font=("Arial", 11))
    entry_numero.pack(pady=5)
    tk.Label(frame_conteudo, text="Novo Período", bg="white", font=("Arial", 11)).pack()
    periodo_var = tk.StringVar(value="Manhã")
    for opcao in ["Manhã", "Tarde", "Noite"]:
        tk.Radiobutton(frame_conteudo, text=opcao, variable=periodo_var, value=opcao, bg="white", font=("Arial", 11)).pack()

    def confirmar():
        try:
            atualizar_turma(periodo_var.get(), entry_numero.get())
            messagebox.showinfo("Sucesso", "Turma atualizada!")
            mostrar_turmas()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    tk.Button(frame_conteudo, text="Atualizar", bg="navy", fg="white", font=("Arial", 11), width=20, command=confirmar).pack(pady=10)
    tk.Button(frame_conteudo, text="Voltar", font=("Arial", 10), width=20, command=mostrar_turmas).pack()

def tela_excluir_turma():
    limpar_conteudo()
    titulo_conteudo("Excluir Turma")
    tk.Label(frame_conteudo, text="Número da Turma", bg="white", font=("Arial", 11)).pack()
    entry_numero = tk.Entry(frame_conteudo, width=40, font=("Arial", 11))
    entry_numero.pack(pady=5)

    def confirmar():
        numero = entry_numero.get()
        if messagebox.askyesno("Confirmar", f"Deseja excluir a turma {numero}?"):
            try:
                excluir_turma(numero)
                messagebox.showinfo("Sucesso", "Turma excluída!")
                mostrar_turmas()
            except Exception as e:
                messagebox.showerror("Erro", str(e))

    tk.Button(frame_conteudo, text="Excluir", bg="red", fg="white", font=("Arial", 11), width=20, command=confirmar).pack(pady=10)
    tk.Button(frame_conteudo, text="Voltar", font=("Arial", 10), width=20, command=mostrar_turmas).pack()

def mostrar_turmas():
    limpar_conteudo()
    titulo_conteudo("Turmas")
    tk.Button(frame_conteudo, text="Cadastrar Turma", width=30, font=("Arial", 11), command=tela_cadastrar_turma).pack(pady=5)
    tk.Button(frame_conteudo, text="Listar Turmas", width=30, font=("Arial", 11), command=tela_listar_turmas).pack(pady=5)
    tk.Button(frame_conteudo, text="Buscar Turma", width=30, font=("Arial", 11), command=tela_buscar_turma).pack(pady=5)
    tk.Button(frame_conteudo, text="Atualizar Turma", width=30, font=("Arial", 11), command=tela_atualizar_turma).pack(pady=5)
    tk.Button(frame_conteudo, text="Excluir Turma", width=30, font=("Arial", 11), command=tela_excluir_turma).pack(pady=5)

# ==================== DISCIPLINAS ====================

def tela_cadastrar_disciplina():
    limpar_conteudo()
    titulo_conteudo("Cadastrar Disciplina")
    tk.Label(frame_conteudo, text="Nome", bg="white", font=("Arial", 11)).pack()
    entry_nome = tk.Entry(frame_conteudo, width=40, font=("Arial", 11))
    entry_nome.pack(pady=5)

    def confirmar():
        nome = entry_nome.get()
        if not nome:
            messagebox.showwarning("Atenção", "Preencha o nome da disciplina!")
            return
        try:
            criar_disciplina(nome)
            messagebox.showinfo("Sucesso", "Disciplina cadastrada!")
            mostrar_disciplinas()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    tk.Button(frame_conteudo, text="Cadastrar", bg="navy", fg="white", font=("Arial", 11), width=20, command=confirmar).pack(pady=15)
    tk.Button(frame_conteudo, text="Voltar", font=("Arial", 10), width=20, command=mostrar_disciplinas).pack()

def tela_listar_disciplinas():
    limpar_conteudo()
    titulo_conteudo("Lista de Disciplinas")
    frame_lista = tk.Frame(frame_conteudo, bg="white")
    frame_lista.pack(fill="both", expand=True, padx=20)
    try:
        disciplinas = listar_disciplinas()
        if not disciplinas:
            tk.Label(frame_lista, text="Nenhuma disciplina cadastrada.", bg="white", font=("Arial", 11)).pack(pady=20)
        else:
            for d in disciplinas:
                frame_d = tk.Frame(frame_lista, bg="#f0f0f0", pady=8, padx=10)
                frame_d.pack(fill="x", pady=5)
                tk.Label(frame_d, text=f"ID: {d[0]}  |  Nome: {d[1]}", bg="#f0f0f0", font=("Arial", 10)).pack(anchor="w")
    except Exception as e:
        messagebox.showerror("Erro", str(e))
    tk.Button(frame_conteudo, text="Voltar", font=("Arial", 10), width=20, command=mostrar_disciplinas).pack(pady=10)

def tela_atualizar_disciplina():
    limpar_conteudo()
    titulo_conteudo("Atualizar Disciplina")
    tk.Label(frame_conteudo, text="ID da Disciplina", bg="white", font=("Arial", 11)).pack()
    entry_id = tk.Entry(frame_conteudo, width=40, font=("Arial", 11))
    entry_id.pack(pady=5)
    tk.Label(frame_conteudo, text="Novo Nome", bg="white", font=("Arial", 11)).pack()
    entry_nome = tk.Entry(frame_conteudo, width=40, font=("Arial", 11))
    entry_nome.pack(pady=3)

    def confirmar():
        try:
            atualizar_disciplina(entry_nome.get(), entry_id.get())
            messagebox.showinfo("Sucesso", "Disciplina atualizada!")
            mostrar_disciplinas()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    tk.Button(frame_conteudo, text="Atualizar", bg="navy", fg="white", font=("Arial", 11), width=20, command=confirmar).pack(pady=10)
    tk.Button(frame_conteudo, text="Voltar", font=("Arial", 10), width=20, command=mostrar_disciplinas).pack()

def tela_excluir_disciplina():
    limpar_conteudo()
    titulo_conteudo("Excluir Disciplina")
    tk.Label(frame_conteudo, text="ID da Disciplina", bg="white", font=("Arial", 11)).pack()
    entry_id = tk.Entry(frame_conteudo, width=40, font=("Arial", 11))
    entry_id.pack(pady=5)

    def confirmar():
        id_disc = entry_id.get()
        if messagebox.askyesno("Confirmar", f"Deseja excluir a disciplina ID {id_disc}?"):
            try:
                excluir_disciplinas(id_disc)
                messagebox.showinfo("Sucesso", "Disciplina excluída!")
                mostrar_disciplinas()
            except Exception as e:
                messagebox.showerror("Erro", str(e))

    tk.Button(frame_conteudo, text="Excluir", bg="red", fg="white", font=("Arial", 11), width=20, command=confirmar).pack(pady=10)
    tk.Button(frame_conteudo, text="Voltar", font=("Arial", 10), width=20, command=mostrar_disciplinas).pack()

def mostrar_disciplinas():
    limpar_conteudo()
    titulo_conteudo("Disciplinas")
    tk.Button(frame_conteudo, text="Cadastrar Disciplina", width=30, font=("Arial", 11), command=tela_cadastrar_disciplina).pack(pady=5)
    tk.Button(frame_conteudo, text="Listar Disciplinas", width=30, font=("Arial", 11), command=tela_listar_disciplinas).pack(pady=5)
    tk.Button(frame_conteudo, text="Atualizar Disciplina", width=30, font=("Arial", 11), command=tela_atualizar_disciplina).pack(pady=5)
    tk.Button(frame_conteudo, text="Excluir Disciplina", width=30, font=("Arial", 11), command=tela_excluir_disciplina).pack(pady=5)

# ==================== MATRÍCULAS ====================

def tela_matricular():
    limpar_conteudo()
    titulo_conteudo("Matricular Aluno em Turma")
    tk.Label(frame_conteudo, text="CPF do Aluno", bg="white", font=("Arial", 11)).pack()
    entry_cpf = tk.Entry(frame_conteudo, width=40, font=("Arial", 11))
    entry_cpf.pack(pady=5)
    tk.Label(frame_conteudo, text="Número da Turma", bg="white", font=("Arial", 11)).pack()
    entry_turma = tk.Entry(frame_conteudo, width=40, font=("Arial", 11))
    entry_turma.pack(pady=5)

    def confirmar():
        cpf = entry_cpf.get()
        turma = entry_turma.get()
        if not all([cpf, turma]):
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
            return
        try:
            from banco import conectar
            conexao, cursor = conectar()
            cursor.execute("INSERT INTO aluno_turmas (cpf_aluno, numero_turmas) VALUES (%s, %s)", (cpf, turma))
            conexao.commit()
            conexao.close()
            messagebox.showinfo("Sucesso", "Aluno matriculado com sucesso!")
            mostrar_matriculas()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    tk.Button(frame_conteudo, text="Matricular", bg="navy", fg="white", font=("Arial", 11), width=20, command=confirmar).pack(pady=15)
    tk.Button(frame_conteudo, text="Voltar", font=("Arial", 10), width=20, command=mostrar_matriculas).pack()

def tela_listar_matriculas():
    limpar_conteudo()
    titulo_conteudo("Lista de Matrículas")
    frame_lista = tk.Frame(frame_conteudo, bg="white")
    frame_lista.pack(fill="both", expand=True, padx=20)
    try:
        from banco import conectar
        conexao, cursor = conectar()
        cursor.execute("""
            SELECT a.nome, a.cpf, t.numero_turma, t.periodo
            FROM aluno_turmas at2
            JOIN alunos a ON at2.cpf_aluno = a.cpf
            JOIN turmas t ON at2.numero_turmas = t.numero_turma
        """)
        matriculas = cursor.fetchall()
        conexao.close()
        if not matriculas:
            tk.Label(frame_lista, text="Nenhuma matrícula cadastrada.", bg="white", font=("Arial", 11)).pack(pady=20)
        else:
            for m in matriculas:
                frame_m = tk.Frame(frame_lista, bg="#f0f0f0", pady=8, padx=10)
                frame_m.pack(fill="x", pady=5)
                tk.Label(frame_m, text=f"Aluno: {m[0]}  |  CPF: {m[1]}  |  Turma: {m[2]}  |  Período: {m[3]}", bg="#f0f0f0", font=("Arial", 10)).pack(anchor="w")
    except Exception as e:
        messagebox.showerror("Erro", str(e))
    tk.Button(frame_conteudo, text="Voltar", font=("Arial", 10), width=20, command=mostrar_matriculas).pack(pady=10)

def mostrar_matriculas():
    limpar_conteudo()
    titulo_conteudo("Matrículas")
    tk.Button(frame_conteudo, text="Matricular Aluno em Turma", width=30, font=("Arial", 11), command=tela_matricular).pack(pady=5)
    tk.Button(frame_conteudo, text="Listar Matrículas", width=30, font=("Arial", 11), command=tela_listar_matriculas).pack(pady=5)

# ==================== HORÁRIOS ====================

def tela_cadastrar_horario():
    limpar_conteudo()
    titulo_conteudo("Cadastrar Horário")
    tk.Label(frame_conteudo, text="Dia da Semana", bg="white", font=("Arial", 11)).pack()
    dia_var = tk.StringVar(value="Segunda")
    for dia in ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]:
        tk.Radiobutton(frame_conteudo, text=dia, variable=dia_var, value=dia, bg="white", font=("Arial", 11)).pack()
    tk.Label(frame_conteudo, text="Hora Início (HH:MM)", bg="white", font=("Arial", 11)).pack(pady=(10,0))
    entry_inicio = tk.Entry(frame_conteudo, width=20, font=("Arial", 11))
    entry_inicio.pack(pady=5)
    tk.Label(frame_conteudo, text="Hora Fim (HH:MM)", bg="white", font=("Arial", 11)).pack()
    entry_fim = tk.Entry(frame_conteudo, width=20, font=("Arial", 11))
    entry_fim.pack(pady=5)

    def confirmar():
        inicio = entry_inicio.get()
        fim = entry_fim.get()
        if not all([inicio, fim]):
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
            return
        try:
            from banco import conectar
            conexao, cursor = conectar()
            cursor.execute("INSERT INTO horario (dia_semana, hora_inicio, hora_fim) VALUES (%s, %s, %s)", (dia_var.get(), inicio, fim))
            conexao.commit()
            conexao.close()
            messagebox.showinfo("Sucesso", "Horário cadastrado!")
            mostrar_horarios()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    tk.Button(frame_conteudo, text="Cadastrar", bg="navy", fg="white", font=("Arial", 11), width=20, command=confirmar).pack(pady=15)
    tk.Button(frame_conteudo, text="Voltar", font=("Arial", 10), width=20, command=mostrar_horarios).pack()

def tela_listar_horarios():
    limpar_conteudo()
    titulo_conteudo("Lista de Horários")
    frame_lista = tk.Frame(frame_conteudo, bg="white")
    frame_lista.pack(fill="both", expand=True, padx=20)
    try:
        from banco import conectar
        conexao, cursor = conectar()
        cursor.execute("SELECT * FROM horario")
        horarios = cursor.fetchall()
        conexao.close()
        if not horarios:
            tk.Label(frame_lista, text="Nenhum horário cadastrado.", bg="white", font=("Arial", 11)).pack(pady=20)
        else:
            for h in horarios:
                frame_h = tk.Frame(frame_lista, bg="#f0f0f0", pady=8, padx=10)
                frame_h.pack(fill="x", pady=5)
                tk.Label(frame_h, text=f"ID: {h[0]}  |  Dia: {h[1]}  |  Início: {h[2]}  |  Fim: {h[3]}", bg="#f0f0f0", font=("Arial", 10)).pack(anchor="w")
    except Exception as e:
        messagebox.showerror("Erro", str(e))
    tk.Button(frame_conteudo, text="Voltar", font=("Arial", 10), width=20, command=mostrar_horarios).pack(pady=10)

def tela_excluir_horario():
    limpar_conteudo()
    titulo_conteudo("Excluir Horário")
    tk.Label(frame_conteudo, text="ID do Horário", bg="white", font=("Arial", 11)).pack()
    entry_id = tk.Entry(frame_conteudo, width=40, font=("Arial", 11))
    entry_id.pack(pady=5)

    def confirmar():
        id_horario = entry_id.get()
        if messagebox.askyesno("Confirmar", f"Deseja excluir o horário ID {id_horario}?"):
            try:
                from banco import conectar
                conexao, cursor = conectar()
                cursor.execute("DELETE FROM horario WHERE id = %s", (id_horario,))
                conexao.commit()
                conexao.close()
                messagebox.showinfo("Sucesso", "Horário excluído!")
                mostrar_horarios()
            except Exception as e:
                messagebox.showerror("Erro", str(e))

    tk.Button(frame_conteudo, text="Excluir", bg="red", fg="white", font=("Arial", 11), width=20, command=confirmar).pack(pady=10)
    tk.Button(frame_conteudo, text="Voltar", font=("Arial", 10), width=20, command=mostrar_horarios).pack()

def mostrar_horarios():
    limpar_conteudo()
    titulo_conteudo("Horários")
    tk.Button(frame_conteudo, text="Cadastrar Horário", width=30, font=("Arial", 11), command=tela_cadastrar_horario).pack(pady=5)
    tk.Button(frame_conteudo, text="Listar Horários", width=30, font=("Arial", 11), command=tela_listar_horarios).pack(pady=5)
    tk.Button(frame_conteudo, text="Excluir Horário", width=30, font=("Arial", 11), command=tela_excluir_horario).pack(pady=5)

# ==================== AULAS ====================

def tela_cadastrar_aula():
    limpar_conteudo()
    titulo_conteudo("Distribuir Professor em Aula")
    campos = {}
    for label in ["CPF do Professor", "Número da Turma", "ID da Disciplina", "ID do Horário"]:
        tk.Label(frame_conteudo, text=label, bg="white", font=("Arial", 11)).pack()
        entry = tk.Entry(frame_conteudo, width=40, font=("Arial", 11))
        entry.pack(pady=5)
        campos[label] = entry
    tk.Label(frame_conteudo, text="Dica: veja os IDs em Disciplinas > Listar e Horários > Listar", bg="white", font=("Arial", 9), fg="gray").pack()

    def confirmar():
        cpf = campos["CPF do Professor"].get()
        turma = campos["Número da Turma"].get()
        disciplina = campos["ID da Disciplina"].get()
        horario = campos["ID do Horário"].get()
        if not all([cpf, turma, disciplina, horario]):
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
            return
        try:
            from banco import conectar
            conexao, cursor = conectar()
            cursor.execute("SELECT * FROM aula WHERE cpf_professor = %s AND horario_id = %s", (cpf, horario))
            if cursor.fetchone():
                messagebox.showwarning("Conflito!", "Este professor já possui aula neste horário!")
                conexao.close()
                return
            cursor.execute("INSERT INTO aula (cpf_professor, numero_turma, disciplina_id, horario_id) VALUES (%s, %s, %s, %s)", (cpf, turma, disciplina, horario))
            conexao.commit()
            conexao.close()
            messagebox.showinfo("Sucesso", "Aula cadastrada com sucesso!")
            mostrar_aulas()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    tk.Button(frame_conteudo, text="Confirmar", bg="navy", fg="white", font=("Arial", 11), width=20, command=confirmar).pack(pady=15)
    tk.Button(frame_conteudo, text="Voltar", font=("Arial", 10), width=20, command=mostrar_aulas).pack()

def tela_listar_aulas():
    limpar_conteudo()
    titulo_conteudo("Grade de Aulas")
    frame_lista = tk.Frame(frame_conteudo, bg="white")
    frame_lista.pack(fill="both", expand=True, padx=20)
    try:
        from banco import conectar
        conexao, cursor = conectar()
        cursor.execute("""
            SELECT p.nome, t.numero_turma, d.nome, h.dia_semana, h.hora_inicio, h.hora_fim
            FROM aula a
            JOIN professores p ON a.cpf_professor = p.cpf
            JOIN turmas t ON a.numero_turma = t.numero_turma
            JOIN disciplinas d ON a.disciplina_id = d.id
            JOIN horario h ON a.horario_id = h.id
            ORDER BY h.dia_semana, h.hora_inicio
        """)
        aulas = cursor.fetchall()
        conexao.close()
        if not aulas:
            tk.Label(frame_lista, text="Nenhuma aula cadastrada.", bg="white", font=("Arial", 11)).pack(pady=20)
        else:
            for a in aulas:
                frame_a = tk.Frame(frame_lista, bg="#f0f0f0", pady=8, padx=10)
                frame_a.pack(fill="x", pady=5)
                tk.Label(frame_a, text=f"Professor: {a[0]}  |  Turma: {a[1]}  |  Disciplina: {a[2]}  |  {a[3]} {a[4]}-{a[5]}", bg="#f0f0f0", font=("Arial", 10)).pack(anchor="w")
    except Exception as e:
        messagebox.showerror("Erro", str(e))
    tk.Button(frame_conteudo, text="Voltar", font=("Arial", 10), width=20, command=mostrar_aulas).pack(pady=10)

def mostrar_aulas():
    limpar_conteudo()
    titulo_conteudo("Aulas")
    tk.Button(frame_conteudo, text="Distribuir Professor em Aula", width=30, font=("Arial", 11), command=tela_cadastrar_aula).pack(pady=5)
    tk.Button(frame_conteudo, text="Ver Grade de Aulas", width=30, font=("Arial", 11), command=tela_listar_aulas).pack(pady=5)

# ==================== BOTÕES DO MENU ====================

tk.Button(frame_menu, text="Alunos", width=20, font=("Arial", 11), command=mostrar_alunos).pack(pady=5)
tk.Button(frame_menu, text="Professores", width=20, font=("Arial", 11), command=mostrar_professores).pack(pady=5)
tk.Button(frame_menu, text="Turmas", width=20, font=("Arial", 11), command=mostrar_turmas).pack(pady=5)
tk.Button(frame_menu, text="Disciplinas", width=20, font=("Arial", 11), command=mostrar_disciplinas).pack(pady=5)
tk.Button(frame_menu, text="Matrículas", width=20, font=("Arial", 11), command=mostrar_matriculas).pack(pady=5)
tk.Button(frame_menu, text="Horários", width=20, font=("Arial", 11), command=mostrar_horarios).pack(pady=5)
tk.Button(frame_menu, text="Aulas", width=20, font=("Arial", 11), command=mostrar_aulas).pack(pady=5)

janela.mainloop()