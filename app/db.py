import databases
import sqlalchemy

DATABASE_URL = "postgresql://fastapi_user:password@postgresql_db:5432/fastapi_database"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(DATABASE_URL)

