#Modificar la lista

import errores

def evaluar_cero(solicitudes):
    return len(solicitudes) == 0

def revertir_ultimo_diccionario(solicitudes):
    if evaluar_cero(solicitudes):
        return "No hay solicitudes por eliminar."
    else:
        solicitudes.pop()
    return "Ultimo diccionario revertido exitosamente."

def mostrar_siguiente_diccionario(solicitudes):
    if evaluar_cero(solicitudes):
        return "No hay diccionario registrado."
    else:
        return solicitudes[-1]

def pedir_solicitud_id(solicitudes):
    if evaluar_cero(solicitudes):
        return "No hay solicitud por buscar."
    else:
        while True:
            try:
                id_solicitado = int(input("Digite el id a seleccionar: "))
                return id_solicitado
            except ValueError:
                print(errores.error_generico())


def buscador_solicitudes(solicitudes):
    id_buscado = pedir_solicitud_id(solicitudes)

    for solicitud in solicitudes:
        if solicitud["ID"] == id_buscado:
            return solicitud
        else:
            return "No se ha registrado ese ID."







    

