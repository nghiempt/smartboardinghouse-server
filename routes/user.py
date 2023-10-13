from fastapi import APIRouter
from models.user import users
from config.db import conn
from schemas.index import User
user = APIRouter()


@user.get('/')
async def get_all_users():
    return User.serializeList(conn.execute(users.select()).fetchall())


@user.get('/{id}')
async def get_one_user(id: int):
    return User.serializeDict(conn.execute(users.select().where(users.c.id == id)).fetchone())


@user.post('/')
async def create_user(user: User):
    conn.execute(users.insert().values(
        name=user.name,
        email=user.email,
        password=user.password,
    ))
    conn.commit()
    return User.serializeList(conn.execute(users.select()).fetchall())


@user.put('/{id}')
async def update_user(id: int, user: User):
    conn.execute(users.update().values(
        name=user.name,
        email=user.email,
        password=user.password,
    ).where(users.c.id == id))
    conn.commit
    return User.serializeList(conn.execute(users.select()).fetchall())


@user.delete('/{id}')
async def delete_user(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    conn.commit()
    return User.serializeList(conn.execute(users.select()).fetchall())
