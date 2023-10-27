from fastapi import FastAPI
from routes._index import accountRouter, loginRouter, houseRouter, postRouter
app = FastAPI()
app.include_router(accountRouter,tags=["Account"])
app.include_router(loginRouter,tags=["Authentication"])
app.include_router(houseRouter,tags=["Boarding House"])
app.include_router(postRouter,tags=["Post"])