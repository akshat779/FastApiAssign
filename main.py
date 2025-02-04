from fastapi import FastAPI
from  src.routers import userRouter
from  src.models import models
from  src.utils.database import engine
app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(userRouter.router)

