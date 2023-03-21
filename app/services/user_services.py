from typing import List
from fastapi import APIRouter, HTTPException

from ..db import database
from ..models.user_model import User

router = APIRouter()

@router.post("/users", response_model=User)
async def create_user(user: User):
    query = User(nome=user.nome, email=user.email, cpf=user.cpf, telefone=user.telefone)
    await query.save()
    return query

@router.get("/users", response_model=List[User])
async def get_users():
    query = User.objects.all()
    return query

@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    query = await User.objects.get(id=user_id)
    if not query:
        raise HTTPException(status_code=404, detail="Usuário não encontrado;")
    return query

@router.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    query = await User.objects.get(id=user_id)
    if not query:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    await query.update(nome=user.nome, email=user.email)
    return {"message": "User updated successfully"}

@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = await User.objects.get(id=user_id)
    if not query:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")