from fastapi import APIRouter
from models._index import account, ResponseObject
from config.db import conn
from schemas._index import Account
import http.client as HTTP_STATUS_CODE
accountRouter = APIRouter()


@accountRouter.get('/')
async def get_all_account():
    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]
    return ResponseObject(True, status_code, status_message, Account.serializeList(conn.execute(account.select()).fetchall()))


@accountRouter.get('/{id}')
async def get_one_account(id: int):
    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]
    return ResponseObject(True, status_code, status_message, Account.serializeDict(conn.execute(account.select().where(account.c.id == id)).fetchone()))


@accountRouter.post('/')
async def create_account(accountInput: Account):
    conn.execute(account.insert().values(
        username=accountInput.username,
        password=accountInput.password,
        role=accountInput.role,
        key=accountInput.key,
    ))
    conn.commit()
    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]
    return ResponseObject(True, status_code, status_message, Account.serializeList(conn.execute(account.select()).fetchall()))


@accountRouter.put('/{id}')
async def update_account(id: int, accountInput: Account):
    conn.execute(account.update().values(
        username=accountInput.username,
        password=accountInput.password,
        role=accountInput.role,
        key=accountInput.key,
    ).where(account.c.id == id))
    conn.commit()
    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]
    return ResponseObject(True, status_code, status_message, Account.serializeList(conn.execute(account.select()).fetchall()))


@accountRouter.delete('/{id}')
async def delete_account(id: int):
    conn.execute(account.delete().where(account.c.id == id))
    conn.commit()
    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]
    return ResponseObject(True, status_code, status_message, Account.serializeList(conn.execute(account.select()).fetchall()))
