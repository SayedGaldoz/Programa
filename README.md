# Programa

Repositorio de la clase.

## Estructura del proyecto

```
Programa/
├── README.md          # Descripción del proyecto
├── requirements.txt   # Librerías de Python que necesita el proyecto
├── .gitignore         # Archivos y carpetas que Git no debe subir
├── data/              # Datos de entrada (CSV, Excel, etc.)
├── src/               # Código fuente (patrón MVC)
│   ├── app.py         # Punto de entrada: crea la app y registra el controlador
│   ├── model.py       # MODELO: base de datos SQLite (tabla alumnos)
│   ├── view.py        # VISTA: genera el HTML a partir del template
│   ├── controller.py  # CONTROLADOR: rutas, valida datos y une modelo y vista
│   ├── templates/
│   │   └── index.html # Template HTML de la vista
│   └── static/
│       └── estilos.css
└── test/
    └── test_model.py  # Pruebas del modelo
```

## Patrón MVC

- **Modelo (`model.py`):** se conecta a la base de datos `data/escuela.db`, crea la tabla `alumnos` y realiza las operaciones (consultar, agregar, eliminar).
- **Vista (`view.py` + `templates/index.html`):** recibe los datos ya listos y los muestra en la página HTML.
- **Controlador (`controller.py`):** recibe las peticiones del navegador, valida los datos, llama al modelo y devuelve la vista.

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
cd src
python app.py
```

Abrir http://127.0.0.1:5000 en el navegador.

## Pruebas

```bash
python -m unittest discover test
```

## Autor

Sayed Galdoz
