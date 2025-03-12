from flask import Flask, jsonify, request, render_template
from app.config import db

app = Flask(__name__)

# Ruta para obtener todos los libros
@app.route("/libros", methods=["GET"])
def get_books():
    libros = list(db.libro.find({}, {"_id": 0}))  # Obtener todos los libros
    return jsonify(libros)

# Ruta para registrar un préstamo
@app.route("/prestar", methods=["POST"])
def prestar_libro():
    data = request.json
    usuario_id = data.get("usuario_id")
    ejemplar_id = data.get("ejemplar_id")

    ejemplar = db.libro.find_one({"ejemplar._id": ejemplar_id, "ejemplar.estado": "available"})

    if ejemplar:
        db.libro.update_one({"ejemplar._id": ejemplar_id}, {"$set": {"ejemplar.$.estado": "borrowed"}})
        db.historial_prestamo.insert_one({
            "usuario_id": usuario_id,
            "ejemplar_id": ejemplar_id,
            "estado": "active"
        })
        return jsonify({"mensaje": "Préstamo registrado con éxito"})
    else:
        return jsonify({"error": "No hay ejemplares disponibles"}), 400
