import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import secrets
import string

def generate_secure_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def generate_password():
    length = int(length_var.get())
    password = generate_secure_password(length)
    messagebox.showinfo("Contraseña generada", f"Contraseña generada: {password}")

# Crear la ventana principal
window = tk.Tk()
window.title("PASSWORD GENERATOR")
window.geometry("300x250")
window.configure(bg="#000000")

# Estilo personalizado para los widgets
style = ttk.Style(window)
style.configure("TLabel", background="#000000", foreground="#FFDC00", font=("PixelOperator8", 16))
style.configure("TButton",
                background="#1E1E1E",
                foreground="#000000",
                font=("PixelOperator8", 14),
                padding=5,
                relief="flat")

# Encabezado
header_label = tk.Label(window, text="PASSWORD\nGENERATOR", font=("PixelOperator8", 16), bg="#000000", fg="#FFDC00")
header_label.pack(pady=10)

# Etiqueta y opción para seleccionar la longitud
length_label = ttk.Label(window, text="Seleccionar longitud:")
length_label.pack(pady=5)

length_var = tk.StringVar(window)
length_var.set("6")  # Valor predeterminado

length_options = ["6", "8", "10", "12", "16"]
length_menu = ttk.OptionMenu(window, length_var, *length_options)
length_menu.pack()

# Botón para generar la contraseña
generate_button = ttk.Button(window, text="Generar Clave segura", command=generate_password)
generate_button.pack(pady=20)
generate_button.configure(style="TButton")

# Etiqueta de crédito
credit_label = ttk.Label(window, text="Desarrollado por dfarpy", font=("PixelOperator8", 8))
credit_label.pack(side=tk.BOTTOM, pady=5)

# Ejecutar la ventana
window.mainloop()
