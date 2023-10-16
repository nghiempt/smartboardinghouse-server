from fastapi import APIRouter, HTTPException
from models.account import account
from config.db import conn
from schemas.index import Login

loginRouter = APIRouter()

@loginRouter.post('/login')
async def login(user_credentials: Login):
    # Check if the provided username and password are valid
    user = conn.execute(account.select().where(
        account.c.username == user_credentials.username,
        account.c.password == user_credentials.password
    )).fetchone()

    if user is None:
        # Return an error response if the credentials are invalid
        raise HTTPException(status_code=401, detail="Invalid username and/or password")

    return {"message": "Login successful",
            "role": user.role}