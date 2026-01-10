import os
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"
TEMPLATES_DIR = FRONTEND_DIR / "templates"
STATIC_DIR = FRONTEND_DIR / "static"

app = FastAPI(title="DIEMAR", docs_url=None, redoc_url=None)
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

if STATIC_DIR.exists() and STATIC_DIR.is_dir():
  app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@app.get("/", include_in_schema=False, response_class=HTMLResponse)
def home(request: Request):
  return templates.TemplateResponse("index.html", {"request": request})


@app.get("/gestion_integral", include_in_schema=False, response_class=HTMLResponse)
def gestion_integral(request: Request):
  return templates.TemplateResponse("gestion_integral.html", {"request": request})


@app.get("/tratamiento", include_in_schema=False, response_class=HTMLResponse)
def tratamiento(request: Request):
  return templates.TemplateResponse("tratamiento.html", {"request": request})


@app.get("/equipos", include_in_schema=False, response_class=HTMLResponse)
def equipos(request: Request):
  return templates.TemplateResponse("equipos.html", {"request": request})


@app.get("/robots.txt", include_in_schema=False)
def robots():
  return FileResponse(str(FRONTEND_DIR / "static" / "robots.txt"), media_type="text/plain")


@app.get("/sitemap.xml", include_in_schema=False)
def sitemap():
  return FileResponse(str(FRONTEND_DIR / "static" / "sitemap.xml"), media_type="application/xml")


@app.get("/health", include_in_schema=False)
def health():
  return {"status": "ok"}


if __name__ == "__main__":
  import uvicorn

  port = int(os.getenv("PORT", "8000"))
  uvicorn.run("app.main:app", host="0.0.0.0", port=port)
