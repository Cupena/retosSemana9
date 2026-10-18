#Practica de diccionario

import errores
solicitudes = []

def registrar_asunto(asunto):
    asunto = input("Ingrese su problema: \n- ")
    return "Problema agregado."

def registrar_solicitud():
    nombre = input("Ingrese su nombre: ").strip()
    
    while True:
        try:
            distrito = int(input("Ingrese su sector: "))
            break
        except ValueError:
            print(errores.error_generico())
    while True:
        print(registrar_asunto())

        while True:
            try:
                op = int(input("Desea seguir agregando asuntos? (1. Si / 2. No)"))
            except ValueError:
                print(errores.error_generico())

            if op ==1:
                registrar_asunto()
            elif op ==2:
                break
            else:
                print(errores.error_generico())

            
    solicitud = {
    "Nombre" : nombre,
    "Sector" : distrito


    }

