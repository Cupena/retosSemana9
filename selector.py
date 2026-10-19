#Modulo para elegir que hacer

import errores, catalogo,registro

def selector_opcion():
    
    while True:
        try:
            print(catalogo.menu())
            op = int(input("\nIngrese la opcion a tomar: "))
        except ValueError:
            print(errores.error_generico())
        if op == 1:
            print(registro.registrar_nombre())
            print(registro.registrar_distrito())
            print(registro.registrar_asunto())
