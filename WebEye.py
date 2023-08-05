import requests
import re
import tkinter as tk
from tkinter import messagebox

def scan_for_sql_injection(url):
    response = requests.get(url)
    if re.search(r"Error de sintaxis en la consulta", response.text):
        return "Se encontró una posible inyección SQL en la URL: " + url
    else:
        return "No se encontraron inyecciones SQL en la URL: " + url

def scan_for_xss(url):
    response = requests.get(url)
    if re.search(r"<script>", response.text):
        xss_type = "Reflected"
        if re.search(r"<script>.*</script>", response.text):
            xss_type = "Persistent"
        elif re.search(r"document\.cookie", response.text):
            xss_type = "DOM-based"
        return f"Se encontró una posible vulnerabilidad XSS {xss_type} en la URL: {url}"
    else:
        return "No se encontraron vulnerabilidades XSS en la URL: " + url

def scan_for_open_directories(url):
    response = requests.get(url)
    if response.status_code == 200:
        if url.endswith('/'):
            url = url[:-1]
        directory_listing_url = url + '/'
        response = requests.get(directory_listing_url)
        if re.search(r"<title>Index of", response.text):
            return "El directorio está abierto y se pueden ver los archivos en la URL: " + directory_listing_url
        else:
            return "El directorio no está abierto en la URL: " + directory_listing_url
    else:
        return "No se pudo acceder al sitio web. Verifique la URL o la disponibilidad del sitio."

def scan_website():
    url = entry_url.get()
    if not url:
        messagebox.showerror("Error", "Ingrese una URL válida.")
        return

    results = []
    results.append(scan_for_sql_injection(url))
    results.append(scan_for_xss(url))
    results.append(scan_for_open_directories(url))
    result_text = "\n\n".join(results)
    lbl_result.config(text=result_text)

def change_cursor(cursor):
    root.config(cursor=cursor)

# Crear la interfaz gráfica
root = tk.Tk()
root.title("WebEye - Herramienta de Análisis de Vulnerabilidades")
root.configure(bg='black')  # Fondo negro

frame = tk.Frame(root, bg='black')
frame.pack(padx=20, pady=20)

lbl_url = tk.Label(frame, text="Ingrese la URL del sitio web:", bg='black', fg='white')  # Texto en blanco
lbl_url.pack()

entry_url = tk.Entry(frame, width=40)
entry_url.pack()

btn_scan = tk.Button(frame, text="SCAN", command=scan_website, bg='#22B14C', fg='black')  # Verde alien
btn_scan.pack()

lbl_result = tk.Label(frame, text="", wraplength=400, justify="left", bg='black', fg='white')  # Texto en blanco
lbl_result.pack()

# Texto de créditos del creador
credit_label = tk.Label(frame, text="Developed by @dfarpy", bg='black', fg='white')  # Texto en blanco
credit_label.pack()

root.mainloop()
