import tkinter as tk
from tkinter import messagebox

def calcular():
    quantidade = float(entryquantidade.get())
    preco = float(entryepreço.get())
    total = quantidade * preco
    labelValor.config(text=f"R$ {total:.2f}")                                

janela = tk.Tk()
janela.title("sistema irango")

#cadastro do lanche do cliente
labellanche = tk.Label(janela,text="Lanche")
labellanche.pack(padx=50, pady=5)

entrylanche = tk.Entry(janela)
entrylanche.pack(padx=50, pady=5)

#***cadastro do quantidade do cliente

labelquantidade = tk.Label(janela,text="Quantidade")
labelquantidade.pack(padx=50, pady=5)

entryquantidade = tk.Entry(janela)
entryquantidade.pack(padx=50, pady=5)

#cadastro do preço do cliente 
labelpreço = tk.Label(janela, text="Preço")
labelpreço.pack(padx=50, pady=5)

entryepreço = tk.Entry(janela, width=100)
entryepreço.pack(padx=50, pady=5)

#cadastro do preço do cliente 
labelTotal = tk.Label(janela, text="Total")
labelTotal.pack(padx=50, pady=5)

labelValor = tk.Label(janela, text="R$ 0.00")
labelValor.pack(padx=50, pady=5)


buttonsalvar = tk.Button(janela,text="Calcular", command=calcular)
buttonsalvar.pack(padx=50, pady=5)

janela.geometry("400x300")
janela.mainloop()

