import tkinter as tk
from tkinter import ttk

#função para somar os numeros e mostrar o resultado
def somar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 + num2
        messagebox.showinfo("resultado", f"a soma é: {resultado}")
    except ValueError:
        messagebox.showerror("erro","por favor,insira numeros validos.")

# configuração da janela principal
root = tk.Tk()
root.title("soma de numeros")

#criação dos widgets
label_num1 = tk.label(root,text="digite o primeiro numero")
label_num1.pack(padx=10, pady=5)

entry_num1 = tk.entry(root)
entry_num1.pack(padx=10 ,pady=5)

label_num2 = tk.Label(root, text="digite o segundo numero:")
label_num2.pack(padx=10, pady=5)

entry_num2 = tk.Entry(root)
entry_num2.pack(padx=10, pady=5)

button_somar = tk.Button(root, text="somar",command=somar)
button_somar.pack(pady=20)

#executa o loop principal da interface gráfica 
root.mainloop

