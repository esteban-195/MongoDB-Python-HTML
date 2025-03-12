from flask import Flask, render_template
from app.config import db

app = Flask(__name__)

# Ruta principal (Página de inicio)
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
