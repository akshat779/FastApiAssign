from fastapi import FastAPI
from  src.routers import userRouter
from src.routers import tenantRouter
from src.routers import productRouter
from  src.models import models
from  src.utils.database import engine
app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(userRouter.router)
app.include_router(tenantRouter.router)
app.include_router(productRouter.router)