from flask_sqlalchemy import SQLAlchemy

# Configuración de la base de datos
DATABASE_URI = 'mysql+pymysql://root:cuentaMYSQLROOT195@localhost/biblioteca02'

db = SQLAlchemy()
