from flask import Flask
import clientes, listos, listas

app = Flask(__name__)

@app.route("/")
def inicio():
    return "===___BIENVENIDO___==="

while True:
    print(menu())
    try:
        op = int(input("Ingrese su opcion a realizar: "))
    except ValueError:
        print(error_generico())
        continue

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
        print(mostrar_UltAtend(atendidos))

    elif op == 7:
        print(mostrar_UltPend(pendientes))

    elif op == 8:
        print(contar_atendidos(atendidos))

    elif op == 9:
        print(contar_pendientes(pendientes))

    elif op == 10:
        print(mostrar_siguiente_pendiente(pendientes))

    elif op == 11:
        print(mostrar_pendientes(pendientes))

    elif op == 12:
        print(mostrar_atendidos(atendidos))

    elif op == 13:
        print("Pendientes: ", mostrar_pendientes(pendientes))
        print("Atendidos: ", mostrar_atendidos(atendidos))

    elif op == 14:
        print(contar_totales(pendientes, atendidos))

    elif op == 15:

        break

    else:
        print(error_generico())


if __name__ == "__name__":
    app.run(debug=True)
