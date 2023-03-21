from typing import List
from fastapi import APIRouter, HTTPException

from ..db import database
from ..models.user_model import User

router = APIRouter()

@router.post("/create_an_user", response_model=User, description='Criar um usuário', summary='Criar um usuário')
async def create_user(user: User):
    new_user = await User.objects.create(**user.dict(exclude_unset=True))
    return new_user


@router.get("/get_all_users", response_model=List[User], description='Listar todos os usuários', summary='Listar todos os usuários')
async def read_users():
    users = await User.objects.all()
    return users


@router.get("/get_an_user/{user_id}", response_model=User, description='Buscar usuário pelo ID',  summary='Buscar usuário pelo ID')
async def read_user(user_id: int):
    user = await User.objects.get_or_none(id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    return user


@router.put("/update_an_user/{user_id}", response_model=User, description='Atualizar dados de um usuário pelo ID', summary='Atualizar dados de um usuário pelo ID')
async def update_user(user_id: int, user: User):
    current_user = await User.objects.get_or_none(id=user_id)
    if current_user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    updated_user = user.dict(exclude_unset=True)
    for field in updated_user:
        setattr(current_user, field, updated_user[field])
    await current_user.update()
    return current_user


@router.delete("/delete_an_user/{user_id}", response_model=None, description='Excluir um usuário pelo ID', summary='Excluir um usuário pelo ID')
async def delete_user(user_id: int):
    user = await User.objects.get_or_none(id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    await user.delete()