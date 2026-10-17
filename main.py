from flask import Flask
import selector
app = Flask(__name__)

@app.route("/")
def inicio():
    return "===___BIENVENIDO___==="

pendientes = []
atendidos = []

print(selector.selector_opcion(pendientes, atendidos))

if __name__ == "__name__":
    app.run(debug=True)

#Hola profe
