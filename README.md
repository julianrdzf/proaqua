# ProAqua - Landing + FastAPI

Este proyecto sirve una landing page estática (HTML/CSS/JS) usando **FastAPI**.

## Requisitos

- Python 3.10+ (recomendado)

## Correr en local (Windows)

1) Crear y activar entorno virtual:

```powershell
python -m venv venv
venv\Scripts\activate
```

2) Instalar dependencias:

```powershell
pip install -r requirements.txt
```

3) Ejecutar el servidor:

```powershell
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

4) Abrir en el navegador:

- http://127.0.0.1:8000/

## Estructura

- `index.html`: landing page
- `styles.css`: estilos
- `script.js`: JS (menú móvil, etc.)
- `main.py`: servidor FastAPI
- `requirements.txt`: dependencias
- `Procfile`: comando de inicio para Railway

## Deploy en Railway (resumen)

Railway ejecuta el comando del `Procfile` y expone el puerto vía la variable `PORT`.

> Tip: no subas `venv/` al repo, está ignorado por `.gitignore`.
