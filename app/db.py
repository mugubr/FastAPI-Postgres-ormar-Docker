import os

import databases
import ormar
import sqlalchemy

DATABASE_URL = "postgresql://fastapi_user:password@localhost/fastapi_database"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

ormar_database = ormar.ModelMeta(
    "BaseModel",
    (ormar.Model,),
    {"metadata": metadata, "database": database}
)

async def connect_to_database():
    await database.connect()

async def close_database_connection():
    await database.disconnect()