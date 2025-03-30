from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
from flask_pymongo import PyMongo

app = Flask(__name__)

# Configuración de MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/Biblioteca01"
app.config["SECRET_KEY"] = "clave_secreta"  # Necesario para usar flash messages
mongo = PyMongo(app)


# @app.route("/")
# def home():
#     return "¡BIENVENIDO A LA BIBLIOTECA!"

@app.route("/")
def home():
    return render_template("index.html")

# Agregar un libro
@app.route("/agregar_libro", methods=["POST"])
def agregar_libro():
    titulo = request.form.get("titulo")
    autor = request.form.get("autor")
    isbn = request.form.get("isbn")
    cantidad = request.form.get("cantidad")

    if not titulo or not autor or not isbn or not cantidad:
            flash("Error: Faltan datos", "danger")
            return redirect(url_for("home"))

    mongo.db.libro.insert_one({
        "titulo": titulo,
        "autor": autor,
        "isbn": isbn,
        "cantidad_ejemplares": int(cantidad),
        "ejemplares_disponibles": int(cantidad)
    })

    flash(f"Libro '{titulo}' agregado correctamente", "success")
    return redirect(url_for("home"))


@app.route("/actualizar_libro", methods=["POST"])
def actualizar_libro():
    titulo_actual = request.form["titulo_actual"]
    titulo_nuevo = request.form["titulo_nuevo"]
    nuevo_autor = request.form["nuevo_autor"]
    nuevo_isbn = request.form["nuevo_isbn"]
    nueva_cantidad = request.form["nueva_cantidad"]
    nueva_cantidad = int(nueva_cantidad) if nueva_cantidad.strip() else None

    # Buscar el libro en la base de datos
    libro_existente = mongo.db.libro.find_one({"titulo": titulo_actual})

    if not libro_existente:
        flash("El libro con ese título no existe", "warning")
        return redirect(url_for("home"))

    # Construir los datos a actualizar
    nueva_data = {}
    if titulo_nuevo:
        nueva_data["titulo"] = titulo_nuevo
    if nuevo_autor:
        nueva_data["autor"] = nuevo_autor
    if nuevo_isbn:
        nueva_data["isbn"] = nuevo_isbn
    if nueva_cantidad:
        nueva_data["cantidad_ejemplares"] = nueva_cantidad  # 💡 Aquí se actualiza cantidad_ejemplares

    if not nueva_data:
        flash("No se realizaron cambios", "warning")
        return redirect(url_for("home"))

    # Realizar la actualización en la base de datos
    resultado = mongo.db.libro.update_one({"titulo": titulo_actual}, {"$set": nueva_data})

    if resultado.matched_count == 0:
        flash("No se encontró el libro", "warning")
    elif resultado.modified_count == 0:
        flash("No hubo cambios en los datos", "info")
    else:
        flash("Libro actualizado correctamente", "success")

    return redirect(url_for("home"))




# Eliminar un libro
@app.route("/eliminar_libro", methods=["POST"])
def eliminar_libro():
    titulo = request.form.get("titulo_eliminar")

    mongo.db.libro.delete_one({"titulo": titulo})

    return redirect(url_for("home"))

# Obtener todos los libros
@app.route("/libros", methods=["GET"])
def obtener_libros():
    libros = list(mongo.db.libro.find({}, {"_id": 0}))
    return jsonify(libros)

# Ruta para registrar usuarios
@app.route("/registrar_usuario", methods=["POST"])
def registrar_usuario():
    data = request.form

    if not data.get("nombre") or not data.get("email") or not data.get("telefono"):
        return jsonify({"error": "Faltan datos"}), 400

    nuevo_usuario = {
        "nombre": data["nombre"],
        "email": data["email"],
        "telefono": data["telefono"]
    }
    mongo.db.usuario.insert_one(nuevo_usuario)

    return jsonify({"mensaje": "Usuario registrado correctamente"}), 201

@app.route("/mostrar_libros")
def mostrar_libros():
    query = request.args.get("q", "").strip()
    
    if query:
        libros = list(mongo.db.libro.find({
            "$or": [
                {"titulo": {"$regex": query, "$options": "i"}},
                {"autor": {"$regex": query, "$options": "i"}},
                {"isbn": {"$regex": query, "$options": "i"}}
            ]
        }))
    else:
        libros = list(mongo.db.libro.find())

    return render_template("mostrar_libros.html", libros=libros)

@app.route('/mostrar_usuarios')
def mostrar_usuarios():
    usuarios = list(mongo.db.usuario.find({}, {"_id": 1, "nombre": 1, "email": 1, "telefono": 1, "prestamos_activos": 1, "reservas_activas": 1}))
    
    return render_template('mostrar_usuarios.html', usuarios=usuarios)

# Iniciar Flask
if __name__ == "__main__":
    app.run(debug=True)

