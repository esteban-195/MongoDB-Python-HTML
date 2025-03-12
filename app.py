from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)

# Configuración de MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/biblioteca"
mongo = PyMongo(app)

@app.route("/")
def home():
    return "¡La API de la biblioteca está funcionando!"

@app.route("/web")
def web():
    return render_template("index.html")

# Ruta para procesar el formulario y agregar un libro
@app.route("/agregar_libro", methods=["POST"])
def agregar_libro():
    titulo = request.form.get("titulo")
    autor = request.form.get("autor")
    isbn = request.form.get("isbn")
    cantidad = request.form.get("cantidad")

    if not titulo or not autor or not isbn or not cantidad:
        return "Error: Faltan datos", 400

    # Insertar en la base de datos
    mongo.db.libro.insert_one({
        "titulo": titulo,
        "autor": autor,
        "isbn": isbn,
        "cantidad_ejemplares": int(cantidad),
        "ejemplares_disponibles": int(cantidad)
    })

    return redirect(url_for("web"))

# Ruta para obtener todos los libros
@app.route("/libros", methods=["GET"])
def obtener_libros():
    libros = list(mongo.db.libro.find({}, {"_id": 0}))
    return jsonify(libros)

if __name__ == "__main__":
    app.run(debug=True)
