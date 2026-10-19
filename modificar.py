#Modificar la lista

def evaluar_cero(solicitudes):
    return len(solicitudes) == 0

def revertir_ultimo_diccionario(solicitudes):
    if evaluar_cero(solicitudes):
        return "No hay solicitudes por eliminar."
    else:
        solicitudes.pop()
    return "Ultimo diccionario revertido exitosamente."




    

