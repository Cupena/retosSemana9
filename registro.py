#Modulo de Registro

import errores

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

    
def registrar_asunto():
    asunto = input("Ingrese su problema: \n- ")
    return "Problema agregado."


def registrar_solicitud(nombre, distrito, asunto,solicitudes):
    solicitud = {
        "Nombre" : nombre,
        "Sector" : distrito,
        "Problema": asunto
        }
    solicitudes.append(solicitud)
    
