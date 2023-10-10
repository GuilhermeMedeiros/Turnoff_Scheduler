import tkinter as tk
import os

def shutdown():
    try:
        tempo = entry.get()
        temp = int(tempo) * 60 
        os.system("shutdown /s /t %s" % temp)
        label.config(text="Tempo de desligamento configurado!")
    except ValueError:
        label.config(text="Erro: O valor inserido não é um número.")
    except Exception as e:
        label.config(text="Algo deu errado, erro: " + str(e))

def cancel_shutdown():
    os.system("shutdown /a")
    label.config(text="Desligamento cancelado!")

root = tk.Tk()
root.geometry("350x170")
root.title("Configurador de Desligamento")
label = tk.Label(root, text="Bem vindo ao configurador de desligamento!")
label.pack()
label = tk.Label(root, text="Informe o tempo para desligar o PC em minutos:")
label.pack()

entry = tk.Entry(root)
entry.pack(pady=10)  # Add vertical padding

button_shutdown = tk.Button(root, text="Agendar Desligamento", command=shutdown)
button_shutdown.pack(pady=5)  # Add vertical padding
label = tk.Label(root, text="Voce também pode cancelar o desligamento:")
label.pack()
button_cancel = tk.Button(root, text="Cancelar Desligamento", command=cancel_shutdown)
button_cancel.pack(pady=5)  # Add vertical padding

root.mainloop()
