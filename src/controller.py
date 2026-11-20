"""CONTROLADOR: recibe las peticiones, usa el modelo y responde con la vista."""
from flask import Blueprint, redirect, request, url_for

from model import AlumnoModel
from view import AlumnoView

controlador = Blueprint("alumnos", __name__)
modelo = AlumnoModel()
vista = AlumnoView()


@controlador.route("/")
def index():
    return vista.mostrar_lista(modelo.obtener_todos(), request.args.get("mensaje"))


@controlador.route("/agregar", methods=["POST"])
def agregar():
    nombre = request.form.get("nombre", "").strip()
    carrera = request.form.get("carrera", "").strip()
    try:
        promedio = float(request.form.get("promedio", ""))
    except ValueError:
        promedio = -1
    if not nombre or not carrera or not 0 <= promedio <= 10:
        return redirect(url_for("alumnos.index", mensaje="Datos inválidos: revisa nombre, carrera y promedio (0 a 10)."))
    modelo.agregar(nombre, carrera, promedio)
    return redirect(url_for("alumnos.index", mensaje=f"Alumno {nombre} agregado."))


@controlador.route("/eliminar/<int:id_alumno>", methods=["POST"])
def eliminar(id_alumno):
    modelo.eliminar(id_alumno)
    return redirect(url_for("alumnos.index", mensaje="Alumno eliminado."))
