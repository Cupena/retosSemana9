#Practica de diccionario

import errores
solicitudes = []

def registrar_solicitud():
    nombre = input("Ingrese su nombre: ")
    
    while True:
        try:
            distrito = int(input("Ingrese su sector: "))
        except ValueError:
            print(errores.error_generico())

    ubicacion = input("En que sector esta ubicado: ")

    solicitud = {
    "Nombre" : nombre,
    "Sector" : distrito

    }

