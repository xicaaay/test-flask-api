# API REST con Python y FastAPI

Este proyecto es una API REST desarrollada con Python y FastAPI.

## Requisitos

Antes de ejecutar el proyecto, es necesario tener instalado:

* Python 3.10 o superior
* `pip`
* Git, opcional
* Visual Studio Code, recomendado

Para verificar la versión de Python:

```powershell
python --version
```

También puede utilizarse:

```powershell
py --version
```

Para verificar que `pip` está instalado:

```powershell
python -m pip --version
```

---

## 1. Clonar o abrir el proyecto

Entrar a la carpeta del proyecto:

```powershell
cd D:\Proyectos\Amilcar\restPython
```

Verificar que se está en la carpeta correcta:

```powershell
Get-Location
```

Listar los archivos:

```powershell
Get-ChildItem
```

---

## 2. Crear el entorno virtual

El entorno virtual permite instalar dependencias de Python de forma aislada para este proyecto.

Ejecutar:

```powershell
python -m venv .venv
```

Esto crea la carpeta:

```text
.venv/
```

La estructura inicial del proyecto puede verse así:

```text
restPython/
├── .venv/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

El entorno virtual solo debe crearse una vez.

---

## 3. Activar el entorno virtual

### PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

Cuando el entorno esté activo, la terminal mostrará algo parecido a:

```text
(.venv) PS D:\Proyectos\Amilcar\restPython>
```

### CMD

En el símbolo del sistema de Windows:

```cmd
.venv\Scripts\activate.bat
```

### Git Bash

```bash
source .venv/Scripts/activate
```

Es importante utilizar el comando correspondiente a la terminal actual.

---

## 4. Error de ejecución de scripts en PowerShell

Si PowerShell muestra un error parecido a:

```text
La ejecución de scripts está deshabilitada en este sistema
```

Ejecutar:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

PowerShell solicitará confirmación. Después, volver a activar el entorno:

```powershell
.\.venv\Scripts\Activate.ps1
```

También puede habilitarse solamente para la terminal actual:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
```

Luego:

```powershell
.\.venv\Scripts\Activate.ps1
```

La opción `Process` solamente aplica mientras esa ventana de PowerShell permanezca abierta.

---

## 5. Actualizar pip

Con el entorno virtual activo:

```powershell
python -m pip install --upgrade pip
```

---

## 6. Instalar FastAPI

Instalar FastAPI junto con sus herramientas estándar:

```powershell
python -m pip install "fastapi[standard]"
```

Esta instalación incluye el servidor necesario para ejecutar la API durante el desarrollo.

Verificar las dependencias instaladas:

```powershell
python -m pip list
```

---

## 7. Crear el archivo principal

Crear un archivo llamado:

```text
main.py
```

Código básico:

```python
from fastapi import FastAPI


app = FastAPI(
    title="Mi primera API REST",
    description="API creada con Python y FastAPI",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "La API está funcionando correctamente"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }
```

---

## 8. Ejecutar la API

Con el entorno virtual activo:

```powershell
fastapi dev main.py
```

También puede ejecutarse con:

```powershell
python -m fastapi dev main.py
```

La API estará disponible en:

```text
http://127.0.0.1:8000
```

La documentación Swagger estará disponible en:

```text
http://127.0.0.1:8000/docs
```

La documentación alternativa ReDoc estará disponible en:

```text
http://127.0.0.1:8000/redoc
```

---

## 9. Detener la API

Para detener el servidor:

```text
Ctrl + C
```

---

## 10. Desactivar el entorno virtual

Cuando se termine de trabajar:

```powershell
deactivate
```

El texto `(.venv)` desaparecerá de la terminal.

---

## 11. Volver a trabajar en el proyecto

Cada vez que se abra nuevamente el proyecto, no es necesario recrear el entorno virtual.

Solo se debe entrar a la carpeta:

```powershell
cd D:\Proyectos\Amilcar\restPython
```

Activar el entorno:

```powershell
.\.venv\Scripts\Activate.ps1
```

Y levantar la API:

```powershell
fastapi dev main.py
```

Flujo diario:

```powershell
cd D:\Proyectos\Amilcar\restPython
.\.venv\Scripts\Activate.ps1
fastapi dev main.py
```

---

## 12. Generar el archivo de dependencias

Después de instalar las dependencias necesarias:

```powershell
python -m pip freeze > requirements.txt
```

El archivo `requirements.txt` contendrá versiones similares a:

```text
fastapi==0.x.x
pydantic==2.x.x
uvicorn==0.x.x
```

No es recomendable modificar manualmente las versiones sin conocer sus compatibilidades.

---

## 13. Instalar dependencias desde requirements.txt

Cuando el proyecto se descargue en otra computadora:

```powershell
python -m pip install -r requirements.txt
```

El flujo completo sería:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
fastapi dev main.py
```

---

## 14. Archivo .gitignore

Crear un archivo llamado:

```text
.gitignore
```

Agregar:

```gitignore
# Entorno virtual
.venv/
venv/

# Variables de entorno
.env

# Caché de Python
__pycache__/
*.py[cod]
*$py.class

# Herramientas de pruebas y análisis
.pytest_cache/
.mypy_cache/
.ruff_cache/

# Archivos del editor
.vscode/
.idea/

# Archivos del sistema operativo
.DS_Store
Thumbs.db
```

La carpeta `.venv` no debe subirse al repositorio porque contiene archivos específicos de cada sistema operativo y puede regenerarse utilizando `requirements.txt`.

---

## 15. Verificar qué Python se está utilizando

Con el entorno activo:

```powershell
python -c "import sys; print(sys.executable)"
```

El resultado debería apuntar al entorno virtual:

```text
D:\Proyectos\Amilcar\restPython\.venv\Scripts\python.exe
```

También puede comprobarse con:

```powershell
Get-Command python
```

---

## 16. Solución de problemas comunes

### El comando `python` no existe

Probar:

```powershell
py --version
```

Crear el entorno con:

```powershell
py -m venv .venv
```

### El entorno no se activa

En PowerShell debe utilizarse:

```powershell
.\.venv\Scripts\Activate.ps1
```

No utilizar:

```powershell
.venv\Scripts\activate.bat
```

El archivo `.bat` corresponde principalmente a CMD.

### El comando `fastapi` no existe

Asegurarse de que el entorno esté activo:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar FastAPI:

```powershell
python -m pip install "fastapi[standard]"
```

Ejecutar mediante Python:

```powershell
python -m fastapi dev main.py
```

### El puerto 8000 está ocupado

Ejecutar la API en otro puerto:

```powershell
fastapi dev main.py --port 8001
```

Abrir:

```text
http://127.0.0.1:8001/docs
```

### Se eliminó la carpeta .venv

Puede reconstruirse:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

---

## Comandos rápidos

### Primera instalación

```powershell
cd D:\Proyectos\Amilcar\restPython
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install "fastapi[standard]"
python -m pip freeze > requirements.txt
fastapi dev main.py
```

### Uso diario

```powershell
cd D:\Proyectos\Amilcar\restPython
.\.venv\Scripts\Activate.ps1
fastapi dev main.py
```

### Finalizar

```powershell
deactivate
```
