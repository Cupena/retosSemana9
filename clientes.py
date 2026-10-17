

def evaluar_cero(lista):
    return len(lista) == 0

def agregar_cliente(pendientes):
    cliente = input("Ingrese nombre del cliente: ")
    pendientes.append(cliente)
    return f"Se ha añadido el cliente: {cliente}"

def revertir_cliente(pendientes):
    if evaluar_cero(pendientes):
        return "No hay clientes por revertir."
    else:
        cliente_revertido = pendientes.pop()
        return f"Se ha revertido {cliente_revertido}"

def mostrar_siguienteLista(pendientes):
    return f"El siguiente en la lista: {pendientes[0]}"

def mostrar_pendientes(pendientes):
    if evaluar_cero(pendientes):
        return "No hay pendientes."
    else:
        return pendientes

def mover_alUltimo(pendientes):
    cliente = pendientes.pop(0)
    pendientes.append(cliente)
    return f"Se ha movido a {cliente} a la ultima posicion."

def mostrar_UltPend(pendientes):
    if evaluar_cero(pendientes):
        return "No hay clientes pendientes."
    else:
        return f"El ultimo cliente pendiente es: {pendientes[-1]}"

def mostrar_siguiente_pendiente(pendientes):
    return f"El siguiente en la lista es: {pendientes[0]}"

def contar_pendientes(pendientes):
    return f"Tiene una cantidad de: {len(pendientes)} en espera."