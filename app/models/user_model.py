import ormar
import sqlalchemy

from app.db import database, metadata
class User(ormar.Model):
    id: int
    cpf: str
    nome: str
    email: str
    telefone: str
    class Meta:
        tablename = "users"
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True, autoincrement=True)
    cpf: str = ormar.String(max_length=11, unique=True)
    nome: str = ormar.String(max_length=100)
    email: str = ormar.String(max_length=100)
    telefone: str = ormar.String(max_length=11)

engine = sqlalchemy.create_engine(str(database.url))
metadata.create_all(engine)
