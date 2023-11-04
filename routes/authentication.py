from fastapi import APIRouter
from models._index import account, ResponseObject
from config.db import conn
from schemas._index import Login
import http.client as HTTP_STATUS_CODE

loginRouter = APIRouter(prefix="/api/v1")

@loginRouter.post('/login')
async def login(user_credentials: Login):
    # Check if the provided username and password are valid
    user = conn.execute(account.select().where(
        account.c.username == user_credentials.username,
        account.c.password == user_credentials.password
    )).fetchone()

    if user is None:
        # Return an error response if the credentials are invalid
        status_code = HTTP_STATUS_CODE.UNAUTHORIZED
        status_message = HTTP_STATUS_CODE.responses[status_code]
        return ResponseObject(False, status_code, status_message, "Invalid Username and/or Password")

    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]
    return ResponseObject(True, status_code, status_message, user.role)
