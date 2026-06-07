import tkinter as tk

janela = tk.Tk()
janela.title("Sistema Acadêmico")
janela.geometry("800x600")

label = tk.Label(janela, text="Sistema Academico")
label.pack()

def clicar():
    label.config(text="Você clicou! ")

botao = tk.Button(janela, text="Clique aqui", command=clicar)
botao.pack()

janela.mainloop()