#Modulo de Registro
import errores

def id_problema(ultimo_id):
    ultimo_id += 1
    return ultimo_id

def registrar_nombre():
    while True:
        nombre_cliente = input("Ingrese su nombre: ").strip()
        if nombre_cliente:
            return nombre_cliente
        else:
            print("Ingresa un nombre valido.") 

def registrar_distrito():
    while True:
            try:
                distrito = int(input("Ingrese su sector: "))
                return distrito
            except ValueError:
                print(errores.error_generico())

    
def registrar_asunto():
    while True:
        asunto = input("Ingrese su problema: \n- ").strip
        if asunto:
            return asunto
        else:
            print("Ingrese un problema valido.")


def registrar_solicitud(id_problema,nombre, distrito, asunto,solicitudes):
    solicitud = {
        "ID" : id_problema,
        "Nombre" : nombre,
        "Sector" : distrito,
        "Problema": asunto
        }
    return solicitudes.append(solicitud)
    
    
