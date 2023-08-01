import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import secrets
import string

# Función para generar una contraseña segura
def generar_contraseña_segura(longitud):
    alfabeto = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(secrets.choice(alfabeto) for _ in range(longitud))
    return contraseña

# Función para generar la contraseña y mostrarla en un cuadro de diálogo
def generar_contraseña():
    longitud = int(var_longitud.get())
    contraseña = generar_contraseña_segura(longitud)
    messagebox.showinfo("Contraseña generada", f"Contraseña generada: {contraseña}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("GENERADOR DE CONTRASEÑAS")
ventana.geometry("300x250")
ventana.configure(bg="#000000")

# Estilo personalizado para los widgets
estilo = ttk.Style(ventana)
estilo.configure("TLabel", background="#000000", foreground="#FFDC00", font=("PixelOperator8", 16))
estilo.configure("TButton", background="#1E1E1E", foreground="#000000", font=("PixelOperator8", 14), padding=5, relief="flat")

# Encabezado
etiqueta_encabezado = tk.Label(ventana, text="GENERADOR\nDE CONTRASEÑAS", font=("PixelOperator8", 16), bg="#000000", fg="#FFDC00")
etiqueta_encabezado.pack(pady=10)

# Etiqueta y opción para seleccionar la longitud de la contraseña
etiqueta_longitud = ttk.Label(ventana, text="Seleccionar longitud:")
etiqueta_longitud.pack(pady=5)

var_longitud = tk.StringVar(ventana)
var_longitud.set("6")  # Valor predeterminado

opciones_longitud = ["6", "8", "10", "12", "16"]
menu_longitud = ttk.OptionMenu(ventana, var_longitud, *opciones_longitud)
menu_longitud.pack()

# Botón para generar la contraseña
boton_generar = ttk.Button(ventana, text="Generar Contraseña segura", command=generar_contraseña)
boton_generar.pack(pady=20)
boton_generar.configure(style="TButton")

# Etiqueta de crédito
etiqueta_credito = ttk.Label(ventana, text="Desarrollado por dfarpy", font=("PixelOperator8", 8))
etiqueta_credito.pack(side=tk.BOTTOM, pady=5)

# Ejecutar la ventana
ventana.mainloop()

