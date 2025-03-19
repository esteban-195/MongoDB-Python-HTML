from flask import Flask
from flask_pymongo import PyMongo
from datetime import datetime, timedelta

app = Flask(__name__)

# Configuración de la base de datos MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/Biblioteca01"
mongo = PyMongo(app)

# Funciones para interactuar con la base de datos

def crear_usuario(nombre, email, telefono):
    usuario = {
        "nombre": nombre,
        "email": email,
        "telefono": telefono,
        "prestamos_activos": [],
        "reservas_activas": []
    }
    return mongo.db.usuario.insert_one(usuario).inserted_id

def agregar_libro(titulo, autor, isbn, cantidad_ejemplares):
    ejemplares = [{
        "_id": f"{isbn}-{i+1}",
        "estado": "available",
        "ubicacion": "Estantería A3"
    } for i in range(cantidad_ejemplares)]

    libro = {
        "titulo": titulo,
        "autor": autor,
        "isbn": isbn,
        "ejemplares": ejemplares
    }
    return mongo.db.libros.insert_one(libro).inserted_id

def realizar_prestamo(usuario_id, isbn):
    usuario = mongo.db.usuario.find_one({"_id": usuario_id})
    libro = mongo.db.libros.find_one({"isbn": isbn})

    if not usuario or not libro:
        return "Usuario o libro no encontrado."

    # Buscar un ejemplar disponible
    for ejemplar in libro["ejemplares"]:
        if ejemplar["estado"] == "available":
            ejemplar["estado"] = "borrowed"
            fecha_prestamo = datetime.now()
            fecha_devolucion = fecha_prestamo + timedelta(days=14)

            prestamo = {
                "usuario_id": usuario_id,
                "isbn": isbn,
                "ejemplar_id": ejemplar["_id"],
                "fecha_prestamo": fecha_prestamo.strftime("%Y-%m-%d"),
                "fecha_devolucion": fecha_devolucion.strftime("%Y-%m-%d"),
                "estado": "active"
            }

            mongo.db.prestamos.insert_one(prestamo)
            mongo.db.libros.update_one({"_id": libro["_id"]}, {"$set": {"ejemplares": libro["ejemplares"]}})
            mongo.db.usuario.update_one({"_id": usuario_id}, {"$push": {"prestamos_activos": prestamo}})
            return "Préstamo realizado con éxito."

    return "No hay ejemplares disponibles para préstamo."

def devolver_libro(usuario_id, ejemplar_id):
    prestamo = mongo.db.prestamos.find_one({"usuario_id": usuario_id, "ejemplar_id": ejemplar_id, "estado": "active"})

    if not prestamo:
        return "No se encontró un préstamo activo para este usuario."

    mongo.db.prestamos.update_one({"_id": prestamo["_id"]}, {"$set": {"estado": "returned"}})
    mongo.db.historial_prestamos.insert_one(prestamo)

    mongo.db.libros.update_one(
        {"ejemplares._id": ejemplar_id},
        {"$set": {"ejemplares.$.estado": "available"}}
    )

    mongo.db.usuario.update_one(
        {"_id": usuario_id},
        {"$pull": {"prestamos_activos": {"ejemplar_id": ejemplar_id}}}
    )

    return "Libro devuelto con éxito."

