#Modulo para elegir que hacer

import errores, catalogo,registro,modificar

solicitudes = []
id_solicitud = 0000

def selector_opcion():
    
    while True:
        try:
            print(catalogo.menu())
            op = int(input("\nIngrese la opcion a tomar: "))
        except ValueError:
            print(errores.error_generico())

        if op == 1:
            id = registro.registrar_id(id_solicitud)
            nombre = registro.registrar_nombre()
            distrito = registro.registrar_distrito()
            asunto = registro.registrar_asunto()
            estado = "Pendiente"
            registro.registrar_solicitud(id, nombre, distrito, asunto, estado, solicitudes)
        if op ==2:
            print(modificar.revertir_ultimo_diccionario(solicitudes))
        if op ==3:
            print(modificar.mostrar_siguiente_diccionario(solicitudes))
        if op ==2:
            pass
        if op ==2:
            pass
        if op ==2:
            pass
        if op ==2:
            pass
        if op ==2:
            pass
        if op ==2:
            pass
        if op ==2:
            pass
        if op ==2:
            pass
        if op ==2:
            pass
        if op ==0:
            print("Se ha cerrado el programa exitosamente.")
            break
        else:
            print(errores.error_opcion())


