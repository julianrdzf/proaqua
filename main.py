import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"

app = FastAPI(title="DIEMAR", docs_url=None, redoc_url=None)

# Static assets (images, icons, etc.)
if STATIC_DIR.exists() and STATIC_DIR.is_dir():
  app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@app.get("/", include_in_schema=False)
def home():
  index_path = BASE_DIR / "index.html"
  return FileResponse(index_path)


@app.get("/styles.css", include_in_schema=False)
def styles():
  return FileResponse(BASE_DIR / "styles.css")


@app.get("/script.js", include_in_schema=False)
def script():
  return FileResponse(BASE_DIR / "script.js")


@app.get("/health", include_in_schema=False)
def health():
  return {"status": "ok"}


if __name__ == "__main__":
  import uvicorn

  port = int(os.getenv("PORT", "8000"))
  uvicorn.run("main:app", host="0.0.0.0", port=port)
