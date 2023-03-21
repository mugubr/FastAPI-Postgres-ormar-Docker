import datetime

import ormar

from app.db import database, metadata
class User(ormar.Model):
    class Meta:
        tablename = "users"
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True, autoincrement=True)
    cpf: str = ormar.String(max_length=11, unique=True)
    nome: str = ormar.String(max_length=100)
    email: str = ormar.String(max_length=100)
    telefone: str = ormar.String(max_length=11)
    created_at: datetime.datetime = ormar.DateTime(default=datetime.datetime.utcnow)
    updated_at: datetime.datetime = ormar.DateTime(default=datetime.datetime.utcnow)