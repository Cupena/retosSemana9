from flask import Flask

#la cola
pendientes = []
#La pila
atendidos = []


def agregar_atendidos(atendidos,pendientes):
    if evaluar_cero(pendientes):
        return "No hay pendientes por atender."
    else:
        atendido = pendientes.pop(0)
        atendidos.append(atendido)
        return f"Ha atendido a:, {atendido}"

def mostrar_ultimoAtendido(atendidos):
    return f"El ultimo atendido: {atendidos[-1]}" 

def revertir_atendido(pendientes, atendidos):
    cliente_regresado = atendidos.pop()
    pendientes.insert(0,cliente_regresado)
    return f"Se ha revertido el cliente atendido: {cliente_regresado}, y regresado como pendiente en su posicion 0."

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
    
def contar_atendidos(atendidos):
    return f"Se han atendido: {len(atendidos)} el dia de hoy."

def contar_totales(pendientes, atendidos):
    return f"El dia de hoy llegaron {len(pendientes) + len(atendidos)} al consultorio."


def error_generico():
    return "Ingrese un numero valido"

