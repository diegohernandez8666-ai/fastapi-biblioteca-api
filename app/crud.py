from sqlmodel import Session, select
from app.models import Autor

def crear_autor(session: Session, autor):

    nuevo = Autor(**autor.dict())

    session.add(nuevo)
    session.commit()
    session.refresh(nuevo)

    return nuevo


def obtener_autores(session: Session):

    return session.exec(select(Autor)).all()


def obtener_autor(session: Session, id):

    return session.get(Autor, id)


def eliminar_autor(session: Session, id):

    autor = session.get(Autor, id)

    if autor:
        session.delete(autor)
        session.commit()

    return autor