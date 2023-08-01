# Importar módulos necesarios
import pyAesCrypt
from os import stat, path

# Aqui mostramos el menú principal
print("***************************************************************************")
print("\t \t \t MENU")
print("***************************************************************************")
print("\t \t 1. Cifrado y Descifrado con XOR")
print("\t \t 2. Cifrado y Descifrado con AES")
print("***************************************************************************")
# Pedimos al usuario que ingrese una opción
a = int(input("Ingrese su elección: "))

# Opción 1: Cifrado y Descifrado con XOR
if a == 1:
    print("*************************************")
    print("1. Presione 1 para cifrar")
    print("2. Presione 2 para descifrar")
    # Pedir al usuario que ingrese otra opción
    b = int(input("Ingrese su elección: "))

    # Opción 1.1: Cifrado con XOR
    if b == 1:
        try:
            # Pedimos la ruta del archivo y la clave de cifrado
            ruta_archivo = input("Ingrese la ruta del archivo a cifrar: ")
            clave = int(input('Ingrese la clave para el cifrado: '))

            print('Ruta del archivo: ', ruta_archivo)
            print('Clave de cifrado: ', clave)

            # Leer el archivo y guardar su contenido en una variable
            with open(ruta_archivo, 'rb') as archivo_entrada:
                datos = bytearray(archivo_entrada.read())

            # Aplicamos el cifrado XOR a cada byte del archivo
            for index, valor in enumerate(datos):
                datos[index] = valor ^ clave

            # Escribimos el archivo cifrado
            with open(ruta_archivo, 'wb') as archivo_salida:
                archivo_salida.write(datos)

            print('Cifrado completado...')

        except Exception as e:
            print('Error: ', e)

    # Opción 1.2: Descifrado con XOR
    elif b == 2:
        try:
            # Pedimos la ruta del archivo y la clave de descifrado
            ruta_archivo = input("Ingrese la ruta del archivo a descifrar: ")
            clave = int(input('Ingrese la clave para el descifrado: '))

            print('Ruta del archivo: ', ruta_archivo)
            print('Nota: La clave de cifrado y descifrado deben ser iguales.')
            print('Clave de descifrado: ', clave)

            # Lee el archivo cifrado y guardar su contenido en una variable
            with open(ruta_archivo, 'rb') as archivo_entrada:
                datos = bytearray(archivo_entrada.read())

            # Aplicamos descifrado con  XOR a cada byte del archivo (es el mismo proceso que el cifrado)
            for index, valor in enumerate(datos):
                datos[index] = valor ^ clave

            # Obtenemos el nombre del archivo y la ruta de salida para el archivo descifrado
            nombre_archivo = path.basename(ruta_archivo)
            ruta_salida = path.dirname(ruta_archivo)
            ruta_descifrado = path.join(ruta_salida, nombre_archivo)

            # Escribimos el archivo descifrado
            with open(ruta_descifrado, 'wb') as archivo_salida:
                archivo_salida.write(datos)

            print('Descifrado completado...')

        except Exception as e:
            print('Error: ', e)

    else:
        print("Por favor, ingrese una opción válida")

# Opción 2: Cifrado y Descifrado con AES
elif a == 2:
    print("**********************************************************************************************")
    print("1. Cifrado")
    print("2. Descifrado")
    print("##############################################################################################")
    # Pedimos al usuario que ingrese otra opción
    h = int(input("Ingrese su elección: "))
    # Pedimos al usuario la ruta del archivo, el tamaño del buffer y la contraseña
    ruta_archivo = input("Ingrese la ubicación del archivo con su extensión: ")
    bufferSize = 64 * 1024
    password = input("Ingrese la contraseña: ")

    # Opción 2.1: Cifrado con AES
    if h == 1:
        try:
            # Pedimos la ruta de salida para el archivo cifrado
            ruta_salida = input("Ingrese la ruta de salida para el archivo cifrado: ")
            # Obtenenemos el nombre del archivo y la ruta de salida para el archivo cifrado
            nombre_archivo = path.basename(ruta_archivo)
            ruta_cifrado = path.join(ruta_salida, nombre_archivo + ".aes")

            # Ciframos el archivo utilizando el algoritmo AES
            with open(ruta_archivo, "rb") as archivo_entrada:
                with open(ruta_cifrado, "wb") as archivo_salida:
                    pyAesCrypt.encryptStream(archivo_entrada, archivo_salida, password, bufferSize)
            print("Cifrado completado")

        except Exception as e:
            print('Error: ', e)

    # Opción 2.2: Descifrado con AES
    elif h == 2:
        try:
            # Obtenenemos el nombre del archivo sin extensión para el archivo descifrado
            nombre_archivo = path.splitext(ruta_archivo)[0]
            # Creamos la ruta de salida para el archivo descifrado
            with open(nombre_archivo, "wb") as archivo_salida:
                # Obtenemos el tamaño del archivo cifrado
                encFileSize = stat(ruta_archivo).st_size
                # Desciframos el archivo utilizando el algoritmo AES
                with open(ruta_archivo, "rb") as archivo_entrada:
                    pyAesCrypt.decryptStream(archivo_entrada, archivo_salida, password, bufferSize, encFileSize)
            print("Descifrado completado")

        except Exception as e:
            print('Error: ', e)

else:
    print("Por favor, ingrese una opción válida")
