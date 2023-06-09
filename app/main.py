from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.services.user_services import router
from app.db import database

import app.services

app = FastAPI(title='CODHAB - Processo Seletivo (CRUD de Usurários)')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(router, prefix='/user')