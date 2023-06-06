from fastapi import APIRouter
from models.user import User
from config.database import con
from schemas.user import userEntity, usersEntity



user = APIRouter()


@user.get('/usuarios')
async def get_usuarios():
    return usersEntity(con.local.user.find())


@user.post('/usuarios')
async def post_usuario(user: User):
    id=con.local.user.insert_one(dict(user)).inserted_id
    user=con.local.user.find_one({"_id": id})
    return userEntity(user)

@user.get('/usuarios/{correo}/')
async def get_email(correo:str):
    return userEntity(con.local.user.find_one({"email": correo}))
    