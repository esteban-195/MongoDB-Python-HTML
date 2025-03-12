from flask import Flask, jsonify, request, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

# Configuración de MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/biblioteca"
mongo = PyMongo(app)

@app.route("/")
def home():
    return "¡La API de la biblioteca está funcionando!"

# Agregar un libro
@app.route("/libros", methods=["POST"])
def agregar_libro():
    data = request.json
    if not data or not "titulo" in data:
        return jsonify({"error": "Datos inválidos"}), 400

    mongo.db.libro.insert_one({
        "titulo": data["titulo"],
        "autor": data["autor"],
        "isbn": data["isbn"],
        "cantidad_ejemplares": data["cantidad_ejemplares"],
        "ejemplares_disponibles": data["ejemplares_disponibles"]
    })
    
    return jsonify({"mensaje": "Libro agregado"}), 201

# Obtener todos los libros
@app.route("/libros", methods=["GET"])
def obtener_libros():
    libros = list(mongo.db.libro.find({}, {"_id": 0}))
    return jsonify(libros)

# Buscar un libro por título
@app.route("/libros/<titulo>", methods=["GET"])
def buscar_libro(titulo):
    libro = mongo.db.libro.find_one({"titulo": titulo}, {"_id": 0})
    if libro:
        return jsonify(libro)
    return jsonify({"error": "Libro no encontrado"}), 404

# Ruta para el frontend (Asegúrate de tener el archivo templates/index.html)
@app.route("/web")
def web():
    return render_template("index.html")

# ¡Coloca esto al final del archivo!
if __name__ == "__main__":
    app.run(debug=True)
