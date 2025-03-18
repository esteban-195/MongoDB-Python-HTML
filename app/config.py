from pymongo import MongoClient

# Configuración de la conexión con MongoDB
MONGO_URI = "mongodb://localhost:27017"
client = MongoClient(MONGO_URI)
db = client.biblioteca  # Nombre de la base de datos
