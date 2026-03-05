from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session
from app.database import create_db, get_session
from app.schemas import AutorCreate
from app.crud import crear_autor, obtener_autores, obtener_autor, eliminar_autor
from fastapi import UploadFile, File
import shutil

app = FastAPI()
app.mount("/images", StaticFiles(directory="images"), name="images")

create_db()

@app.post("/upload-image")
def upload_image(file: UploadFile = File(...)):
    ruta = f"images/{file.filename}"
    
    with open(ruta, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"mensaje": "imagen subida", "ruta": ruta}

@app.post("/autores")
def crear(autor: AutorCreate, session: Session = Depends(get_session)):
    return crear_autor(session, autor)


@app.get("/autores")
def listar(session: Session = Depends(get_session)):
    return obtener_autores(session)


@app.get("/autores/{id}")
def detalle(id: int, session: Session = Depends(get_session)):

    autor = obtener_autor(session, id)

    if not autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")

    return autor


@app.delete("/autores/{id}")
def eliminar(id: int, session: Session = Depends(get_session)):
    return eliminar_autor(session, id)