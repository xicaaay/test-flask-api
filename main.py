from flask import Flask, jsonify, request

app = Flask(__name__)



'''
GET -> Obtener información
POST -> Crear información
PUT -> Actualizar información
DELETE -> Borrar información
'''

@app.route("/")
def home():
    return "home"


@app.route("/users/<user_id>")
def getUser(user_id):
    user = {"id": user_id, "name": "test", "teléfono": "333 3333"}
    
    #/users/2332?query=queryTest
    query = request.args.get('query') 
    if query:
        user["query"] = query
    
    return jsonify(user), 200

@app.route("/users", methods=["POST"])
def createUser():
    data = request.get_json()
    data["status"] = "user crated"
    return jsonify(data), 201

@app.route("/holamundo")
def hola():
    return "Hola Mundo"

# Entorno virtual: .\.venv\Scripts\Activate.ps1
# flask --app main run / python nombreDelArchivo (ejemplo: main.py)
# Comando para levantar el servidor

if __name__=='__main__':
    app.run(debug=True)