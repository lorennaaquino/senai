import tkinter as tk
from tkinter import messagebox

def mensagem():
    messagebox.showinfo("teste",f"({entrynome.get()};tel: {entrytelefone.get()}")
                                  

janela = tk.Tk()
janela.title("cadastro de cliente")

#cadastro do nome do cliente
labelnome = tk.Label(janela,text="nome")
labelnome.pack(padx=50, pady=5)

entrynome = tk.Entry(janela)
entrynome.pack(padx=50, pady=5)

#***cadastro do telefone do cliente

labeltelefone = tk.Label(janela,text="telefone")
labeltelefone.pack(padx=50, pady=5)

entrytelefone = tk.Entry(janela)
entrytelefone.pack(padx=50, pady=5)

#cadastro do email do cliente 
labelemail = tk.Label(janela, text="email")
labelemail.pack(padx=50, pady=5)

entryemail = tk.Entry(janela, width=100)
entryemail.pack(padx=50, pady=5)

buttonsalvar = tk.Button(janela,text="salvar",command=mensagem)
buttonsalvar.pack(padx=50, pady=5)

janela.geometry("400x300")
janela.mainloop()

