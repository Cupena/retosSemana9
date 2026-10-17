from flask import Flask

#la cola
pendientes = []
#La pila
atendidos = []

def evaluar_cero(lista):
    return len(lista) == 0

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

def mostrar_pendientes(pendientes):
    if evaluar_cero(pendientes):
        return "No hay pendientes."
    else:
        return pendientes

def mostrar_atendidos(atendidos):
    if evaluar_cero(atendidos):
        return "No hay lista de atendidos"
    else:
        return atendidos

def mostrar_UltAtend(atendidos):
    if evaluar_cero(atendidos):
        return "No hay clientes atendidos."
    else:
        return f"El último cliente atendido fue: {atendidos[-1]}"

def mostrar_UltPend(pendientes):
    if evaluar_cero(pendientes):
        return "No hay clientes pendientes."
    else:
        return f"El ultimo cliente pendiente es: {pendientes[-1]}"
    

def mostrar_siguiente_pendiente(pendientes):
    return f"El siguiente en la lista es: {pendientes[0]}"

def contar_atendidos(atendidos):
    return f"Se han atendido: {len(atendidos)} el dia de hoy."

def contar_pendientes(pendientes):
    return f"Tiene una cantidad de: {len(pendientes)} en espera."

def contar_totales(pendientes, atendidos):
    return f"El dia de hoy llegaron {len(pendientes) + len(atendidos)} al consultorio."

def menu():
    return """===MENU===
    1. Agregar cliente
    2. Agregar atendido
    3. Revertir cliente registrado
    4. Revertir atendido registrado
    5. Mover primero a ultimo
    6. Muestra ultimo atendido
    7. Mostrar ultimo pendiente
    8. Contar atendidos hoy
    9. Contar pendientes por hoy
    10. Muestra siguiente en la lista
    11. Muestra lista pendientes
    12. Muestra lista atendidos
    13. Muestra lista total
    14. Contar lista total
    14. Salir"""

def error_generico():
    return "Ingrese un numero valido"

