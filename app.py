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

# Agregar un libro
@app.route("/agregar_libro", methods=["POST"])
def agregar_libro():
    titulo = request.form.get("titulo")
    autor = request.form.get("autor")
    isbn = request.form.get("isbn")
    cantidad = request.form.get("cantidad")

    if not titulo or not autor or not isbn or not cantidad:
        return "Error: Faltan datos", 400

    mongo.db.libro.insert_one({
        "titulo": titulo,
        "autor": autor,
        "isbn": isbn,
        "cantidad_ejemplares": int(cantidad),
        "ejemplares_disponibles": int(cantidad)
    })

    return redirect(url_for("web"))

# Actualizar un libro
@app.route("/actualizar_libro", methods=["POST"])
def actualizar_libro():
    titulo = request.form.get("titulo_actualizar")
    nuevo_autor = request.form.get("nuevo_autor")
    nuevo_isbn = request.form.get("nuevo_isbn")
    nueva_cantidad = request.form.get("nueva_cantidad")

    actualizacion = {}
    if nuevo_autor:
        actualizacion["autor"] = nuevo_autor
    if nuevo_isbn:
        actualizacion["isbn"] = nuevo_isbn
    if nueva_cantidad:
        actualizacion["cantidad_ejemplares"] = int(nueva_cantidad)
        actualizacion["ejemplares_disponibles"] = int(nueva_cantidad)

    if actualizacion:
        mongo.db.libro.update_one({"titulo": titulo}, {"$set": actualizacion})

    return redirect(url_for("web"))

# Eliminar un libro
@app.route("/eliminar_libro", methods=["POST"])
def eliminar_libro():
    titulo = request.form.get("titulo_eliminar")

    mongo.db.libro.delete_one({"titulo": titulo})

    return redirect(url_for("web"))

# Obtener todos los libros
@app.route("/libros", methods=["GET"])
def obtener_libros():
    libros = list(mongo.db.libro.find({}, {"_id": 0}))
    return jsonify(libros)

if __name__ == "__main__":
    app.run(debug=True)
