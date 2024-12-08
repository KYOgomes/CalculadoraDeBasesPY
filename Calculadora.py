import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

# Função de conversão
def converter():
    try:
        input_value = entry.get()
        base_origem = combo_base.get()
        
        if base_origem == "BINÁRIO":
            numero = int(input_value, 2)
        elif base_origem == "OCTAL":
            numero = int(input_value, 8)
        elif base_origem == "DECIMAL":
            numero = int(input_value)
        elif base_origem == "HEXADECIMAL":
            numero = int(input_value, 16)
        else:
            messagebox.showerror("Erro", "Escolha uma base de origem válida!")
            return

        # Atualiza os resultados
        resultado_binario.set(bin(numero)[2:])
        resultado_octal.set(oct(numero)[2:])
        resultado_decimal.set(str(numero))
        resultado_hexadecimal.set(hex(numero)[2:].upper())
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida! Insira um número correto para a base escolhida.")

# Função para gerar um número aleatório em uma base aleatória
def gerar_aleatorio():
    bases = ["BINÁRIO", "OCTAL", "DECIMAL", "HEXADECIMAL"]
    base_escolhida = random.choice(bases)
    combo_base.set(base_escolhida)  # Seleciona a base no combobox
    
    # Gera um número aleatório com base no intervalo apropriado para cada base
    if base_escolhida == "BINÁRIO":
        numero = bin(random.randint(1, 255))[2:]  # Número binário (máx. 8 bits)
    elif base_escolhida == "OCTAL":
        numero = oct(random.randint(1, 255))[2:]  # Número octal
    elif base_escolhida == "DECIMAL":
        numero = str(random.randint(1, 255))  # Número decimal
    elif base_escolhida == "HEXADECIMAL":
        numero = hex(random.randint(1, 255))[2:].upper()  # Número hexadecimal

    entry.delete(0, tk.END)  # Limpa o campo de entrada
    entry.insert(0, numero)  # Insere o número gerado
    converter()  # Converte o número gerado automaticamente

# Janela principal
root = tk.Tk()
root.title("Conversor de Base Numérica")
root.geometry("400x350")
root.resizable(False, False)

# Estilo
style = ttk.Style()
style.theme_use('clam')
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TLabel", font=("Arial", 12))
style.configure("TCombobox", font=("Arial", 12))

#Cabeçalho
header = tk.Label(root, text="Conversor de base numérica", bg="#F5DEB3", fg="black", font=("Impact", 16, "bold"))
header.pack(fill=tk.X)


# Seletor de base e entrada de número
frame_top = tk.Frame(root, pady=10)
frame_top.pack()

combo_base = ttk.Combobox(frame_top, values=["BINÁRIO", "OCTAL", "DECIMAL", "HEXADECIMAL"], state="readonly")
combo_base.set("Escolha a base")
combo_base.pack(side=tk.LEFT, padx=5)

entry = ttk.Entry(frame_top, width=20)
entry.pack(side=tk.LEFT, padx=5)

btn_converter = ttk.Button(frame_top, text="CONVERTER", command=converter)
btn_converter.pack(side=tk.LEFT, padx=5)

# Botão para gerar número aleatório
btn_aleatorio = ttk.Button(root, text="GERAR ALEATÓRIO", command=gerar_aleatorio)
btn_aleatorio.pack(pady=10)

# Resultados
frame_results = tk.Frame(root, pady=10)
frame_results.pack()

resultado_binario = tk.StringVar()
resultado_octal = tk.StringVar()
resultado_decimal = tk.StringVar()
resultado_hexadecimal = tk.StringVar()

def criar_linha(base, var_resultado):
    frame = tk.Frame(frame_results)
    frame.pack(fill=tk.X, pady=5)
    label = ttk.Label(frame, text=base, width=15, anchor="w", background="#7FA6C8", foreground="white")
    label.pack(side=tk.LEFT, padx=5, fill=tk.X)
    result = ttk.Label(frame, textvariable=var_resultado, anchor="w", background="white")
    result.pack(side=tk.LEFT, fill=tk.X, expand=True)

criar_linha("BINÁRIO", resultado_binario)
criar_linha("OCTAL", resultado_octal)
criar_linha("DECIMAL", resultado_decimal)
criar_linha("HEXADECIMAL", resultado_hexadecimal)

# Rodar o app
root.mainloop()
