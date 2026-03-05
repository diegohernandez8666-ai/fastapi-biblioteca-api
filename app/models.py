from sqlmodel import SQLModel, Field
from typing import Optional

class Autor(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    nacionalidad: str


class Libro(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    descripcion: str
    autor_id: int
    portada: Optional[str] = None