"""MODELO: acceso a la base de datos (SQLite)."""
import os
import sqlite3

RUTA_BD = os.path.join(os.path.dirname(__file__), "..", "data", "escuela.db")


class AlumnoModel:
    def __init__(self, ruta_bd=RUTA_BD):
        self.ruta_bd = ruta_bd
        self.crear_tabla()

    def _conectar(self):
        conexion = sqlite3.connect(self.ruta_bd)
        conexion.row_factory = sqlite3.Row
        return conexion

    def crear_tabla(self):
        with self._conectar() as conexion:
            conexion.execute(
                """CREATE TABLE IF NOT EXISTS alumnos (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nombre TEXT NOT NULL,
                       carrera TEXT NOT NULL,
                       promedio REAL NOT NULL
                   )"""
            )

    def obtener_todos(self):
        with self._conectar() as conexion:
            filas = conexion.execute("SELECT * FROM alumnos ORDER BY id").fetchall()
        return [dict(f) for f in filas]

    def obtener_por_id(self, id_alumno):
        with self._conectar() as conexion:
            fila = conexion.execute("SELECT * FROM alumnos WHERE id = ?", (id_alumno,)).fetchone()
        return dict(fila) if fila else None

    def agregar(self, nombre, carrera, promedio):
        with self._conectar() as conexion:
            cursor = conexion.execute(
                "INSERT INTO alumnos (nombre, carrera, promedio) VALUES (?, ?, ?)",
                (nombre, carrera, promedio),
            )
        return cursor.lastrowid

    def eliminar(self, id_alumno):
        with self._conectar() as conexion:
            conexion.execute("DELETE FROM alumnos WHERE id = ?", (id_alumno,))
