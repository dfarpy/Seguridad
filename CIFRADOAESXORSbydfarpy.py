import pyAesCrypt
from os import stat, path

print("***************************************************************************")
print("\t \t \t MENU")
print("***************************************************************************")
print("\t \t 1. Cifrado y Descifrado con XOR")
print("\t \t 2. Cifrado y Descifrado con AES")
print("***************************************************************************")
a = int(input("Ingrese su elección: "))

if a == 1:
    print("*************************************")
    print("1. Presione 1 para cifrar")
    print("2. Presione 2 para descifrar")
    b = int(input("Ingrese su elección: "))

    if b == 1:
        try:
            ruta_archivo = input("Ingrese la ruta del archivo a cifrar: ")
            clave = int(input('Ingrese la clave para el cifrado: '))

            print('Ruta del archivo: ', ruta_archivo)
            print('Clave de cifrado: ', clave)

            with open(ruta_archivo, 'rb') as archivo_entrada:
                datos = bytearray(archivo_entrada.read())

            for index, valor in enumerate(datos):
                datos[index] = valor ^ clave

            with open(ruta_archivo, 'wb') as archivo_salida:
                archivo_salida.write(datos)

            print('Cifrado completado...')

        except Exception as e:
            print('Error: ', e)

    elif b == 2:
        try:
            ruta_archivo = input("Ingrese la ruta del archivo a descifrar: ")
            clave = int(input('Ingrese la clave para el descifrado: '))

            print('Ruta del archivo: ', ruta_archivo)
            print('Nota: La clave de cifrado y descifrado deben ser iguales.')
            print('Clave de descifrado: ', clave)

            with open(ruta_archivo, 'rb') as archivo_entrada:
                datos = bytearray(archivo_entrada.read())

            for index, valor in enumerate(datos):
                datos[index] = valor ^ clave

            nombre_archivo = path.basename(ruta_archivo)
            ruta_salida = path.dirname(ruta_archivo)
            ruta_descifrado = path.join(ruta_salida, nombre_archivo)

            with open(ruta_descifrado, 'wb') as archivo_salida:
                archivo_salida.write(datos)

            print('Descifrado completado...')

        except Exception as e:
            print('Error: ', e)

    else:
        print("Por favor, ingrese una opción válida")

elif a == 2:
    print("**********************************************************************************************")
    print("1. Cifrado")
    print("2. Descifrado")
    print("##############################################################################################")
    h = int(input("Ingrese su elección: "))
    ruta_archivo = input("Ingrese la ubicación del archivo con su extensión: ")
    bufferSize = 64 * 1024
    password = input("Ingrese la contraseña: ")

    if h == 1:
        try:
            ruta_salida = input("Ingrese la ruta de salida para el archivo cifrado: ")
            nombre_archivo = path.basename(ruta_archivo)
            ruta_cifrado = path.join(ruta_salida, nombre_archivo + ".aes")

            with open(ruta_archivo, "rb") as archivo_entrada:
                with open(ruta_cifrado, "wb") as archivo_salida:
                    pyAesCrypt.encryptStream(archivo_entrada, archivo_salida, password, bufferSize)
            print("Cifrado completado")

        except Exception as e:
            print('Error: ', e)

    elif h == 2:
        try:
            with open(ruta_archivo, "rb") as archivo_entrada:
                nombre_archivo = path.splitext(ruta_archivo)[0]
                with open(nombre_archivo, "wb") as archivo_salida:
                    encFileSize = stat(ruta_archivo).st_size
                    pyAesCrypt.decryptStream(archivo_entrada, archivo_salida, password, bufferSize, encFileSize)
            print("Descifrado completado")

        except Exception as e:
            print('Error: ', e)

else:
    print("Por favor, ingrese una opción válida")
