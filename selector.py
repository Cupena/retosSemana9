#Modulo para elegir que hacer

import errores, catalogo,registro,modificar

solicitudes = []
solicitudes_atendidas = []
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
            registro.registrar_solicitud(id, nombre, distrito, asunto, solicitudes)

        if op ==2:
            print(modificar.revertir_ultimo_diccionario(solicitudes))

        if op ==3:
            print(modificar.mostrar_siguiente_diccionario(solicitudes))

        if op ==4:
            print(modificar.buscador_solicitudes(solicitudes))

        if op ==5:
            print(modificar.marcar_siguiente_atendido(solicitudes, solicitudes_atendidas))
        
        if op ==6:
            print(modificar.mostrar_solicitud(solicitudes))
            
        if op ==7:
            print(modificar.mostrar_solicitud(solicitudes_atendidas))
            
        if op ==8:
            print(modificar.eliminar_especifico(solicitudes))
        if op ==9:
            print(modificar.eliminar_especifico(solicitudes_atendidas))
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


