# API REST basica con Python y Flask

Este proyecto contiene una API REST sencilla creada con Python y Flask.

Actualmente es un proyecto de practica: no usa base de datos, no tiene autenticacion y los datos de ejemplo se generan directamente dentro de `main.py`.

## Estado actual

Archivo principal:

```text
main.py
```

Framework usado:

```text
Flask
```

Puerto por defecto al ejecutar con `python main.py`:

```text
http://127.0.0.1:5000
```

## Estructura del proyecto

```text
restPython/
|-- .venv/
|-- __pycache__/
|-- .git/
|-- main.py
`-- README.md
```

Notas:

- `.venv/` es el entorno virtual local.
- `__pycache__/` es generado automaticamente por Python.
- `.git/` contiene la informacion interna del repositorio.
- No hay un archivo `requirements.txt` actualmente en la carpeta del proyecto.

## Requisitos

Antes de ejecutar el proyecto se necesita:

- Python 3.10 o superior.
- `pip`.
- PowerShell, CMD o una terminal compatible.

Verificar Python:

```powershell
python --version
```

Verificar pip:

```powershell
python -m pip --version
```

## Preparar el entorno virtual

Entrar a la carpeta del proyecto:

```powershell
cd D:\Proyectos\Amilcar\restPython
```

Crear el entorno virtual, si todavia no existe:

```powershell
python -m venv .venv
```

Activar el entorno virtual en PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Cuando este activo, la terminal mostrara algo parecido a:

```text
(.venv) PS D:\Proyectos\Amilcar\restPython>
```

Si PowerShell bloquea la activacion por politicas de ejecucion, se puede habilitar solo para la terminal actual:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\.venv\Scripts\Activate.ps1
```

## Instalar dependencias

El proyecto usa Flask. Si no esta instalado en el entorno virtual:

```powershell
python -m pip install Flask
```

Verificar que Flask quedo instalado:

```powershell
python -m pip show Flask
```

## Ejecutar la API

Con el entorno virtual activo:

```powershell
python main.py
```

La aplicacion se levanta en modo debug porque `main.py` contiene:

```python
app.run(debug=True)
```

Abrir en el navegador:

```text
http://127.0.0.1:5000
```

Para detener el servidor:

```text
Ctrl + C
```

## Rutas disponibles

### GET /

Ruta inicial de prueba.

Respuesta:

```text
home
```

Ejemplo:

```powershell
Invoke-RestMethod http://127.0.0.1:5000/
```

### GET /holamundo

Devuelve un texto simple.

Respuesta:

```text
Hola Mundo
```

Ejemplo:

```powershell
Invoke-RestMethod http://127.0.0.1:5000/holamundo
```

### GET /users/<user_id>

Devuelve un usuario de ejemplo usando el `user_id` recibido en la URL.

Ejemplo:

```powershell
Invoke-RestMethod http://127.0.0.1:5000/users/2332
```

Respuesta esperada:

```json
{
  "id": "2332",
  "name": "test",
  "tel\u00e9fono": "333 3333"
}
```

La ruta tambien acepta un parametro opcional llamado `query`.

Ejemplo:

```powershell
Invoke-RestMethod "http://127.0.0.1:5000/users/2332?query=queryTest"
```

Respuesta esperada:

```json
{
  "id": "2332",
  "name": "test",
  "tel\u00e9fono": "333 3333",
  "query": "queryTest"
}
```

### POST /users

Recibe un JSON en el cuerpo de la peticion, agrega un campo `status` y devuelve el resultado.

Ejemplo:

```powershell
Invoke-RestMethod `
  -Uri http://127.0.0.1:5000/users `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"name":"Amilcar","telefono":"333 3333"}'
```

Respuesta esperada:

```json
{
  "name": "Amilcar",
  "telefono": "333 3333",
  "status": "user crated"
}
```

Nota: el texto actual devuelto por el codigo es `user crated`. Si se quiere corregir el mensaje, habria que cambiarlo en `main.py`.

## Resumen de endpoints

| Metodo | Ruta | Descripcion |
| --- | --- | --- |
| GET | `/` | Devuelve `home`. |
| GET | `/holamundo` | Devuelve `Hola Mundo`. |
| GET | `/users/<user_id>` | Devuelve un usuario de ejemplo. |
| POST | `/users` | Recibe JSON y devuelve el mismo contenido con un campo `status`. |

## Flujo diario de trabajo

```powershell
cd D:\Proyectos\Amilcar\restPython
.\.venv\Scripts\Activate.ps1
python main.py
```

## Generar requirements.txt

Actualmente el proyecto no incluye `requirements.txt`. Para generarlo desde el entorno virtual activo:

```powershell
python -m pip freeze > requirements.txt
```

Luego, en otra computadora o instalacion limpia, se podrian instalar las dependencias con:

```powershell
python -m pip install -r requirements.txt
```

## Limitaciones actuales

- Los usuarios no se guardan en una base de datos.
- El endpoint `GET /users/<user_id>` siempre devuelve el mismo nombre y telefono de ejemplo.
- El endpoint `POST /users` no valida que el JSON tenga campos especificos.
- No hay manejo personalizado de errores.
- No hay pruebas automatizadas.
- No hay autenticacion ni autorizacion.
- No hay documentacion Swagger automatica, porque el proyecto usa Flask directamente y no FastAPI.

## Posibles siguientes mejoras

- Corregir el texto `user crated` a `user created`.
- Agregar `requirements.txt`.
- Agregar un `.gitignore` para excluir `.venv/`, `__pycache__/` y archivos temporales.
- Separar rutas en otro archivo si la API crece.
- Agregar validaciones para el JSON recibido en `POST /users`.
- Agregar una base de datos o almacenamiento en memoria mas estructurado.
- Agregar pruebas con `pytest`.
