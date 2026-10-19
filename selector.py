#Modulo para elegir que hacer

import errores, catalogo,registro

solicitudes = []
id = 0000

def selector_opcion():
    
    while True:
        try:
            print(catalogo.menu())
            op = int(input("\nIngrese la opcion a tomar: "))
        except ValueError:
            print(errores.error_generico())

        if op == 1:
            nombre = registro.registrar_nombre()
            distrito = registro.registrar_distrito()
            asunto = registro.registrar_asunto()
            registro.registrar_solicitud(nombre, distrito, asunto, solicitudes)
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
        if op ==2:
            pass
        if op ==2:
            pass
        if op ==3:
            break
        else:
            print(errores.error_opcion())


