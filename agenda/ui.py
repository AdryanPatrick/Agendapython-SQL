import tkinter as tk
from tkinter import messagebox
from .models import adicionar_compromisso, listar_compromissos

def adicionar():
    data = entry_data.get()
    hora = entry_hora.get()
    descricao = entry_descricao.get()

    if not data or not hora or not descricao:
        messagebox.showwarning('Erro', 'Todos os campos precisam ser preenchidos.')
        return
    
    adicionar_compromisso(data, hora, descricao)
    messagebox.showinfo('Sucesso', 'Compromisso adicionado com sucesso!')

def listar():
    compromissos = listar_compromissos()

    # Cria uma nova janela para exibir a lista de compromissos
    janela_lista = tk.Toplevel()
    janela_lista.title('Lista de Compromissos')

    if compromissos:
        for compromisso in compromissos:
            tk.Label(janela_lista, text=f"ID: {compromisso[0]} | Data: {compromisso[1]} | Hora: {compromisso[2]} | Descrição: {compromisso[3]}").pack()
    else:
        tk.Label(janela_lista, text="Nenhum compromisso encontrado.").pack()

def criar_interface():
    root = tk.Tk()
    root.title('Agenda de Compromissos')

    tk.Label(root, text='Data (YYYY-MM-DD)').pack()
    global entry_data
    entry_data = tk.Entry(root)
    entry_data.pack()

    tk.Label(root, text='Hora (HH:MM)').pack()
    global entry_hora
    entry_hora = tk.Entry(root)
    entry_hora.pack()

    tk.Label(root, text='Descrição').pack()
    global entry_descricao
    entry_descricao = tk.Entry(root)
    entry_descricao.pack()

    # Botão para adicionar compromisso
    tk.Button(root, text='Adicionar Compromisso', command=adicionar).pack()

    # Botão para listar compromissos
    tk.Button(root, text='Ver Compromissos', command=listar).pack()

    root.mainloop()
