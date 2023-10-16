from fastapi import FastAPI
from routes.index import accountRouter, loginRouter
app = FastAPI()
app.include_router(accountRouter,tags=["Account"])
app.include_router(loginRouter,tags=["Authentication"])
