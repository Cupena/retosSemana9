from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "===___BIENVENIDO___==="


#CODIGOOOO





if __name__ == "__name__":
    app.run(debug=True)
