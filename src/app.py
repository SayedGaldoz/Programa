"""Punto de entrada de la aplicación (patrón MVC con Flask)."""
from flask import Flask

from controller import controlador

app = Flask(__name__)
app.register_blueprint(controlador)

if __name__ == "__main__":
    app.run(debug=True)
