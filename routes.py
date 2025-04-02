from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Libro, Usuario


def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/agregar_libro', methods=['GET', 'POST'])
    def agregar_libro():
        if request.method == 'POST':
            nombre = request.form['nombre']
            autor = request.form['autor']
            isbn = request.form['isbn']
            copias = request.form['copias']

            nuevo_libro = Libro(nombre=nombre, autor=autor, isbn=isbn, copias=copias, copias_disp=copias)
            db.session.add(nuevo_libro)
            db.session.commit()
            return redirect(url_for('index'))
        
        return render_template('agregar_libro.html')

    @app.route('/libros')
    def ver_libros():
        libros = Libro.query.all()
        return render_template('ver_libros.html', libros=libros)

    @app.route('/editar_libro/<int:libro_id>', methods=['GET', 'POST'])
    def editar_libro(libro_id):
        libro = Libro.query.get_or_404(libro_id)

        if request.method == 'POST':
            libro.nombre = request.form['nombre']
            libro.autor = request.form['autor']
            libro.isbn = request.form['isbn']
            libro.copias = request.form['copias']
            db.session.commit()
            return redirect(url_for('ver_libros'))
        
        return render_template('editar_libro.html', libro=libro)

    @app.route('/eliminar_libro/<int:libro_id>', methods=['GET', 'POST'])
    def eliminar_libro(libro_id):
        libro = Libro.query.get_or_404(libro_id)

        if request.method == 'POST':
            confirmacion = request.form['confirmacion']
            if confirmacion == libro.nombre:
                db.session.delete(libro)
                db.session.commit()
                return redirect(url_for('ver_libros'))
            else:
                return "El nombre no coincide. No se eliminó el libro.", 400

        return render_template('eliminar_libro.html', libro=libro)

    @app.route('/buscar_libro', methods=['GET'])
    def buscar_libro():
        query = request.args.get('q', '')
        libros = Libro.query.filter((Libro.nombre.ilike(f"%{query}%")) | (Libro.autor.ilike(f"%{query}%"))).all()
        return render_template('ver_libros.html', libros=libros, query=query)

    @app.route('/agregar_usuario', methods=['GET', 'POST'])
    def agregar_usuario():
        if request.method == 'POST':
            nombre = request.form.get('nombre', '').strip()
            email = request.form.get('email', '').strip()
            telefono = request.form.get('telefono', '').strip()

            # Validación: nombre y email son obligatorios, pero teléfono no
            if not nombre or not email:
                flash("El nombre y el email son obligatorios", "danger")
                return render_template('agregar_usuario.html')  # Volver a renderizar la misma página

            # Verificar si el email ya existe
            usuario_existente = Usuario.query.filter_by(email=email).first()
            if usuario_existente:
                flash("El email ya está registrado", "warning")
                return render_template('agregar_usuario.html')  # Volver a la misma página con el mensaje

            try:
                nuevo_usuario = Usuario(nombre=nombre, email=email, telefono=telefono if telefono else None)
                db.session.add(nuevo_usuario)
                db.session.commit()
                flash("Usuario agregado correctamente", "success")
            except Exception as e:
                db.session.rollback()
                flash(f"Error al agregar usuario: {str(e)}", "danger")

        return render_template('agregar_usuario.html')  # Siempre renderizar la misma página
    
    @app.route('/ver_usuarios')
    def ver_usuarios():
        query = request.args.get('q', '').strip()
        
        if query:
            usuarios = Usuario.query.filter(
                (Usuario.nombre.ilike(f"%{query}%")) | (Usuario.email.ilike(f"%{query}%"))
            ).all()
        else:
            usuarios = Usuario.query.all()
        
        return render_template('ver_usuarios.html', usuarios=usuarios)
    
    @app.route('/editar_usuario/<int:usuario_id>', methods=['GET', 'POST'])
    def editar_usuario(usuario_id):
        usuario = Usuario.query.get_or_404(usuario_id)
        
        if request.method == 'POST':
            usuario.telefono = request.form['telefono']
            db.session.commit()
            return redirect(url_for('ver_usuarios'))
        
        return render_template('editar_usuario.html', usuario=usuario)




