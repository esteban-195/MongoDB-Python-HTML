from config import db
from datetime import datetime


class Libro(db.Model):
    __tablename__ = 'libros'
    libro_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(500), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(100), unique=True, nullable=False)
    copias = db.Column(db.Integer)
    copias_disp = db.Column(db.Integer)

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    usuario_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefono = db.Column(db.String(20), nullable=True)  # Permitir NULL
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
