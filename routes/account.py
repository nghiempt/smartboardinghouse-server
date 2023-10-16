from fastapi import APIRouter
from models.account import account
from config.db import conn
from schemas.index import Account
accountRouter = APIRouter()


@accountRouter.get('/')
async def get_all_account():
    return Account.serializeList(conn.execute(account.select()).fetchall())


@accountRouter.get('/{id}')
async def get_one_account(id: int):
    return Account.serializeDict(conn.execute(account.select().where(account.c.id == id)).fetchone())


@accountRouter.post('/')
async def create_account(accountInput: Account):
    conn.execute(account.insert().values(
        username=accountInput.username,
        password=accountInput.password,
        role=accountInput.role,
        key=accountInput.key,
    ))
    conn.commit()
    return Account.serializeList(conn.execute(account.select()).fetchall())


@accountRouter.put('/{id}')
async def update_account(id: int, accountInput: Account):
    conn.execute(account.update().values(
        username=accountInput.username,
        password=accountInput.password,
        role=accountInput.role,
        key=accountInput.key,
    ).where(account.c.id == id))
    conn.commit()
    return Account.serializeList(conn.execute(account.select()).fetchall())


@accountRouter.delete('/{id}')
async def delete_account(id: int):
    conn.execute(account.delete().where(account.c.id == id))
    conn.commit()
    return Account.serializeList(conn.execute(account.select()).fetchall())
