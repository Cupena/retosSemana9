#Practica de diccionario

import errores
solicitudes = []

def registrar_nombre():
    nombre_cliente = input("Ingrese su nombre: ").strip()
    return f"Su nombre {nombre_cliente} se ha registrado exitosamente."

def registrar_distrito():
    while True:
            try:
                distrito = int(input("Ingrese su sector: "))
                break
            except ValueError:
                print(errores.error_generico())
    while True:

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
    
def registrar_asunto():
    asunto = input("Ingrese su problema: \n- ")
    return "Problema agregado."


def registrar_solicitud():
    print(registrar_nombre())

    

            
    solicitud = {
    "Nombre" : nombre,
    "Sector" : distrito


    }

