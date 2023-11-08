from fastapi import APIRouter
from models._index import account, ResponseObject
from config.db import conn
from schemas._index import Login, Account
import http.client as HTTP_STATUS_CODE
import hashlib

loginRouter = APIRouter(prefix="/api/v1")

# Function to hash the password using MD5
def md5_hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

@loginRouter.post('/sign_in')
async def login(user_credentials: Login):
    # Check if the provIDed username and password are valID
    user = conn.execute(account.select().where(
        account.c.username == user_credentials.username,
        account.c.password == md5_hash_password(user_credentials.password)
    )).fetchone()

    if user is None:
        # Return an error response if the credentials are invalID
        status_code = HTTP_STATUS_CODE.UNAUTHORIZED
        status_message = HTTP_STATUS_CODE.responses[status_code]
        return ResponseObject(False, status_code, status_message, "Invalid Username and/or Password")

    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]
    dict = [user.role, user.ID]
    return ResponseObject(True, status_code, status_message, Login.serializeDict(dict))