from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.services.user_services import router

import app.services

app = FastAPI(title='CODHAB - Processo Seletivo (CRUD de Usurários)')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix='/user')