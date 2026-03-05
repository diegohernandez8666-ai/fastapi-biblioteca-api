from pydantic import BaseModel, Field

class AutorCreate(BaseModel):

    nombre: str = Field(min_length=3, max_length=50)
    nacionalidad: str


class LibroCreate(BaseModel):

    titulo: str = Field(min_length=2)
    descripcion: str
    autor_id: int