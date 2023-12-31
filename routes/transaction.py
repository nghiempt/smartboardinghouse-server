from fastapi import APIRouter
from models._index import transaction, ResponseObject
from config.db import conn
from schemas._index import Transaction
import http.client as HTTP_STATUS_CODE
transactionRouter = APIRouter(prefix="/api/v1")

@transactionRouter.post('/transaction/create')
async def create_transaction(transaction_input: Transaction):
    # Insert a new transaction in the database
    conn.execute(transaction.insert().values(
        status = transaction_input.status,
        date = transaction_input.date,
        content = transaction_input.content,
        total = transaction_input.total,
        account_ID = transaction_input.account_ID
    ))
    conn.commit()
    status_code = HTTP_STATUS_CODE.CREATED
    status_message = HTTP_STATUS_CODE.responses[status_code]
    return ResponseObject(True, status_code, status_message, Transaction.serializeList(conn.execute(transaction.select().where(transaction.c.account_ID == transaction_input.account_ID)).fetchall()))

@transactionRouter.get('/transaction/detail/{ID}')
async def get_transaction_by_ID(ID: int):
    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]
    return ResponseObject(True, status_code, status_message, Transaction.serializeDict(conn.execute(transaction.select().where(transaction.c.ID == ID)).fetchone()))


@transactionRouter.get('/transaction/')
async def get_transactions_by_accountID(account_ID: int):
    # Query the database to get transactions that match the specified account_ID
    transactions = conn.execute(transaction.select().where(transaction.c.account_ID == account_ID)).fetchall()

    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]

    if not transactions:
        status_code = HTTP_STATUS_CODE.NOT_FOUND
        status_message = HTTP_STATUS_CODE.responses[status_code]
        return ResponseObject(False,status_code, status_message, "No transactions found")

    return ResponseObject(True, status_code, status_message, Transaction.serializeList(transactions))

@transactionRouter.put('/transaction/payment/{ID}')
async def update_transaction_status(ID: int):
    # Update a transaction in the database
    conn.execute(transaction.update().where(transaction.c.ID == ID).values(status = 1))
    conn.commit()
    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]
    return ResponseObject(True, status_code, status_message, Transaction.serializeDict(conn.execute(transaction.select().where(transaction.c.ID == ID)).fetchone()))