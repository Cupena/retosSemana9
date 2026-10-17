from flask import Flask

#la cola
pendientes = []
#La pila
atendidos = []

def evaluar_cero(pendientes):
    return len(pendientes) == 0

def agregar_cliente(pendientes):
    cliente = input("Ingrese nombre del cliente: ")
    pendientes.append(cliente)
    return f"Se ha añadido el cliente: {cliente}"

def agregar_atendidos(atendidos,pendientes):
    if evaluar_cero(pendientes):
        return "No hay pendientes por atender."
    else:
        atendido = pendientes.pop(0)
        atendidos.append(atendido)
        return f"Ha atendido a:, {atendido}"

#En caso de error, querer eliminar cliente sin afectar el proceso:
def revertir_cliente(pendientes):
    if evaluar_cero(pendientes):
        return "No hay clientes por revertir."
    else:
        cliente_revertido = pendientes.pop()
        return f"Se ha revertido {cliente_revertido}"

def mostrar_ultimoAtendido(atendidos):
    return f"El ultimo atendido: {atendidos[-1]}" 

def mostrar_siguienteLista(pendientes):
    return f"El siguiente en la lista: {pendientes[0]}"

def revertir_atendido(pendientes, atendidos):
    cliente_regresado = atendidos.pop()
    pendientes.insert(0,cliente_regresado)
    return f"Se ha revertido el cliente atendido: {cliente_regresado}, y regresado como pendiente en su posicion 0."

def mover_alUltimo(pendientes):
    cliente = pendientes.pop(0)
    pendientes.append(cliente)
    return f"Se ha movido a {cliente} a la ultima posicion."

def menu():
    return """===MENU===
    1. Agregar cliente
    2. Agregar atendido
    3. Revertir cliente registrado
    4. Revertir atendido registrado
    5. Mover primero a ultimo
    6. Muestra ultimo atendido
    7. Muestra siguiente en la lista
    8. Muestra lista pendientes
    9. Muestra lista atendidos
    10. Muestra lista total
    11. Salir"""

def error_generico():
    return "Ingrese un numero valido"

while True:
    print(menu())
    try:
        op = int(input("Ingrese su opcion a realizar: "))
    except ValueError:
        print(error_generico())

    if op == 1:
        print(agregar_cliente(pendientes))
    elif op == 2:
        print(agregar_atendidos(atendidos, pendientes))
    elif op == 3:
        print(revertir_cliente(pendientes))
    elif op == 4:
        print(revertir_atendido(pendientes, atendidos))
    elif op == 5:
        print(mover_alUltimo(pendientes))
    elif op == 6:
        pass
    elif op == 7:
        pass
    elif op == 8:
        pass
    elif op == 9:
        pass
    elif op == 0:
        break
    else:
        print(error_generico())

#Creacion nueva rama

