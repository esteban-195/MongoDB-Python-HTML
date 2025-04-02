from flask import Flask
from config import db
from routes import init_routes

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:cuentaMYSQLROOT195@localhost/biblioteca02'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
init_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
