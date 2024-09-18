import  tkinter as tk
from tkinter import simpledialog, messagebox

# configuração basica da interface grafica
root = tk.Tk ()
root.withdraw()  # esconde a janela principal

# exemplo de uso
messagebox.showinfo("boas vindas","olá mundo!")
nomedigitado = simpledialog.askstring("identificação","qual o seu nome?")
nomesobrenome = simpledialog.askstring("identificação","qual o seu sobrenome?")
messagebox.showinfo("tchau"f"seu nome é{nomedigitado}{nomesobrenome}")

