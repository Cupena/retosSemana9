import clientes, listos, listas, errores, catalogo

def selector_opcion(pendientes, atendidos):
    while True:
        print(catalogo.menu())
        try:
            op = int(input("Ingrese su opcion a realizar: "))
        except ValueError:
            print(errores.error_generico())
            continue

        if op == 1:
            print(clientes.agregar_cliente(pendientes))

        elif op == 2:
            print(listos.agregar_atendidos(atendidos, pendientes))

        elif op == 3:
            print(clientes.revertir_cliente(pendientes))

        elif op == 4:
            print(listos.revertir_atendido(pendientes, atendidos))

        elif op == 5:
            print(clientes.mover_alUltimo(pendientes))

        elif op == 6:
            print(listos.mostrar_UltAtend(atendidos))

        elif op == 7:
            print(clientes.mostrar_UltPend(pendientes))

        elif op == 8:
            print(listos.contar_atendidos(atendidos))

        elif op == 9:
            print(clientes.contar_pendientes(pendientes))

        elif op == 10:
            print(clientes.mostrar_siguiente_pendiente(pendientes))

        elif op == 11:
            print(clientes.mostrar_pendientes(pendientes))

        elif op == 12:
            print(listos.mostrar_atendidos(atendidos))

        elif op == 13:
            print("Pendientes: ", clientes.mostrar_pendientes(pendientes))
            print("Atendidos: ", listos.mostrar_atendidos(atendidos))

        elif op == 14:
            print(listas.contar_totales(pendientes, atendidos))

        elif op == 15:

            break

        else:
            print(errores.error_generico())

