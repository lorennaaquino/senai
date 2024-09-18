import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime
import os

# Caminho para o arquivo JSON onde os chamados serão armazenados
CHAMADOS_FILE = 'chamados.json'

# Função para carregar o último número de chamado do arquivo JSON
def carregar_ultimo_numero():
    if os.path.exists(CHAMADOS_FILE):
        with open(CHAMADOS_FILE, 'r') as file:
            chamados = json.load(file)
            if chamados:
                return max(chamado['numero_chamado'] for chamado in chamados)
    return 0

# Função para salvar os chamados no arquivo JSON
def salvar_chamados(chamados):
    with open(CHAMADOS_FILE, 'w') as file:
        json.dump(chamados, file, indent=4)

# Função para criar um novo chamado
def novo_chamado():
    global numero_chamado_atual
    numero_chamado_atual += 1
    campo_numero_chamado.config(text=str(numero_chamado_atual))
    campo_nome_cliente.delete(0, tk.END)
    campo_tipo_problema.set('')
    campo_descricao.delete('1.0', tk.END)
    campo_prioridade.set('')
    campo_data_abertura.config(text=datetime.now().strftime("%Y-%m-%d"))

# Função para localizar um chamado pelo número
def localizar_chamado():
    numero_chamado = campo_localizar_numero.get()
    if not numero_chamado.isdigit():
        messagebox.showerror("Erro", "O número do chamado deve ser numérico.")
        return
    
    numero_chamado = int(numero_chamado)
    if os.path.exists(CHAMADOS_FILE):
        with open(CHAMADOS_FILE, 'r') as file:
            chamados = json.load(file)
            for chamado in chamados:
                if chamado['numero_chamado'] == numero_chamado:
                    campo_nome_cliente.delete(0, tk.END)
                    campo_nome_cliente.insert(0, chamado['cliente'])
                    campo_tipo_problema.set(chamado['tipo_problema'])
                    campo_descricao.delete('1.0', tk.END)
                    campo_descricao.insert('1.0', chamado['descricao'])
                    campo_prioridade.set(chamado['prioridade'])
                    campo_data_abertura.config(text=chamado['data_abertura'])
                    return
            messagebox.showerror("Erro", "Chamado não encontrado.")
    else:
        messagebox.showerror("Erro", "Nenhum chamado registrado.")

# Função para salvar o chamado atual
def salvar_chamado():
    chamado = {
        "numero_chamado": numero_chamado_atual,
        "cliente": campo_nome_cliente.get(),
        "tipo_problema": campo_tipo_problema.get(),
        "descricao": campo_descricao.get('1.0', tk.END).strip(),
        "prioridade": campo_prioridade.get(),
        "data_abertura": campo_data_abertura.cget("text")
    }

    chamados = []
    if os.path.exists(CHAMADOS_FILE):
        with open(CHAMADOS_FILE, 'r') as file:
            chamados = json.load(file)
    
    chamados.append(chamado)
    salvar_chamados(chamados)
    messagebox.showinfo("Sucesso", "Chamado salvo com sucesso.")
    novo_chamado()

# Criação da interface gráfica
root = tk.Tk()
root.title("Sistema de Registro e Consulta de Chamados")

# Dados para o combo box
tipos_problema = ["Problema de Rede", "Falha de Software", "Erro de Hardware"]
prioridades = ["Baixa", "Média", "Alta"]

# Interface
tk.Label(root, text="Nome do Cliente:").grid(row=0, column=0, padx=10, pady=5)
campo_nome_cliente = tk.Entry(root)
campo_nome_cliente.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Tipo de Problema:").grid(row=1, column=0, padx=10, pady=5)
campo_tipo_problema = ttk.Combobox(root, values=tipos_problema)
campo_tipo_problema.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Descrição do Problema:").grid(row=2, column=0, padx=10, pady=5)
campo_descricao = tk.Text(root, height=5, width=30)
campo_descricao.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Prioridade:").grid(row=3, column=0, padx=10, pady=5)
campo_prioridade = ttk.Combobox(root, values=prioridades)
campo_prioridade.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Data de Abertura:").grid(row=4, column=0, padx=10, pady=5)
campo_data_abertura = tk.Label(root, text=datetime.now().strftime("%Y-%m-%d"))
campo_data_abertura.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Número do Chamado:").grid(row=5, column=0, padx=10, pady=5)
campo_numero_chamado = tk.Label(root, text="")
campo_numero_chamado.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Localizar Chamado (Número):").grid(row=6, column=0, padx=10, pady=5)
campo_localizar_numero = tk.Entry(root)
campo_localizar_numero.grid(row=6, column=1, padx=10, pady=5)

# Botões
btn_novo_chamado = tk.Button(root, text="Novo Chamado", command=novo_chamado)
btn_novo_chamado.grid(row=7, column=0, padx=10, pady=5)

btn_localizar_chamado = tk.Button(root, text="Localizar Chamado", command=localizar_chamado)
btn_localizar_chamado.grid(row=7, column=1, padx=10, pady=5)

btn_salvar_chamado = tk.Button(root, text="Salvar Chamado", command=salvar_chamado)
btn_salvar_chamado.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

# Configuração inicial
numero_chamado_atual = carregar_ultimo_numero()
campo_numero_chamado.config(text=str(numero_chamado_atual))

# Iniciar a interface gráfica
novo_chamado()
root.mainloop()
