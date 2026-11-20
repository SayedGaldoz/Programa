"""VISTA: prepara los datos y genera el HTML con el template."""
from flask import render_template


class AlumnoView:
    def mostrar_lista(self, alumnos, mensaje=None):
        promedio_general = (
            round(sum(a["promedio"] for a in alumnos) / len(alumnos), 2) if alumnos else 0
        )
        return render_template(
            "index.html",
            alumnos=alumnos,
            total=len(alumnos),
            promedio_general=promedio_general,
            mensaje=mensaje,
        )
